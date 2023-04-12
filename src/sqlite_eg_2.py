import sqlite3

# Connect to or create SQLite database
conn = sqlite3.connect('members.db')
cur = conn.cursor()

# Load SQL script from file
with open('D:\\demo\\test.sql') as file:
    sql_script = file.read()

# Execute script
cur.executescript(sql_script)

# Display data
member_data = cur.execute("SELECT * FROM members ORDER BY ln")
for row in member_data:
    print(row)

# Display data using cursor
# cur.execute("SELECT * FROM members ORDER BY ln")
# for member in cur:
#     print(member)

# It's closing time
cur.close()
conn.close()