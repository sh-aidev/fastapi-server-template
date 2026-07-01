from pydantic import BaseModel


class Logger(BaseModel):
    environment: str


class Server(BaseModel):
    host: str
    port: int


class AppConfig(BaseModel):
    logger: Logger
    server: Server
