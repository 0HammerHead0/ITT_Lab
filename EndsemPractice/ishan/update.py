import sqlite3

def update(conn):
    conn.execute("UPDATE travel \
                 SET BUDGET=COST+1000\
                 WHERE BUDGET<COST\
                 ")
conn = sqlite3.connect('ishan.db')
update(conn)
conn.commit()
conn.close()