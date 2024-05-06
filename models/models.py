from sqlalchemy import ForeignKey
from typing import Annotated
from database import Base
from sqlalchemy.orm import Mapped, mapped_column


intpk = Annotated[int, mapped_column(primary_key=True)]
str_null = Annotated[str, mapped_column(nullable=False)]
int_null = Annotated[int, mapped_column(nullable=False)]

"""hotels = Table(
    'hotels',
    Base.metadata,
    Column('id', Integer, primary_key=True),
    Column('name', VARCHAR(30), nullable=False),
)"""

class Hotels(Base):
    __tablename__ = 'hotels'

    id: Mapped[intpk]
    name: Mapped[str_null]



"""branches = Table(
    'branches',
    Base.metadata,
    Column('id', Integer, primary_key=True),
    Column('city', VARCHAR(30), nullable=False),
)"""
class Branches(Base):
    __tablename__ = 'branches'
    id: Mapped[intpk]
    city: Mapped[str_null]


"""rooms = Table(
    'rooms',
    Base.metadata,
    Column('id', Integer, primary_key=True),
    Column('number', Integer, nullable=False),
    Column('city_id', Integer, ForeignKey('branches.id'), nullable=False),
    Column('hotel_id', Integer, ForeignKey('hotels.id'), nullable=False),
    Column('is_reserved', BOOLEAN, nullable=False),
    Column('reserved_period', TIMESTAMP, nullable=False) #вот тут я не понял как связать с таблицы клиента
                                                                    #со столбцом end_time таблицы clients

)
"""
class Room_categories(Base):
    __tablename__ = 'room_categories'
    id: Mapped[intpk]
    category: Mapped[str_null]
    amount_room: Mapped[int_null]
    amount_seats: Mapped[int_null]
    price: Mapped[float]


class Rooms(Base):
    __tablename__ = 'rooms'
    id: Mapped[intpk]
    number: Mapped[int_null]
    id_category: Mapped[int]= mapped_column(ForeignKey('room_categories.id'))
    hotel_id: Mapped[int] = mapped_column(ForeignKey('hotels.id'))
    city_id: Mapped[int] = mapped_column(ForeignKey('branches.id'))


"""clients = Table(
    'clients',
    Base.metadata,
    Column('id_client', Integer, primary_key=True),
    Column('first_name', VARCHAR(30), nullable=False),
    Column('last_name', VARCHAR(30), nullable=False),
    Column('email', VARCHAR(20), nullable=False),
    Column('start_date', TIMESTAMP, nullable=False),
    Column('end_date', TIMESTAMP, nullable=False),
    Column('room_id', Integer, ForeignKey('rooms.id'), nullable=False),
    Column('hotel_id', Integer, ForeignKey("hotels.id")),
    Column('city_id', Integer, ForeignKey("branches.id")),
)
"""

class Clients(Base):
    __tablename__ = 'clients'
    id: Mapped[intpk]
    first_name: Mapped[str_null]
    last_name: Mapped[str_null]
    email: Mapped[str_null]
    passport_serias: Mapped[str_null]
    passport_number: Mapped[str_null]



"""employees = Table(
'employess',
Base.metadata,
Column('id', Integer, primary_key=True),
Column('name', VARCHAR(30), nullable=False),
Column('job_title', VARCHAR(20), nullable=False),
Column('id_branches', Integer, ForeignKey("branches.id")),
Column('id_hotel', Integer, ForeignKey('hotels.id')),
)"""


class Employyes(Base):
    __tablename__ = 'employyes'
    id: Mapped[intpk]
    first_name: Mapped[str_null]
    last_name: Mapped[str_null]
    title_id: Mapped[int] = mapped_column(ForeignKey('positions.id'))

class Positions(Base):
    __tablename__ = 'positions'
    id: Mapped[intpk]
    title: Mapped[str_null]


class Reservations(Base):
    __tablename__ = 'reservations'
    id: Mapped[intpk]
    client_id: Mapped[int] = mapped_column(ForeignKey('clients.id'))
    hotel_id: Mapped[int] = mapped_column(ForeignKey('hotels.id'))
    branches_id: Mapped[int] = mapped_column(ForeignKey('branches.id'))
    rooms_id: Mapped[int] = mapped_column(ForeignKey('rooms_id'))
    start_date:Mapped[int]
    end_date:Mapped[int]














