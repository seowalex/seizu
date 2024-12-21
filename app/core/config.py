import msgspec
from dotenv import dotenv_values
from litestar.config.allowed_hosts import AllowedHostsConfig
from litestar.config.compression import CompressionConfig
from litestar.middleware.session.server_side import ServerSideSessionConfig
from msgspec import Struct


class Settings(Struct, frozen=True, kw_only=True, forbid_unknown_fields=True):
    API_PREFIX: str = "/api/v1"

    DB_PATH: str = "db.sqlite3"

    YNAB_API_BASE_URL: str = "https://api.ynab.com/v1"
    YNAB_TOKEN: str

    @staticmethod
    def from_env():
        return msgspec.convert(dotenv_values(), Settings, strict=False)


settings = Settings.from_env()

allowed_hosts = AllowedHostsConfig(["localhost", "127.0.0.1"])
compression = CompressionConfig("brotli")
session = ServerSideSessionConfig(renew_on_access=True, secure=True, samesite="strict")
