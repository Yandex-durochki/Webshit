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