import sqlite3

def create_student_table(conn):
    conn.execute('''DROP TABLE IF EXISTS STUDENTS''')
    conn.execute('''CREATE TABLE IF NOT EXISTS STUDENTS
                    (STUDENT_ID INT PRIMARY KEY NOT NULL,
                     REG_NO TEXT NOT NULL,
                     NAME TEXT NOT NULL,
                     BRANCH TEXT NOT NULL,
                     SEMESTER INT NOT NULL,
                     CGPA REAL NOT NULL,
                     EMAIL TEXT NOT NULL);''')
    print("Student table created successfully")

def insert_student_data(conn, data):
    conn.execute("INSERT INTO STUDENTS (STUDENT_ID, REG_NO, NAME, BRANCH, SEMESTER, CGPA, EMAIL) \
                  VALUES (?, ?, ?, ?, ?, ?, ?)", data)
    conn.commit()

def search_student_by_regno(conn, regno):
    cursor = conn.execute("SELECT * FROM STUDENTS WHERE REG_NO=?", (regno,))
    student = cursor.fetchone()
    if student:
        print("\nStudent Details:")
        print(f"Student ID: {student[0]}")
        print(f"Registration Number: {student[1]}")
        print(f"Name: {student[2]}")
        print(f"Branch: {student[3]}")
        print(f"Semester: {student[4]}")
        print(f"CGPA: {student[5]}")
        print(f"Email: {student[6]}")
    else:
        print(f"No student found with Registration Number: {regno}")

conn = sqlite3.connect('Lab7.db')

create_student_table(conn)

student_data = [
    (1, '210911052', 'Shashwat Trivedi', 'Information Tech', 1, 3.8, 'shashwat.trivedi@example.com'),
    (2, '210911122', 'Shantanu', 'Information Tech', 2, 3.5, 'shantanu.srivastava@example.com')
]

for data in student_data:
    insert_student_data(conn, data)

search_regno = input("Enter the Registration Number to search for a student: ")

search_student_by_regno(conn, search_regno)

conn.close()
