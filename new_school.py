import sqlite3
import csv


class School:
    cur = None

    def __init__(self):
        pass

    def create_school_db(name_of_school):
        global cur
        con = sqlite3.connect("{}_school.db3".format(name_of_school))
        cur = con.cursor()


    def create_tables(**kwargs):
        cur.executemany('CREATE TABLE IF NOT EXISTS {}(id INTEGER PRIMARY KEY)'.format(kwargs) )
        cur.commit()



