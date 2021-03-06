#! /opt/miniconda3/bin/python3
'''
tracker is an app that maintains a list of personal
financial transactions.

It uses Object Relational Mappings (ORM)
to abstract out the database operations from the
UI/UX code.

The ORM, Category, will map SQL rows with the schema
  (rowid, category, description)
to Python Dictionaries as follows:

(5,'rent','monthly rent payments') <-->

{rowid:5,
 category:'rent',
 description:'monthly rent payments'
 }

Likewise, the ORM, Transaction will mirror the database with
columns:
amount, category, date (yyyymmdd), description

In place of SQL queries, we will have method calls.

This app will store the data in a SQLite database ~/tracker.db

Note the actual implementation of the ORM is hidden and so it
could be replaced with PostgreSQL or Pandas or straight python lists

'''

from transactions import Transaction
from category import Category

transactions = Transaction('tracker.db')
category = Category('tracker.db')


# here is the menu for the tracker app

MENU = '''
0. quit
1. show categories
2. add category
3. modify category
4. show transactions
5. add transaction
6. delete transaction
7. summarize transactions by date
8. summarize transactions by month
9. summarize transactions by year
10. summarize transactions by category
11. print this menu
'''




def process_choice(choice):
    """Process the choice associated with the provided number"""

    if choice=='0':
        return
    elif choice=='1':
        cats = category.select_all()
        print_categories(cats)
    elif choice=='2':
        name = input("category name: ")
        desc = input("category description: ")
        cat = {'name':name, 'desc':desc}
        category.add(cat)
    elif choice=='3':
        print("modifying category")
        rowid = int(input("rowid: "))
        name = input("new category name: ")
        desc = input("new category description: ")
        cat = {'name':name, 'desc':desc}
        category.update(rowid,cat)
    elif choice == '4':
        print_transactions(transactions.select_all())
    elif choice=='5':
        item_number = input("transaction number: ")
        amount = input("transaction amount: ")
        cat = input("transaction category: ")
        date = input("transaction date: ")
        description = input("transaction description: ")
        transaction = {'item_number': item_number ,'amount': amount, 'category': cat, 'date': date, 'description': description}
        transactions.add(transaction)
    elif choice=='6':
        # Leora Baumgarten
        item_number = int(input("item number of transaction to be deleted: "))
        transactions.delete(item_number)
    elif choice=='7':
        print_date_summary(transactions.summarize_by_date())
    elif choice == '8':
        # Leora Baumgarten
        print_month_summary(transactions.summarize_by_month())
    elif choice == '9': #Steven Rud
        print_year_summary(transactions.summarize_by_year())
    elif choice == '10': #Steven Rud
        print_cat_summary(transactions.summarize_by_category())
    elif choice =='11':
        toplevel()
    else:
        print("choice",choice,"not yet implemented")

    choice = input("> ")
    return(choice)


def toplevel():
    ''' read the command args and process them'''
    print(MENU)
    choice = input("> ")
    while choice !='0' :
        choice = process_choice(choice)
    print('bye')

#
# here are some helper functions
#

def print_transactions(items):
    ''' print the transactions '''
    if len(items)==0:
        print('no items to print')
        return
    print('\n')
    print("%-10s %-10s %-10s %-10s %-30s"%(
        'item #','amount','category','date','description'))
    print('-'*40)
    for item in items:
        values = tuple(item.values()) 
        print("%-10d %-10d %-10s %-10s %-30s"%values)

def print_category(cat):
    """print a category"""
    print("%-3d %-10s %-30s"%(cat['rowid'],cat['name'],cat['desc']))

def print_categories(cats):
    """print multiple categories"""
    print("%-3s %-10s %-30s"%("id","name","description"))
    print('-'*45)
    for cat in cats:
        print_category(cat)

def print_date_summary(date_dicts):
    """summarize transactions by date"""
    for date in date_dicts:
        print("Date:", date["date"])
        print("Total amount spent:", date["total_amount"])
        print("Categories of spending:", date["categories"])
        print()

# Leora Baumgarten: 
def print_month_summary(months):
    """summarize transactions by month"""
    for month in months:
        print("Month:", month["month"])
        print("Total amount spent:", month["total_amount"])
        print("Categories of spending:", month["total_categories"])
        print()

def print_year_summary(year_dicts):
    """Code by Steven Rud, printing the summary by years"""
    for y in year_dicts:
        print("Year: ",y["Years"])
        print("Total Spent in the Year: ",y["Total Spent"])
        print()

def print_cat_summary(cat_dicts):
    """Code by Steven Rud, printing the summary by category"""
    for y in cat_dicts:
        print("Category: ",y["Category"])
        print("Total Spent in the Category: ",y["Total Spent"])
        print()


# here is the main call!

toplevel()
