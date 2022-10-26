from multiprocessing.util import LOGGER_NAME
from typing import List, Union

from pydantic import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str
    DB_URL: str

    class Config:
        case_sensitive = True
        env_file = ".env"

settings = Settings()