import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.execute('DROP TABLE IF EXISTS tasks;')
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO tasks (task_name, task_priority, task_date, task_hour) VALUES (?, ?, ?, ?)",
            )

connection.commit()
connection.close()
