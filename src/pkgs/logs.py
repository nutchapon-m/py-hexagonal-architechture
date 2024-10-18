import logging
import logging.config as log_conf
from logging import Logger

LOGGING_CONFIG: dict[str,] = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "()": "uvicorn.logging.DefaultFormatter",
            "fmt": "%(levelprefix)s %(asctime)s | %(message)s",
            "use_colors": None,
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
        "access": {
            "()": "uvicorn.logging.AccessFormatter",
            "fmt": '%(levelprefix)s %(asctime)s | %(client_addr)s | "%(request_line)s" | %(status_code)s',  # noqa: E501
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
        "app" : {
            "()": "uvicorn.logging.DefaultFormatter",
            "fmt": "%(levelprefix)s %(asctime)s | %(funcName)s/%(filename)s;%(lineno)d | %(message)s",
            "use_colors": None,
            "datefmt": "%Y-%m-%d %H:%M:%S",
        }
    },
    "handlers": {
        "default": {
            "formatter": "default",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stderr",
        },
        "access": {
            "formatter": "access",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",
        },
        "app" : {
            "formatter": "app",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",
        }
    },
    "loggers": {
        "uvicorn": {"handlers": ["default"], "level": "INFO", "propagate": False},
        "uvicorn.error": {"level": "INFO"},
        "uvicorn.access": {"handlers": ["access"], "level": "INFO", "propagate": False},
        "app" : {"handlers": ["app"], "level": "INFO", "propagate": False},
    },
}

class Log:
    def __init__(self) -> None:
        log_conf.dictConfig(LOGGING_CONFIG)
        self.logger = logging.getLogger("app")

    @classmethod
    def getLogger(cls):
        return cls().logger
