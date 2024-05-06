from models.models import Hotels, Base
from database import session_factory, engine


def create_table():
    Base.metadata.create_all(engine)



def insert_data():
    with session_factory() as session:
        hotel = Hotels(name='Hayte')
        session.add(hotel)
        session.commit()



