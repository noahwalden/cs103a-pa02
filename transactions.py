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

    # Leora Baumgarten
    # delete according to transaction number
    def delete(self, item_number):
        con = sqlite3.connect(self.database_file)
        cur = con.cursor()
        cur.execute('''DELETE FROM transactions WHERE item_number=(?);''',(item_number,))
        con.commit()
        con.close()

    # Leora Baumgarten
    def summarize_by_month(self):
        con = sqlite3.connect(self.database_file)
        cur = con.cursor()
        cur.execute('''SELECT date, sum(amount), group_concat(distinct category) FROM transactions GROUP BY date''')
        tuples = cur.fetchall()
        con.commit()
        con.close()
        transactions_by_month = {}
        for t in tuples:
            date = t[0].split()
            month = (date[0], date[-1])
            if month in transactions_by_month:
                transactions_by_month[month][0] += t[1]
                transactions_by_month[month][1].add(t[2])
            else: 
                transactions_by_month[month] = [t[1], {t[2]}]
        return [{"month": k, "total_amount": transactions_by_month[k][0], "total_categories": transactions_by_month[k][1]} for k in transactions_by_month]


    def summarize_by_year(self): #Operates assuming the date input format is done by Month/Day/Year For Example 12/25/2012
        """Implemented by Steven Rud"""
        con= sqlite3.connect(self.database_file) #Shows how much was spent in each year regardless of on what it is was spent
        cur = con.cursor()
        cur.execute("select date, sum(amount) from transactions group by date")
        date = cur.fetchall()
        year = []
        years = [x[0] for x in date]
        cash = [c[1] for c in date]
        list_years = list(years)
        for i in list_years:
            i=str(i)
            i=i[-4:]
            i = int(i)
            year.append(i)
        dict_years={}
        for key, val in zip(year,cash): 
            dict_years[key] = dict_years.get(key, 0) + val
        tuple_years = tuple(dict_years.items())
        return [{"Years": t[0], "Total Spent":t[1]} for t in tuple_years]

    def summarize_by_category(self): #Summarizes how much was spent in each category
        """Implemented by Steven Rud"""
        con= sqlite3.connect(self.database_file) #Shows how much was spent in each category regardless of on when it was spent
        cur = con.cursor()
        cur.execute("select group_concat(distinct category), sum(amount) from transactions group by amount")
        cat = cur.fetchall()
        cats = [c[0] for c in cat]
        money = [m[1] for m in cat]
        list_cats= []
        for i in cats:
            i = i.split(',')
            list_cats.extend(i)
        dict_cats={}
        for key, val in zip(list_cats,money): 
            dict_cats[key] = dict_cats.get(key,0) + val
        tuple_years = tuple(dict_cats.items())
        return [{"Category": t[0], "Total Spent":t[1]} for t in tuple_years]

