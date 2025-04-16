from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends
from typing import List
from typing import Annotated
from schemas import TableSchema
from models import Table
from models import db
from database import get_async_session  # Нужно создать эту функцию
from sqlalchemy import select

# database = ... 

router = APIRouter(
    prefix="/tables",
    tags=["Столы"],
)


@router.get('/', response_model=List[TableSchema])
async def get_tables(session: AsyncSession = Depends(get_async_session)):
    print("Получаем таблицы...")  # Для отладки
    result = await session.execute(select(Table))
    tables = result.scalars().all()
    print(f"Найдено {len(tables)} таблиц")  # Для отладки
    return tables


# @router.post('/tables')
# async def create_table(
#     session: AsyncSession,
# ) -> TableSchema:
#     return await db.session.q