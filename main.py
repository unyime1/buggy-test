from fastapi import FastAPI, status
from db import Tournament
from db import create_start_app_handler


def get_application():
    app = FastAPI()
    app.add_event_handler("startup", create_start_app_handler(app))
    return app


app = get_application()


@app.get("/",
    name="point1",
    status_code=status.HTTP_200_OK
)
async def home():
    return {
        "title":"Hello world"
    }


@app.get(
    "/save/",
    name="point2",
    status_code=status.HTTP_200_OK
)
async def save_data():
    await Tournament.create(
        name="test2"
    )
    return {
        "status":"created"
    }
