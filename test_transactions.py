'''
category.py is a Object Relational Mapping to the transactions table

The ORM will work map SQL rows with the schema
    (item_number, amount, category, date, description)
to Python Dictionaries.

This app will store the data in a SQLite database ~/tracker.db

'''

import pytest
from transactions import Transaction

@pytest.fixture
def dbfile(tmpdir):
    ''' create a database file in a temporary file system '''
    return tmpdir.join('test_tracker.db')

@pytest.fixture
def transaction(dbfile):
    ''' create an empty database '''
    db = Transaction(dbfile)
    yield db

@pytest.fixture
def small_transaction(transaction):
    cat1 = {'item_number':1,'amount':25,'category':'food','date':'2021-05-18','description':'steak dinner'}
    cat2 = {'item_number':2,'amount':40,'category':'school','date':'2021-05-18','description':'notebooks and pens'}
    cat3 = {'item_number':3,'amount':30,'category':'gas','date':'2022-04-12','description':'diesel'}
    cat4 = {'item_number':4,'amount':62,'category':'gas','date':'2019-02-05','description':'regular'}
    cat5 = {'item_number':5,'amount':89,'category':'gift','date':'2019-02-05','description':'birthday present'}
    cat6 = {'item_number':6,'amount':45,'category':'school','date':'2022-04-12','description':'textbooks'}
    transaction.add(cat1)
    transaction.add(cat2)
    transaction.add(cat3)
    transaction.add(cat4)
    transaction.add(cat5)
    transaction.add(cat6)
    return transaction

# test the first data in the tracker db
@pytest.mark.show
def test_select_all():
    transaction = Transaction('tracker.db')
    items = transaction.select_all()
    assert items[0]['item_number'] == 1
    assert items[0]['amount'] == 1

# test the first data in the tracker db
@pytest.mark.date_summary
def test_date_summary(small_transaction):
    """Implemented by Noah"""
    items = small_transaction.summarize_by_date()
    assert len(items) == 3
    assert "date" in items[0]
    assert "total_amount" in items[0]
    assert "categories" in items[0]

# test the first data in the tracker db
@pytest.mark.add
def test_add(transaction):
    """Implemented by Noah"""
    transaction.add({'item_number':1,'amount':25,'category':'food','date':'2021-05-18','description':'steak dinner'})
    transaction.add({'item_number':2,'amount':40,'category':'school','date':'2021-05-18','description':'notebooks and pens'})
    transaction.add({'item_number':3,'amount':30,'category':'gas','date':'2022-04-12','description':'diesel'})
    transaction.add({'item_number':4,'amount':62,'category':'gas','date':'2019-02-05','description':'regular'})
    transaction.add({'item_number':5,'amount':89,'category':'gift','date':'2019-02-05','description':'birthday present'})
    transaction.add({'item_number':6,'amount':45,'category':'school','date':'2022-04-12','description':'textbooks'})
    assert len(transaction.select_all()) == 6
