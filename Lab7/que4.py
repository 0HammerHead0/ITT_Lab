import sqlite3
conn = sqlite3.connect('Lab7.db')
def update_cgpa_by_id(conn, student_id, new_cgpa):
    conn.execute("UPDATE STUDENTS SET CGPA = ? WHERE STUDENT_ID = ?", (new_cgpa, student_id))
    conn.commit()
    print("CGPA updated successfully!")
print("\nCurrent Student Records:")
[print(row) for row in conn.execute("SELECT * FROM STUDENTS")]

student_id = int(input("\nEnter the Student ID to update CGPA: "))
new_cgpa = float(input("Enter the new CGPA: "))

update_cgpa_by_id(conn, student_id, new_cgpa)

print("\nUpdated Student Records:")
[print(row) for row in conn.execute("SELECT * FROM STUDENTS")]

conn.close()
