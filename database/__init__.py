from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from config import get_db_url

DATABASE_URL = get_db_url()

engine = create_async_engine(DATABASE_URL)
async_session = sessionmaker(engine, class_=AsyncSession,
                             expire_on_commit=False)


async def get_async_session() -> AsyncSession:
    async with async_session() as session:
        yield session
