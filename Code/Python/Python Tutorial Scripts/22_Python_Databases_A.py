import sqlite3

connection = sqlite3.connect('mydata.db')

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS persons (
    first_name TEXT,
    last_name TEXT,
    age INTEGER                                     
)               
""")

cursor.execute("""
INSERT INTO persons VALUES
('Paul', 'Smith', 24),
('Mark', 'Johnson', 42),
('Anna', 'Smith', 34)                              
""")

cursor.execute("""
SELECT * FROM persons
WHERE last_name = 'Smith'
""")

rows = cursor.fetchall()
print(rows)

connection.commit()

connection.close()