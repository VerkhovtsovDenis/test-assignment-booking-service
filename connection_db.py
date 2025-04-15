from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from models import Base, Table, Reservation

engine = create_engine(r"postgresql://localhost/booking-service")


# # URL базы данных PostgreSQL
# database_url = 'postgresql://postgres:1234@localhost/db'
# engine = create_engine(database_url)


# Base.metadata.create_all(engine)

# Session = sessionmaker(bind=engine)
# session = Session()

# # Пример: Вставка нового пользователя в базу данных
# new_user = User(username='Sandy', email='sandy@gmail.com', password='cool-password')
# session.add(new_user)
# session.commit()