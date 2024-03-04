import sqlite3

def create_users_table(conn):
    conn.execute('''CREATE TABLE IF NOT EXISTS USERS
                    (USERNAME TEXT PRIMARY KEY NOT NULL,
                     PASSWORD TEXT NOT NULL,
                     EMAIL TEXT NOT NULL);''')
    print("Users table created successfully")

def register_user(conn, username, password, email):
    try:
        conn.execute("INSERT INTO USERS (USERNAME, PASSWORD, EMAIL) VALUES (?, ?, ?)", (username, password, email))
        conn.commit()
        print("Registration successful!")
    except sqlite3.IntegrityError:
        print("Username already exists. Please choose a different username.")

def is_valid_password(password):
    return len(password) >= 8

conn = sqlite3.connect('Lab7.db')

create_users_table(conn)

username = input("Enter your username: ")
password = input("Enter your password: ")

while not is_valid_password(password):
    print("Invalid password. Password should have at least 8 characters.")
    password = input("Enter a valid password: ")

email = input("Enter your email address: ")

register_user(conn, username, password, email)

conn.close()
