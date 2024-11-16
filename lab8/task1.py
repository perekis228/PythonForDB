import sqlite3

conn = sqlite3.connect('task1_db.db')
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS transport (
    car_id INTEGER PRIMARY KEY,
    brand VARCHAR(50),
    reg_date DATE,
    colour VARCHAR(50)
)''')

cur.execute('''CREATE TABLE IF NOT EXISTS sender (
    sender_id INTEGER PRIMARY KEY,
    surname VARCHAR(50),
    name VARCHAR(50),
    mid_name VARCHAR(50),
    birth_date VARCHAR(50),
    indexx INTEGER,
    city VARCHAR(50),
    street VARCHAR(50),
    house VARCHAR(50),
    flat INTEGER,
    telephone VARCHAR(50)
)''')

cur.execute("INSERT INTO transport VALUES (1, 'Nissan', '2020-10-12', 'white')")
cur.execute("INSERT INTO sender VALUES (1, 'Antonov', 'Anton', 'Antonovich', '2000-11-11', 1, 'Moscow', 'Komsomolskaya', '14/1', 5, '88005553535')")
cur.execute("UPDATE transport SET colour='red' WHERE car_id=1")

conn.commit()
conn.close()