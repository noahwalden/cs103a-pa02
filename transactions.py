import sqlite3

from category import to_cat_dict


def to_transaction_dict(transaction_tuple):
    transaction = {
        "item_number": transaction_tuple[0],
        "amount": transaction_tuple[1],
        "category": transaction_tuple[2],
        "date": transaction_tuple[3],
        "description": transaction_tuple[4],
    }
    return transaction


def to_transaction_dict_list(transaction_tuple):
    return [to_transaction_dict(transaction) for transaction in transaction_tuple]


class Transaction:
    def __init__(self, db_filename):
        self.database_file = db_filename
        con = sqlite3.connect(db_filename)
        cur = con.cursor()
        cur.execute(
            """CREATE TABLE IF NOT EXISTS transactions
                    (
                    item_number int,
                    amount int,
                     category text,
                    date text,
                    description text)"""
        )
        con.commit()
        con.close()

    def add(self, item):
        con = sqlite3.connect(self.database_file)
        cur = con.cursor()
        cur.execute(
            "INSERT INTO transactions VALUES(?,?,?,?,?)",
            (
                item["item_number"],
                item["amount"],
                item["category"],
                item["date"],
                item["description"],
            ),
        )
        con.commit()
        con.close()

    # show transactions
    def select_all(self):
        ''' return all of the transactions as a list of dicts.'''
        con= sqlite3.connect(self.database_file)
        cur = con.cursor()
        cur.execute("SELECT item_number,* from transactions")
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return to_transaction_dict_list(tuples)

    def summarize_by_date(self):
        pass
