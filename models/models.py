from sqlalchemy import ForeignKey, String
from typing import Annotated
from database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship


intpk = Annotated[int, mapped_column(primary_key=True)]
str_null = Annotated[str, mapped_column(String(200), nullable=False)]
int_null = Annotated[int, mapped_column(nullable=False)]


class Hotels(Base):
    __tablename__ = 'hotels'

    id: Mapped[intpk]
    name: Mapped[str_null]




class Room_categories(Base):
    __tablename__ = 'room_categories'
    id: Mapped[intpk]
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    amount_room: Mapped[int_null]
    amount_seats: Mapped[int_null]
    price: Mapped[float]

    room: Mapped[list['Rooms']] = relationship(
        back_populates='room_category'
    )


class Rooms(Base):
    __tablename__ = 'rooms'
    id: Mapped[intpk]
    number: Mapped[int_null]
    category_id: Mapped[int] = mapped_column(ForeignKey('room_categories.id'))
    room_category: Mapped['Room_categories'] = relationship(
        back_populates='room'
    )


class Clients(Base):
    __tablename__ = 'clients'
    id: Mapped[intpk]
    first_name: Mapped[str_null]
    last_name: Mapped[str_null]
    email: Mapped[str_null]
    passport_seria: Mapped[str_null]
    passport_number: Mapped[str_null]



class Employyes(Base):
    __tablename__ = 'employyes'
    id: Mapped[intpk]
    first_name: Mapped[str_null]
    last_name: Mapped[str_null]
    title_id: Mapped[int] = mapped_column(ForeignKey('positions.id'))
    position: Mapped["Positions"] = relationship(
        back_populates='employyes'
    )

class Positions(Base):
    __tablename__ = 'positions'
    id: Mapped[intpk]
    title: Mapped[str_null]
    employyes: Mapped[list["Employyes"]] = relationship(
        back_populates='position'
    )


class Reservations(Base):
    __tablename__ = 'reservations'
    id: Mapped[intpk]
    client_id: Mapped[int] = mapped_column(ForeignKey('clients.id'))
    hotel_id: Mapped[int] = mapped_column(ForeignKey('hotels.id'))
    room_id: Mapped[int] = mapped_column(ForeignKey('rooms_id'))
    start_date: Mapped[int]
    end_date: Mapped[int]














