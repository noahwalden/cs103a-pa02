Financial transaction tracker program for CS103A PA02
```
Script started on Fri Mar 25 04:16:58 2022

(base) PS C:\Users\Steven\Desktop\PA02\cs103a-pa02> python tracker.py

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

> 1
id  name       description
---------------------------------------------
> 2
category name: Groceries
category description: Food and Drinks
> 2
category name: Wardrobe
category description: Clothes
> 2
category name: Toys
category description: Kids Toys
> 1
id  name       description
---------------------------------------------
1   Groceries  Food and Drinks
2   Wardrobe   Clothes
3   Toys       Kids Toys
> 3
modifying category
rowid: 2
new category name: Clothes
new category description: Clothing
> 1
id  name       description
---------------------------------------------
1   Groceries  Food and Drinks
2   Clothes    Clothing
3   Toys       Kids Toys
> 4
no items to print
> 5
transaction number: 1
transaction amount: 15
transaction category: Groceries
transaction date: 1/14/2021
transaction description: Apples and Water
> 5
transaction number: 2
transaction amount: 8
transaction category: Groceries
transaction date: 3/24/2021
transaction description: Soda
> 4


item #     amount     category   date       description
----------------------------------------
1          15         Groceries  1/14/2021  Apples and Water
2          8          Groceries  3/24/2021  Soda
> 5
transaction number: 3
transaction amount: 79
transaction category: Clothes
transaction date: 7/30/2019
transaction description: Shirts and Pants
> 5
transaction number: 4
transaction amount: 30
transaction category: Toys
transaction date: 12/20/2020
transaction description: Toy Cars
> 4


item #     amount     category   date       description
----------------------------------------
1          15         Groceries  1/14/2021  Apples and Water
2          8          Groceries  3/24/2021  Soda
3          79         Clothes    7/30/2019  Shirts and Pants
4          30         Toys       12/20/2020 Toy Cars
> 5
transaction number: 5
transaction amount: 45
transaction category: Clothes
transaction date: 6/7/2020
transaction description: Shorts
> 5
transaction number: 6
transaction amount: 19
transaction category: Toys
transaction date: 12/25/2020
transaction description: Teddy Bear
> 4


item #     amount     category   date       description
----------------------------------------
1          15         Groceries  1/14/2021  Apples and Water
2          8          Groceries  3/24/2021  Soda
3          79         Clothes    7/30/2019  Shirts and Pants
4          30         Toys       12/20/2020 Toy Cars
5          45         Clothes    6/7/2020   Shorts
6          19         Toys       12/25/2020 Teddy Bear
> 5
transaction number: 7
transaction amount: 23
transaction category: Groceries
transaction date: 4/14/2022
transaction description: Vegetables
> 11

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

> 4


item #     amount     category   date       description
----------------------------------------
1          15         Groceries  1/14/2021  Apples and Water
2          8          Groceries  3/24/2021  Soda
3          79         Clothes    7/30/2019  Shirts and Pants
4          30         Toys       12/20/2020 Toy Cars
5          45         Clothes    6/7/2020   Shorts
6          19         Toys       12/25/2020 Teddy Bear
7          23         Groceries  4/14/2022  Vegetables
> 6
item number of transaction to be deleted: 7
> 4


item #     amount     category   date       description
----------------------------------------
1          15         Groceries  1/14/2021  Apples and Water
2          8          Groceries  3/24/2021  Soda
3          79         Clothes    7/30/2019  Shirts and Pants
4          30         Toys       12/20/2020 Toy Cars
5          45         Clothes    6/7/2020   Shorts
6          19         Toys       12/25/2020 Teddy Bear
> 7
Date: 1/14/2021
Total amount spent: 15
Categories of spending: Groceries

Date: 12/20/2020
Total amount spent: 30
Categories of spending: Toys

Date: 12/25/2020
Total amount spent: 19
Categories of spending: Toys

Date: 3/24/2021
Total amount spent: 8
Categories of spending: Groceries

Date: 6/7/2020
Total amount spent: 45
Categories of spending: Clothes

Date: 7/30/2019
Total amount spent: 79
Categories of spending: Clothes

> 8
Month: ('1/14/2021', '1/14/2021')
Total amount spent: 15
Categories of spending: {'Groceries'}

Month: ('12/20/2020', '12/20/2020')
Total amount spent: 30
Categories of spending: {'Toys'}

Month: ('12/25/2020', '12/25/2020')
Total amount spent: 19
Categories of spending: {'Toys'}

Month: ('3/24/2021', '3/24/2021')
Total amount spent: 8
Categories of spending: {'Groceries'}

Month: ('6/7/2020', '6/7/2020')
Total amount spent: 45
Categories of spending: {'Clothes'}

Month: ('7/30/2019', '7/30/2019')
Total amount spent: 79
Categories of spending: {'Clothes'}

> 9
Year:  2021
Total Spent in the Year:  23

Year:  2020
Total Spent in the Year:  94

Year:  2019
Total Spent in the Year:  79

> 10
Category:  Groceries
Total Spent in the Category:  23

Category:  Toys
Total Spent in the Category:  49

Category:  Clothes
Total Spent in the Category:  124

> 11

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

> 1
id  name       description
---------------------------------------------
1   Groceries  Food and Drinks
2   Clothes    Clothing
3   Toys       Kids Toys
> 4


item #     amount     category   date       description
----------------------------------------
1          15         Groceries  1/14/2021  Apples and Water
2          8          Groceries  3/24/2021  Soda
3          79         Clothes    7/30/2019  Shirts and Pants
4          30         Toys       12/20/2020 Toy Cars
5          45         Clothes    6/7/2020   Shorts
6          19         Toys       12/25/2020 Teddy Bear
> 0
bye
(base) PS C:\Users\Steven\Desktop\PA02\cs103a-pa02> pylint transactions.py
************* Module transactions
transactions.py:70:0: C0301: Line too long (112/100) (line-too-long)
transactions.py:91:0: C0301: Line too long (116/100) (line-too-long)
transactions.py:102:17: C0303: Trailing whitespace (trailing-whitespace)
transactions.py:104:0: C0301: Line too long (154/100) (line-too-long)
transactions.py:107:0: C0301: Line too long (122/100) (line-too-long)
transactions.py:109:0: C0301: Line too long (125/100) (line-too-long)
transactions.py:123:39: C0303: Trailing whitespace (trailing-whitespace)
transactions.py:130:0: C0301: Line too long (126/100) (line-too-long)
transactions.py:132:0: C0301: Line too long (108/100) (line-too-long)
transactions.py:141:45: C0303: Trailing whitespace (trailing-whitespace)
transactions.py:145:0: C0305: Trailing newlines (trailing-newlines)
transactions.py:1:0: C0114: Missing module docstring (missing-module-docstring)
transactions.py:80:4: C0116: Missing function or method docstring (missing-function-docstring)
transactions.py:88:4: C0116: Missing function or method docstring (missing-function-docstring)
transactions.py:96:12: C0103: Variable name "t" doesn't conform to snake_case naming style (invalid-name)
transactions.py:104:0: C0206: Consider iterating with .items() (consider-using-dict-items)

------------------------------------------------------------------
Your code has been rated at 8.28/10 (previous run: 8.28/10, +0.00)

(base) PS C:\Users\Steven\Desktop\PA02\cs103a-pa02> pylint tracker.py
************* Module tracker
tracker.py:89:0: C0301: Line too long (127/100) (line-too-long)
tracker.py:110:0: C0325: Unnecessary parens after 'return' keyword (superfluous-parens)
tracker.py:135:37: C0303: Trailing whitespace (trailing-whitespace)
tracker.py:157:19: C0303: Trailing whitespace (trailing-whitespace)
tracker.py:64:4: R1705: Unnecessary "elif" after "return" (no-else-return)
tracker.py:61:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
tracker.py:61:0: R0912: Too many branches (13/12) (too-many-branches)
tracker.py:168:8: C0103: Variable name "y" doesn't conform to snake_case naming style (invalid-name)
tracker.py:175:8: C0103: Variable name "y" doesn't conform to snake_case naming style (invalid-name)

------------------------------------------------------------------
Your code has been rated at 9.05/10 (previous run: 9.05/10, +0.00)

(base) PS C:\Users\Steven\Desktop\PA02\cs103a-pa02> pytest -v -m delete
================================================= test session starts =================================================
platform win32 -- Python 3.9.7, pytest-6.2.5, py-1.10.0, pluggy-0.13.1 -- C:\Users\Steven\anaconda3\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\Steven\Desktop\PA02\cs103a-pa02, configfile: pytest.ini
plugins: anyio-2.2.0
collected 9 items / 7 deselected / 2 selected

test_category.py::test_delete PASSED                                                                             [ 50%]
test_transactions.py::test_delete PASSED                                                                         [100%]

=========================================== 2 passed, 7 deselected in 0.24s ===========================================
(base) PS C:\Users\Steven\Desktop\PA02\cs103a-pa02> pytest -v -m date_summary
================================================= test session starts =================================================
platform win32 -- Python 3.9.7, pytest-6.2.5, py-1.10.0, pluggy-0.13.1 -- C:\Users\Steven\anaconda3\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\Steven\Desktop\PA02\cs103a-pa02, configfile: pytest.ini
plugins: anyio-2.2.0
collected 9 items / 8 deselected / 1 selected

test_transactions.py::test_date_summary PASSED                                                                   [100%]

=========================================== 1 passed, 8 deselected in 0.08s ===========================================
(base) PS C:\Users\Steven\Desktop\PA02\cs103a-pa02> pytest -v
================================================= test session starts =================================================
platform win32 -- Python 3.9.7, pytest-6.2.5, py-1.10.0, pluggy-0.13.1 -- C:\Users\Steven\anaconda3\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\Steven\Desktop\PA02\cs103a-pa02, configfile: pytest.ini
plugins: anyio-2.2.0
collected 9 items

test_category.py::test_to_cat_dict PASSED                                                                        [ 11%]
test_category.py::test_add PASSED                                                                                [ 22%]
test_category.py::test_delete PASSED                                                                             [ 33%]
test_category.py::test_update PASSED                                                                             [ 44%]
test_transactions.py::test_select_all PASSED                                                                     [ 55%]
test_transactions.py::test_date_summary PASSED                                                                   [ 66%]
test_transactions.py::test_add PASSED                                                                            [ 77%]
test_transactions.py::test_delete PASSED                                                                         [ 88%]
test_transactions.py::test_month_summary PASSED                                                                  [100%]

================================================== 9 passed in 0.48s ==================================================

Script done on Fri Mar 25 04:49:13 2022
```