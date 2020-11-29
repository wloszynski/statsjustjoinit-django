import time
import sqlite3


conn = sqlite3.connect('database_for_d.sqlite')
cur = conn.cursor()


cur.execute('SELECT name from language')
rows = cur.fetchall()

for row in rows:
    print(row[0])
