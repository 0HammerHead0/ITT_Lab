import sqlite3
data =[
    {
        "dest" : "Mumbai",
        "cost" : 2000,
        "budget" : 5000.0
    },
    {
        "dest" : "Unnao",
        "cost" : 200,
        "budget" : 500.0
    },
    {
        "dest" : "Kanpur",
        "cost" : 300,
        "budget" : 200.0
    },
    {
        "dest" : "Lucknow",
        "cost" : 100,
        "budget" : 5.0
    },
    {
        "dest" : "Varanasi",
        "cost" : 20000,
        "budget" : 50000.0
    },
]

def insert(conn,dest,cost,budget):
    if(type(dest)==str and type(cost)==int and type(budget)==float):
        conn.execute("INSERT INTO travel VALUES(?, ?,?)",(dest,cost,budget))
        conn.commit()
    else:
        print("Can't")

conn = sqlite3.connect('ishan.db')
for i in data:
    insert(conn,i['dest'],i['cost'],i['budget'])
insert(conn,101,"hello",101)
conn.close()