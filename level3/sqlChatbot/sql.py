# Import module 
import sqlite3 
  
# Connecting to sqlite 
conn = sqlite3.connect('test.db') 
  
# Creating a cursor object using the  
# cursor() method 
cursor = conn.cursor() 

# Drop table if it exists (to avoid conflicts)
cursor.execute('''DROP TABLE IF EXISTS STUDENT''')

# Creating table with better structure
table = """CREATE TABLE STUDENT(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NAME VARCHAR(255), 
    CLASS VARCHAR(255), 
    SECTION VARCHAR(255),
    MARKS INTEGER
);"""
cursor.execute(table) 
  
# Insert 10 diverse student records for testing
students_data = [
    ('Alice Johnson', 'Data Science', 'A', 95),
    ('Bob Smith', 'Data Science', 'B', 78),
    ('Charlie Brown', 'Web Development', 'A', 89),
    ('Diana Prince', 'DevOps', 'C', 92),
    ('Ethan Hunt', 'Data Science', 'A', 85),
    ('Fiona Chen', 'Machine Learning', 'B', 96),
    ('George Wilson', 'Web Development', 'C', 73),
    ('Hannah Davis', 'DevOps', 'A', 88),
    ('Ivan Petrov', 'Machine Learning', 'B', 82),
    ('Julia Roberts', 'Data Science', 'C', 91)
]

# Insert all student records
for student in students_data:
    cursor.execute('''INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS) VALUES (?, ?, ?, ?)''', student)

print("=== STUDENT DATABASE CREATED ===")
print(f"Total records inserted: {len(students_data)}")
print("\n=== ALL STUDENT RECORDS ===")

# Display all data
data = cursor.execute('''SELECT * FROM STUDENT''') 
for row in data: 
    print(f"ID: {row[0]}, Name: {row[1]}, Class: {row[2]}, Section: {row[3]}, Marks: {row[4]}")

# Commit the changes to save data permanently
conn.commit()
print("\n✅ Database created and data saved successfully!")
    
# Closing the connection 
conn.close()