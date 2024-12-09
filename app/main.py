from contextlib import asynccontextmanager
from fastapi import FastAPI
from starlette.middleware.base import BaseHTTPMiddleware
from app.models import db_user_model
from app.core.constants import BASE_URL
from app.api.api_v1.auth_routes import auth_router
from app.database import engine
from app.core.logger_middleware import logger_middleware


@asynccontextmanager
async def lifespan(app: FastAPI):
    db_user_model.Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(root_path=BASE_URL, lifespan=lifespan)
app.add_middleware(BaseHTTPMiddleware, dispatch=logger_middleware)

app.include_router(router=auth_router, tags=["auth"])

# db_user_model.Base.metadata.drop_all(bind=engine)
