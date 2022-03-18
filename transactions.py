import sqlite3

class Transaction():

    def __init__(self, db_filename):
        self.c = db_filename
        con= sqlite3.connect(db_filename)
        cur = con.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS transactions
                    ('item #' int, amount int, category text, date text, description text)''')
        con.commit()
        con.close()
