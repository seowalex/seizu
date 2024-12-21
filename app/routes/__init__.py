import msgspec
from httpx import HTTPStatusError
from litestar import Request, Router
from litestar.datastructures import State
from litestar.exceptions import HTTPException
from litestar.middleware.rate_limit import RateLimitConfig

from app.core.config import settings
from app.core.models import ErrorResponse
from app.routes.transactions import TransactionController

rate_limit = RateLimitConfig(rate_limit=("hour", 200))


async def http_client(state: State):
    return state.http_client


def api_exception_handler(_: Request, exc: HTTPStatusError):
    error = msgspec.json.decode(exc.response.content, type=ErrorResponse).error

    raise HTTPException(detail=error.detail, status_code=exc.response.status_code)


router = Router(
    settings.API_PREFIX,
    dependencies={"client": http_client},
    exception_handlers={HTTPStatusError: api_exception_handler},
    middleware=[rate_limit.middleware],
    route_handlers=[TransactionController],
)
