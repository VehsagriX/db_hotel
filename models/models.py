from sqlalchemy import MetaData, Table, Column, Integer, VARCHAR, ForeignKey, TIMESTAMP, BOOLEAN



metadata = MetaData()

hotels = Table(
    'hotels',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', VARCHAR(30), nullable=False),
)

branches = Table(
    'branches',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('city', VARCHAR(30), nullable=False),
)

rooms = Table(
    'rooms',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('number', Integer, nullable=False),
    Column('city_id', Integer, ForeignKey('branches.id'), nullable=False),
    Column('hotel_id', Integer, ForeignKey('hotels.id'), nullable=False),
    Column('is_reserved', BOOLEAN, nullable=False),
    Column('reserved_period', TIMESTAMP, nullable=False) #вот тут я не понял как связать с таблицы клиента
                                                                    #со столбцом end_time таблицы clients

)

clients = Table(
    'clients',
    metadata,
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


employees = Table(
    'employess',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', VARCHAR(30), nullable=False),
    Column('job_title', VARCHAR(20), nullable=False),
    Column('id_branches', Integer, ForeignKey("branches.id")),
    Column('id_hotel', Integer, ForeignKey('hotels.id')),
)

