import time
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
from src.routing.router import router
import os
import logging
import threading
logger = logging.getLogger(__name__)

def get_app() -> FastAPI:
    app = FastAPI(
        title="Tanatishe.ru",
        description="Темное логово Рипера",
        version="1.0.0"
    )

    threading.Thread(target=background_task,daemon=True).start()

    # Монтируем статические файлы
    app.mount("/static", StaticFiles(directory="src/static"), name="static")

    # Обработчики ошибок
    @app.exception_handler(404)
    async def not_found_handler(request: Request, exc):
        return JSONResponse(
            status_code=404,
            content={"detail": "Not Found"}
        )

    @app.exception_handler(500)
    async def server_error_handler(request: Request, exc):
        return JSONResponse(
            status_code=500,
            content={"detail": "Internal Server Error"}
        )

    app.include_router(router, prefix='')
    return app


def background_task():
    while True:
        logger.info("Background task is running")
        time.sleep(10)