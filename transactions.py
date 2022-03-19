import sqlite3


def to_transaction_dict(transaction_tuple):
    transaction = {
        "item #": transaction_tuple[0],
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
                    (amount int, category text, date text, description text)"""
        )
        con.commit()
        con.close()

    def add(self, item):
        con = sqlite3.connect(self.database_file)
        cur = con.cursor()
        cur.execute(
            "INSERT INTO transactions VALUES(?,?,?,?)",
            (
                item["amount"],
                item["category"],
                item["date"],
                item["description"],
            ),
        )
        con.commit()
        con.close()

    def summarize_by_date(self):
        pass
