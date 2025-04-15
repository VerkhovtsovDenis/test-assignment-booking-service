"""seed_initial_data

Revision ID: bebd59534448
Revises: d9e9116df3b9
Create Date: 2025-04-15 20:24:55.602562

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import json
from datetime import datetime
from pathlib import Path


# revision identifiers, used by Alembic.
revision: str = 'bebd59534448'
down_revision: Union[str, None] = 'd9e9116df3b9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

# Указываем путь к JSON-файлам
BASE_DIR = Path(__file__).resolve().parent.parent.parent

def upgrade():
    # Загружаем данные из tables.json
    with open(BASE_DIR / 'fixtures/tables.json', 'r', encoding='utf-8') as f:
        tables_data = json.load(f)
    
    # Вставляем столики (используем правильное имя таблицы)
    for table in tables_data:
        op.execute(
            sa.text(
                """
                INSERT INTO "table" (id, name, seats, location)
                VALUES (:id, :name, :seats, :location)
                """
            ).bindparams(
                id=table['id'],
                name=table['name'],
                seats=table['seats'],
                location=table['location']
            )
        )

    # Загружаем данные из reservations.json
    with open(BASE_DIR / 'fixtures/reservations.json', 'r', encoding='utf-8') as f:
        reservations_data = json.load(f)
    
    # Вставляем брони
    for reservation in reservations_data:
        op.execute(
            sa.text(
                """
                INSERT INTO reservation (id, customer_name, table_id, reservation_time, duration_minutes)
                VALUES (:id, :customer_name, :table_id, :reservation_time, :duration_minutes)
                """
            ).bindparams(
                id=reservation['id'],
                customer_name=reservation['customer_name'],
                table_id=reservation['table_id'],
                reservation_time=datetime.fromisoformat(reservation['reservation_time']),
                duration_minutes=reservation['duration_minutes']
            )
        )

def downgrade():
    op.execute(sa.text('DELETE FROM reservation'))
    op.execute(sa.text('DELETE FROM "table"'))
