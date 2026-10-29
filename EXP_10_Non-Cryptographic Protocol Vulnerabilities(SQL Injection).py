import sqlite3

con = sqlite3.connect(":memory:")
cur = con.cursor()

cur.execute("CREATE TABLE users (username TEXT, password TEXT)")
cur.execute("INSERT INTO users VALUES ('admin', '1234')")

username = input("Enter username: ")
password = input("Enter password: ")

query = "SELECT * FROM users WHERE username=? AND password=?"
cur.execute(query, (username, password))

if cur.fetchone():
    print("Login successful")
else:
    print("Login failed")

con.close()