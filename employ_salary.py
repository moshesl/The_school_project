import csv
import sqlite3

con = sqlite3.connect("crazy_school2.db")
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS SCHOOL_1 ('מדעי_מחשב' ,'שמות', 'ת_ז', 'מתמטיקה', 'אנגלית', 'יהדות');") # use your column names here

with open('בית ספר - גיליון1.csv','r') as fin: # `with` statement available in 2.5+
    # csv.DictReader uses first line in file for column headings by default
    dr = csv.DictReader(fin) # comma is default delimiter
    to_db = [(i['מדעי_מחשב'], i['שמות'], i['ת_ז'], i['מתמטיקה'], i['אנגלית'], i['יהדות']) for i in dr]

for row in to_db:
    cur.execute(
        "INSERT INTO SCHOOL_1 ('מדעי_מחשב' ,'שמות', 'ת_ז', 'מתמטיקה', 'אנגלית', 'יהדות') VALUES (?, ?, ?, ?, ?, ?);",
        row)

con.commit()
con.close()
