from fastapi import FastAPI
from config import get_db_url
import uvicorn
from typing import Union

from routers import routers

app = FastAPI(
    title='Booking API',
    description=(
        "Booking API - FastApi приложение для управления бронированием столиков "
    )
)

[app.include_router(router) for router in routers]


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


if __name__ == "__main__":
    uvicorn.run(app)
