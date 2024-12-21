from datetime import timedelta
from os import PathLike
from pathlib import Path

import aiosqlite
from litestar.stores.base import StorageObject, Store


class SQLiteStore(Store):
    def __init__(self, path: PathLike[str] | str, table: str = "litestar"):
        self.path = Path(path)
        self.table = table

    async def __aenter__(self):
        async with aiosqlite.connect(self.path) as db:
            await db.execute(f"""
                CREATE TABLE IF NOT EXISTS "{self.table}" (
                    key TEXT PRIMARY KEY, value BLOB NOT NULL
                ) WITHOUT ROWID
            """)

    async def set(
        self, key: str, value: str | bytes, expires_in: int | timedelta | None = None
    ):
        if isinstance(value, str):
            value = value.encode()

        storage_obj = StorageObject.new(value, expires_in)

        async with aiosqlite.connect(self.path) as db:
            await db.execute(
                f"""
                    INSERT INTO "{self.table}" (key, value) VALUES (
                        ?, ?
                    ) ON CONFLICT DO UPDATE SET value
                    = excluded.value
                """,
                (key, storage_obj.to_bytes()),
            )
            await db.commit()

    async def get(self, key: str, renew_for: int | timedelta | None = None):
        async with aiosqlite.connect(self.path) as db:
            result = await db.execute(
                f'SELECT value FROM "{self.table}" WHERE key = ?', (key,)
            )

            if row := await result.fetchone():
                (value,) = row
                storage_obj = StorageObject.from_bytes(value)

                if storage_obj.expired:
                    await self.delete(key)

                    return None

                if renew_for and storage_obj.expires_at:
                    await self.set(key, storage_obj.data, renew_for)

                return storage_obj.data

        return None

    async def delete(self, key: str):
        async with aiosqlite.connect(self.path) as db:
            await db.execute(f'DELETE FROM "{self.table}" WHERE key = ?', (key,))
            await db.commit()

    async def delete_all(self):
        async with aiosqlite.connect(self.path) as db:
            await db.execute(f'DELETE FROM "{self.table}"')
            await db.commit()

    async def exists(self, key: str):
        async with aiosqlite.connect(self.path) as db:
            result = await db.execute(
                f"""
                    SELECT EXISTS(
                        SELECT 1 FROM "{self.table}"
                        WHERE key = ?
                    )
                """,
                (key,),
            )

            if row := await result.fetchone():
                (value,) = row

                return value == 1

        return False

    async def expires_in(self, key: str):
        async with aiosqlite.connect(self.path) as db:
            result = await db.execute(
                f'SELECT value FROM "{self.table}" WHERE key = ?', (key,)
            )

            if row := await result.fetchone():
                (value,) = row
                storage_obj = StorageObject.from_bytes(value)

                return storage_obj.expires_in

        return None
