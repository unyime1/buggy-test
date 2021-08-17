from fastapi import FastAPI
from tortoise.models import Model
from tortoise import fields
from tortoise.contrib.fastapi import register_tortoise
from typing import Callable


class Tournament(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)


async def init_db(app: FastAPI):
    register_tortoise(
        app,
        db_url='postgres://admin:admin@localhost:5432/postgres_test',
        modules={"models": ["db"]},
        generate_schemas=True,
        add_exception_handlers=True,
    ) 


def create_start_app_handler(app: FastAPI) -> Callable:
    async def start_app() -> None:
        await init_db(app)
    return start_app
