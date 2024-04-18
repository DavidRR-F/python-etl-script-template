from pydantic_settings import BaseSettings
from pydantic import computed_field
from logging.handlers import RotatingFileHandler
import logging


class Settings(BaseSettings):
    db_user: str
    db_pass: str
    db_host: str
    db_name: str
    db_dialect: str = "mssql+pyodbc"
    db_driver: str = "ODBC+Driver+17+for+SQL+Server"

    log_file: str = "logs/logfile.log"
    log_level: int = logging.INFO

    @computed_field
    @property
    def db_uri(self) -> str:
        return f"{self.db_dialect}://{self.db_user}:{self.db_pass}@{self.db_host}/{self.db_name}?driver={self.db_driver}"

    @computed_field
    @property
    def log_handler(self) -> RotatingFileHandler:
        return RotatingFileHandler(
            self.log_file, mode="a", maxBytes=10000000, backupCount=20
        )

    @computed_field
    @property
    def log_formatter(self) -> logging.Formatter:
        return logging.Formatter(
            fmt="%(asctime)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S %Z",
        )

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True


env = Settings()
