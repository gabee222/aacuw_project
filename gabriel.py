import sqlite3
import matplotlib.pyplot as plt


con = sqlite3.connect("files/seahawks.db")

cur = con.cursor()

cur.execute("SELECT * FROM Seahawks")

rows = cur.fetchall()

con.commit()
con.close()

print(rows)

