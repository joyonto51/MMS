"""
importent links:
http://sebastianraschka.com/Articles/2014_sqlite_in_python_tutorial.html
http://www.pythoncentral.io/introduction-to-sqlite-in-python/
"""

import sqlite3

# Create a database in RAM
conn = sqlite3.connect('testdb.sqlite')

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS student(
    	id INTEGER PRIMARY KEY, 
    	roll INTEGER, 
    	name TEXT,
        phone TEXT)
''')
Roll=int(input("Roll:"))
Name=input("Name:")
Phone=int(input("Phone:"))
cursor.execute('''
    INSERT INTO student( roll, name, phone )
    VALUES ( :roll,:name,:phone )''',{'roll':Roll,'name': Name ,'phone': Phone}
               )


cursor.execute('''
    SELECT roll, name, phone
    FROM student
''')

all_rows = cursor.fetchall()

for row in all_rows:
    print('{0}: {1}, {2}'.format(row[0], row[1], row[2]))


conn.commit()

conn.close()
