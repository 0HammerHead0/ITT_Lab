import sqlite3

def create_table(conn):
    conn.execute('''
                CREATE TABLE IF NOT EXISTS travel(
                    DESTINATION_NAME TEXT NOT NULL,
                    COST INT NOT NULL,
                    BUDGET REAL NOT NULL
                )
                 ''')

conn = sqlite3.connect('./ishan.db')
create_table(conn)
conn.commit()
conn.close()