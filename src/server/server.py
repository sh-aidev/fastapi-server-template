from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from src.utils.logger import logger
from src.utils.config import Config
from src.utils.exceptions import AppException, app_exception_handler


def get_router() -> APIRouter:
    v1Router = APIRouter()

    @v1Router.get("/health", status_code=200)
    def health() -> dict:
        return {"status": "ok"}

    @v1Router.get("/greet/{name}", status_code=200)
    def greet(name: str) -> dict:
        if not name.strip():
            raise AppException("Name must not be empty", status_code=400)
        return {"message": f"Hello, {name}!"}

    return v1Router


class Server:
    def __init__(self, cfg: Config) -> None:
        self.config = cfg
        logger.debug("Configs Loaded...")

        self.server = FastAPI(title="FastAPI Server Template")
        logger.debug("FastAPI server initialized...")
        self.server.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
        logger.debug("CORS Middleware added...")

        self.server.add_exception_handler(AppException, app_exception_handler)
        logger.debug("Exception handlers registered...")

        v1Router = get_router()
        logger.debug("Router initialized...")
        self.server.include_router(v1Router, prefix="/v1")
        logger.debug("Router added to server...")

    def serve(self) -> None:
        logger.debug(
            f"Starting FastAPI server at {self.config.app_config.server.host}:{self.config.app_config.server.port}"
        )
        uvicorn.run(
            self.server,
            host=self.config.app_config.server.host,
            port=self.config.app_config.server.port,
        )
