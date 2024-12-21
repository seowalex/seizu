from contextlib import asynccontextmanager

import httpx
from litestar import Litestar

from app.core import config
from app.core.config import settings
from app.core.stores import SQLiteStore
from app.routes import router


@asynccontextmanager
async def http_client(app: Litestar):
    async with httpx.AsyncClient(base_url=settings.YNAB_API_BASE_URL) as client:
        app.state.http_client = client

        yield


app = Litestar(
    [router],
    allowed_hosts=config.allowed_hosts,
    compression_config=config.compression,
    lifespan=[http_client],
    middleware=[config.session.middleware],
    stores={"sessions": SQLiteStore(settings.DB_PATH)},
)
