from models import engine, Transport, Sender, Courier, Recipient, Orders
from datetime import date, time
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

for i in range(1, 3):
    courier = Courier(surname='Ivanov'+str(i),
                      name='Ivan'+str(i),
                      mid_name='Ivanovich'+str(i),
                      passport_num=int(str(i) * 10),
                      birth_date=date(2000, 1, 1),
                      employment_date=date(2000, 1, 1),
                      day_begin=time(10, 0),
                      day_end=time(20, 0),
                      city='Moscow',
                      street='Bolshaya',
                      house=str(i),
                      flat=i,
                      telephone='8' + str(i) * 10)
    session.add(courier)
    session.commit()

for i in range(3, 5):
    recipient = Recipient(recipient_id=i - 2,
                          surname='Sokolov' + str(i),
                          name='Sokol' + str(i),
                          mid_name='Sokolovich' + str(i),
                          birth_date=date(2000, 1, 1),
                          indexx=i,
                          city='Kaliningrad',
                          street='Malaya',
                          house=str(i),
                          flat=i,
                          telephone='8' + str(i) * 10)
    session.add(recipient)
    session.commit()

for i in range(1, 3):
    order = Orders(order_id=i,
                   sender=1,
                   recipient=i,
                   order_date=date(2024, 1, 1),
                   delivery_date=date(2024, 2, 1),
                   shipping_cost=i * 1111.11,
                   courier=i,
                   car=1)
    session.add(order)
    session.commit()

session.close()