import sqlite3

# Connect to a (new) database
conn = sqlite3.connect('D:\\demo\\alpha.db')

# Create a cursor
cur = conn.cursor()

# Create a "people" table
cur.execute('''CREATE TABLE IF NOT EXISTS people
               (first_name TEXT, last_name TEXT)''')
conn.commit()

# Test data
names_list = [
    ("Roderick", "Watson"),
    ("Roger", "Hom"),
    ("Petri", "Halonen"),
    ("Jussi", ""),
    ("James", "McCann")
]

# Insert data into database
cur.executemany('INSERT INTO people (first_name, last_name) VALUES (?, ?)', names_list)
conn.commit()

# Close db objects
cur.close()
conn.close()