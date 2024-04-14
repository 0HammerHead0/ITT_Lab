import sqlite3

def viewAll(conn):
    cur = conn.execute("SELECT * FROM travel")
    return cur

conn = sqlite3.connect('ishan.db')
cur = viewAll(conn)

for i in cur:
    print(f"{i[0]:<10} | {i[1]:<10} | {i[2]:<10}")
    print("_"*35)

def average(conn):
    cur=conn.execute("SELECT AVG(COST) FROM TRAVEL")
    return cur
cur = average(conn)
