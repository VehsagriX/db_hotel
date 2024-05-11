from models.models import Hotels, Base, Room_categories, Rooms, Clients, Reservations
from database import session_factory, engine
from sqlalchemy import Integer, and_, func, insert, select, text, update

def create_table(self):
    engine.echo = False
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


class Hotel():
    def insert_hotel(self):
        with session_factory() as session:
            hotel_serena = Hotels(name='Serena Hotel')
            asia_grand = Hotels(name='Asia Grand Hotel')
            hyyatt_hotel = Hotels(name='Hyatt Regency')
            hilton_hotel = Hotels(name='Hilton')
            session.add_all([hotel_serena, asia_grand, hyyatt_hotel, hilton_hotel])
            session.commit()

    def update_hotel(self):
        pass


    def delete_hotel(self):
        pass


class Category:
    def insert_rooms_category(self):
        with session_factory() as session:
            suite = Room_categories(name='Сьют',amount_room=4, amount_seats=6, price=800.00)
            apartament = Room_categories(name='Апартаменты',amount_room=3, amount_seats=4, price=600.00)
            luxury = Room_categories(name='Люкс',amount_room=2, amount_seats=4, price=500.00)
            studio = Room_categories(name='Студия',amount_room=1, amount_seats=2, price=200.00)
            session.add_all([suite, apartament, luxury, studio])
    def update_category(self):
        pass

    def delete_category(self):
        pass


class Room:
    pass


class Client:
    def insert_client(self):
        with session_factory() as session:
            luke_skywalker = Clients(first_name='Luke', last_name='SkyWalker', email='luke_skywalker@gmail.com',
                                     passport_seria='12345', passport_namber='6789')
            darth_vader = Clients(first_name='Darth', last_name='Vader', email='darth_vader@gmail.com',
                                     passport_seria='13545', passport_namber='7790')
            han_solo = Clients(first_name='Han', last_name='Solo', email='han_solo@gmail.com',
                                  passport_seria='225145', passport_namber='8799')
            session.add_all([luke_skywalker, darth_vader, han_solo])
    def update_client(self):
        pass


    def delete_client(self):
        pass
