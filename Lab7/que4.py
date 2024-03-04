import sqlite3
conn = sqlite3.connect('test.db')
def update_cgpa_by_id(conn, student_id, new_cgpa):
    conn.execute("UPDATE STUDENTS SET CGPA = ? WHERE STUDENT_ID = ?", (new_cgpa, student_id))
    conn.commit()
    print("CGPA updated successfully!")
print("\nCurrent Student Records:")
[print(row) for row in conn.execute("SELECT * FROM STUDENTS")]

# Ask the user for the student ID and the new CGPA
student_id = int(input("\nEnter the Student ID to update CGPA: "))
new_cgpa = float(input("Enter the new CGPA: "))

# Update CGPA based on student ID
update_cgpa_by_id(conn, student_id, new_cgpa)

# Display updated student records
print("\nUpdated Student Records:")
[print(row) for row in conn.execute("SELECT * FROM STUDENTS")]

# Close the database connection
conn.close()
