from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy.orm import Mapped
from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from .Base import Base
from .Table import Table


class Reservation(Base):
    __tablename__ = "reservation"

    id: Mapped[int] = mapped_column(primary_key=True)   
    customer_name: Mapped[str] = mapped_column(String(60))
    table_id: Mapped[int] = mapped_column(ForeignKey("table.id"))
    reservation_time: Mapped[DateTime] = mapped_column(DateTime)
    duration_minutes: Mapped[int] = mapped_column()

    table: Mapped["Table"] = relationship('Table',
                                          back_populates="reservations")

    def __repr__(self) -> str:
        return f"Reservation(id={self.id!r}, "\
               f"customer_name={self.customer_name!r}, " \
               f"table_id={self.table_id!r}, " \
               f"reservation_time={self.reservation_time!r}, " \
               f"duration_minutes={self.duration_minutes!r})"
