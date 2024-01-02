import sqlite3

with sqlite3.connect('db.sqlite') as conn:
    cur = conn.cursor()
    # ISO-8601
    cur.execute("CREATE TABLE files(filename TEXT PRIMARY KEY, time_created)")
    conn.commit()
