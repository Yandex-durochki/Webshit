import sqlite3


def compare_data_with(username):
    conn = sqlite3.connect("db/db.sqlite")
    cur = conn.cursor()

    cur.execute(f"SELECT login FROM Users")
    rows = cur.fetchall()

    data_found = False
    for row in rows:
        if str(row[0]) == username:
            data_found = True
            return data_found

    if not data_found:
        return data_found

    conn.close()


def check_password(username, password):
    conn = sqlite3.connect('db.sqlite')
    cursor = conn.cursor()
    data_true = None
    error_type = None
    cursor.execute('SELECT password FROM users WHERE login = ?', (username,))
    result = cursor.fetchone()

    if result:
        if result[0] == password:
            data_true = True
            return data_true
        else:
            data_true = False
            error_type = "Пароль не совпадает"
            return data_true, error_type
    else:
        error_type = "Пользователь с таким логином не найден"
        data_true = False
        return data_true, error_type

    conn.close()
