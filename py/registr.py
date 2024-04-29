import sqlite3

def registrat(username, password, name, address, tguse, sex, age):
    age = int(age)
    conn = sqlite3.connect("db/db.sqlite")
    cur = conn.cursor()

    cur.execute(
        '''INSERT INTO Users(name, age, sex, address, login, password, tguse) VALUES(?, ?, ?, ?, ?, ?, ?)''',
        (name, age, sex, address, username, password, tguse)
    )
    conn.commit()
    conn.close()
