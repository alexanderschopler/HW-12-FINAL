# 17.1 (Books Database) In an IPython session, perform each of the
# following tasks on the books database from Section 17.2:
#   1. Select all authors’ last names from the authors table in descending order.
#   2. Select all book titles from the titles table in ascending order.
#   3. Use an INNER JOIN to select all the books for a specific author. Include the title, copyright year and ISBN. Order the information alphabetically by title.
#   4. Insert a new author into the authors table.
#   5. Insert a new title for an author. Remember that the book must have an entry in the author_ISBN table and an entry in the titles table.

import sqlite3
import pandas as pd

connection = sqlite3.connect('books.db')

pd.options.display.max_columns = 10

#a
print('')
print('PART A')
print('')
print(pd.read_sql('SELECT last FROM authors ORDER BY last DESC', connection))

#b
print('')
print('PART B')
print('')
print(pd.read_sql('SELECT title FROM titles ORDER BY title ASC', connection))

#c
print('')
print('PART C')
print('')
print('Books written by Paul Deitel')
print(pd.read_sql('SELECT title, copyright, titles.isbn FROM titles INNER JOIN author_ISBN ON titles.isbn = author_ISBN.isbn WHERE author_ISBN.id=1 ORDER BY title ASC', connection))

#d
print('')
print('PART D')
print('')
cursor = connection.cursor()
cursor.execute('INSERT INTO authors (first, last) VALUES (\'Matt\', \'Pembroke\')')
authors = pd.read_sql('SELECT id, first, last FROM authors', connection, index_col=['id'])
print(authors)

#e
print('')
print('PART E')
print('')
cursor.execute('INSERT INTO author_ISBN (id, isbn) VALUES (6, \'0000000000\')')
cursor.execute('INSERT INTO titles (isbn, title, edition, copyright) VALUES (\'0000000000\',\'Example Book\',1,\'2020\')')
print(pd.read_sql('SELECT * FROM author_ISBN', connection))
print(pd.read_sql('SELECT * FROM titles', connection))

connection.close()