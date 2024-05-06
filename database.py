from sqlalchemy.orm import Session, sessionmaker, DeclarativeBase
from sqlalchemy import create_engine
from config import settings

engine = create_engine(
    url=settings.DATABASE_URL,
    echo=True,
)


session_factory = sessionmaker(engine)

class Base(DeclarativeBase):
    pass