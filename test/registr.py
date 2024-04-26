import sqlite3

def registrat(username, password, name, address, tguse, sex, age):
    age = int(age)
    print(age)
    conn = sqlite3.connect("adad.sqlite")
    cur = conn.cursor()

    cur.execute(
        '''INSERT INTO Users(name, age, sex, address, login, password, tguse) VALUES(?, ?, ?, ?, ?, ?, ?)''',
        (name, age, sex, address, username, password, tguse)
    )
    conn.commit()  # Commit the transaction
    conn.close()

registrat("asda", "asdas", "asasd", "asasd", "@aaaaa", "suka", 20)