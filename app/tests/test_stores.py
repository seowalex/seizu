import string
import tempfile
from datetime import datetime, timedelta

import pytest
import time_machine
from litestar.stores.base import Store
from time_machine import Coordinates

from app.core.stores import SQLiteStore


@pytest.fixture
async def store():
    with tempfile.NamedTemporaryFile() as f:
        store = SQLiteStore(f.name)

        async with store:
            yield store


@pytest.fixture
def frozen_datetime():
    with time_machine.travel(datetime.now, tick=False) as frozen:
        yield frozen


async def test_get(store: Store):
    key = "key"
    value = b"value"

    assert await store.get("foo") is None

    await store.set(key, value, expires_in=60)

    stored_value = await store.get(key)

    assert stored_value == value


async def test_set(store: Store):
    values = {"key_1": b"value_1", "key_2": "value_2"}

    for key, value in values.items():
        await store.set(key, value)

    for key, value in values.items():
        stored_value = await store.get(key)

        assert stored_value == value if isinstance(value, bytes) else value.encode()


@pytest.mark.parametrize("key", [*list(string.punctuation), "foo\xc3\xbc", ".."])
async def test_set_special_chars_key(store: Store, key: str):
    value = b"value"

    await store.set(key, value)

    assert await store.get(key) == value


async def test_expires(store: Store, frozen_datetime: Coordinates):
    await store.set("foo", b"bar", expires_in=1)

    frozen_datetime.shift(2)

    stored_value = await store.get("foo")

    assert stored_value is None


@pytest.mark.parametrize("renew_for", [10, timedelta(seconds=10)])
async def test_get_and_renew(
    store: Store, renew_for: int | timedelta, frozen_datetime: Coordinates
):
    await store.set("foo", b"bar", expires_in=1)
    await store.get("foo", renew_for)

    frozen_datetime.shift(2)

    stored_value = await store.get("foo")

    assert stored_value is not None


async def test_delete(store: Store):
    key = "key"

    await store.set(key, b"value", expires_in=60)
    await store.delete(key)

    value = await store.get(key)

    assert value is None


async def test_delete_empty(store: Store):
    await store.delete("foo")


async def test_exists(store: Store):
    assert await store.exists("foo") is False

    await store.set("foo", b"bar")

    assert await store.exists("foo") is True


async def test_expires_in_not_set(store: Store):
    assert await store.expires_in("foo") is None

    await store.set("foo", b"bar")

    assert await store.expires_in("foo") == -1


async def test_delete_all(store: Store):
    keys = []

    for i in range(10):
        key = f"key-{i}"
        keys.append(key)

        await store.set(key, b"value", expires_in=10 if i % 2 else None)

    await store.delete_all()

    for key in keys:
        assert await store.get(key) is None


async def test_db_path(store: SQLiteStore):
    await store.set("foo", b"bar")

    assert store.path.exists()
