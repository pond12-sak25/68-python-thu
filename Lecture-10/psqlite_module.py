import sqlite3

conn = sqlite3.connect('mydatabase.db')

cursor = conn.cursor()
cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            city TEXT NOT NULL
            )
''')
cursor.execute("INSERT INTO users (name, age, ) VALUES (?, ?, ?)"('Alice', 30,))
cursor.execute("INSERT INTO users (name, age, ) VALUES (?, ?, ?)"('Bob', 25, ))
cursor.execute("INSERT INTO users (name, age, ) VALUES (?, ?, ?)"('Charlie', 35, ))

conn.commit()

cursor.execute('SELECT * FROM users Where age > 28')
rows = cursor.fetchall()

print("Users older than 28:")
for row in rows:
    print(f'ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, City: {row[3]}')
conn.close()