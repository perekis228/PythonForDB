from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Date, Time, ForeignKey, Float
from sqlalchemy.orm import declarative_base, relationship

engine = create_engine('sqlite:///task1_db.db')
Base = declarative_base()

class Transport(Base):
    __tablename__ = 'transport'

    car_id = Column(Integer, primary_key=True)
    brand = Column(String)
    reg_date = Column(Date)
    colour = Column(String)

class Sender(Base):
    __tablename__ = 'sender'

    sender_id = Column(Integer, primary_key=True)
    surname = Column(String)
    name = Column(String)
    mid_name = Column(String)
    birth_date = Column(Date)
    indexx = Column(Integer)
    city = Column(String)
    street = Column(String)
    house = Column(String)
    flat = Column(Integer)
    telephone = Column(String)

class Courier(Base):
    __tablename__ = 'courier'

    courier_id = Column(Integer, primary_key=True)
    surname = Column(String)
    name = Column(String)
    mid_name = Column(String)
    passport_num = Column(Integer)
    birth_date = Column(Date)
    employment_date = Column(Date)
    day_begin = Column(Time)
    day_end = Column(Time)
    city = Column(String)
    street = Column(String)
    house = Column(String)
    flat = Column(Integer)
    telephone = Column(String)

class Recipient(Base):
    __tablename__ = 'recipient'

    recipient_id = Column(Integer, primary_key=True)
    surname = Column(String)
    name = Column(String)
    mid_name = Column(String)
    birth_date = Column(Date)
    indexx = Column(Integer)
    city = Column(String)
    street = Column(String)
    house = Column(String)
    flat = Column(Integer)
    telephone = Column(String)

class Orders(Base):
    __tablename__ = 'orders'

    order_id = Column(Integer, primary_key=True)
    sender = Column(Integer, ForeignKey('sender.sender_id'))
    recipient = Column(Integer, ForeignKey('recipient.recipient_id'))
    order_date = Column(Date)
    delivery_date = Column(Date)
    shipping_cost = Column(Float)
    courier = Column(Integer, ForeignKey('courier.courier_id'))
    car = Column(Integer, ForeignKey('transport.car_id'))

    transport_rel = relationship('Transport', backref='transport_order_rel')
    sender_rel = relationship('Sender', backref='sender_order_rel')
    courier_rel = relationship('Courier', backref='courier_order_rel')
    recipient_rel = relationship('Recipient', backref='recipient_order_rel')

Base.metadata.create_all(engine)