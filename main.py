from fastapi import FastAPI
from config import get_db_url
import uvicorn

from routers import routers

app = FastAPI(
    title='Booking API',
    description=(
        "Booking API - FastApi приложение для управления бронированием столиков "
    )
)

[app.include_router(router) for router in routers]

if __name__ == "__main__":
    uvicorn.run(app)
