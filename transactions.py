import sqlite3

def to_transaction_dict(transaction_tuple):
    """Converts row in SQLite to a dict"""
    transaction = {
        "item_number": transaction_tuple[0],
        "amount": transaction_tuple[1],
        "category": transaction_tuple[2],
        "date": transaction_tuple[3],
        "description": transaction_tuple[4],
    }
    return transaction


def to_transaction_dict_list(transaction_tuple_list):
    """Converts a list of SQLite row tuples to a list of dicts"""
    return [to_transaction_dict(transaction) for transaction in transaction_tuple_list]


class Transaction:
    """Represents a collection of transactions"""
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
        """Implemented by Noah"""
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
        cur.execute("SELECT * from transactions")
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return to_transaction_dict_list(tuples)

    def summarize_by_date(self):
        """Implemented by Noah"""
        con = sqlite3.connect(self.database_file)
        cur = con.cursor()
        cur.execute("select date, sum(amount), group_concat(distinct category) from transactions group by date")

        tuples = cur.fetchall()
        con.commit()
        con.close()

        return [{"date": t[0], "total_amount": t[1], "categories": t[2]} for t in tuples]
