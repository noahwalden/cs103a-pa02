'''
category.py is a Object Relational Mapping to the transactions table

The ORM will work map SQL rows with the schema
    (item_number, amount, category, date, description)
to Python Dictionaries.

This app will store the data in a SQLite database ~/tracker.db

'''

import pytest
from transactions import Transaction

# test the first data in the tracker db
@pytest.mark.show
def test_select_all():
    transaction = Transaction('tracker.db')
    items = transaction.select_all()
    assert items[0]['item_number'] == 1
    assert items[0]['amount'] == 1