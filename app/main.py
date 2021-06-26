import logging
from logging.config import dictConfig

import uvicorn
from fastapi import FastAPI

from app.config.logging import LOGGING_CONFIG
from app.routers import router as calc_router
from front_part.routers import router as front_router

logger = logging.getLogger(__name__)


class Application:
    """Класс, инициализирующий сервис."""

    def __init__(self):
        logger.debug('Initialize application.')
        self.server: FastAPI = FastAPI(
            title='Calculator',
            description='Simple calculator',
        )

        self._config_logging()
        self._config_routers()

    @staticmethod
    def _config_logging():
        """Настраиваем логирование."""
        dictConfig(LOGGING_CONFIG)
        logger.debug('Configure logging')

    def _config_routers(self):
        """Настраиваем роуты приложения."""
        logger.debug('Configure routes.')
        self.server.include_router(calc_router)
        self.server.include_router(front_router)


app = Application()


if __name__ == '__main__':
    uvicorn.run(app.server, port=8001, host='0.0.0.0')  # noqa: S104

