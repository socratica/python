import sqlite3

# Connect to a non-existant database
#conn = sqlite3.connect('datadiet.db')
# cur = conn.cursor()

conn = sqlite3.connect('d:\\git_repositories\\python\\data_diet.db')
print(dir(conn))
