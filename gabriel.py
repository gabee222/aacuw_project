import sqlite3
import matplotlib.pyplot as plt
import csv
import sys

con = sqlite3.connect("files/seahawks.db")

cur = con.cursor()

cur.execute("SELECT * FROM Seahawks")

rows = cur.fetchall()

con.commit()
con.close()

print(rows)

