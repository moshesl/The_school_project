import sqlite3
cur = None

def create_school_db(name_of_school):
    global cur
    con = sqlite3.connect("{}_school.db".format(name_of_school))
    cur = con.cursor()


def create_table_columns(name_of_t):
    cur.execute("""CREATE TABLE IF NOT EXISTS
                (id INTEGER PRIMARY KEY)
                """, (name_of_t))
    cur.commit()


def insert_info(name_of_t, **kwargs):
    for colum_name, value in kwargs:
        cur.execute('update {table} set {key} {val} '.format(table=name_of_t, val=value, key=colum_name))


create_school_db('ha-nisuwi71')
create_table_columns('2016')
