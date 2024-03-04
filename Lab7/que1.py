import sqlite3

def create_student_table(conn):
    conn.execute('''CREATE TABLE IF NOT EXISTS STUDENTS
                    (STUDENT_ID INT PRIMARY KEY NOT NULL,
                     REG_NO TEXT NOT NULL,
                     BRANCH TEXT NOT NULL,
                     SEMESTER INT NOT NULL,
                     SECTION TEXT NOT NULL,
                     CGPA REAL NOT NULL,
                     EMAIL TEXT NOT NULL);''')
    print("Student table created successfully")

def insert_student_data(conn, data):
    conn.execute("INSERT INTO STUDENTS (STUDENT_ID, REG_NO, BRANCH, SEMESTER, SECTION, CGPA, EMAIL) \
                  VALUES (?, ?, ?, ?, ?, ?, ?)", data)
    conn.commit()

def display_sorted_records(conn, sort_key):
    cursor = conn.execute(f"SELECT * FROM STUDENTS ORDER BY {sort_key}")
    print(f"\n{'STUDENT_ID':<12} {'REG_NO':<15} {'BRANCH':<15} {'SEMESTER':<10} {'SECTION':<10} {'CGPA':<10} {'EMAIL'}")
    print("-" * 90)
    for row in cursor:
        print(f"{row[0]:<12} {row[1]:<15} {row[2]:<15} {row[3]:<10} {row[4]:<10} {row[5]:<10} {row[6]}")

conn = sqlite3.connect('Lab7.db')

create_student_table(conn)

student_data = [
    (1, '2022001', 'Computer Science', 1, 'A', 3.8, 'student1@example.com'),
    (2, '2022002', 'Electrical Engineering', 2, 'B', 3.5, 'student2@example.com'),
]

for data in student_data:
    insert_student_data(conn, data)

display_sorted_records(conn, 'CGPA')

conn.close()
