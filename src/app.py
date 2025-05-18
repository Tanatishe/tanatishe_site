from fastapi import FastAPI

from src.routing.router import router
def get_app()->FastAPI:

    app=FastAPI()

    app.include_router(router,prefix='')
    return app