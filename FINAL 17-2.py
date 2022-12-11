# 17.2 (Cursor Method fetchall and Attribute description) When you use a
# sqlite3 Cursor’s execute method to perform a query, the query’s
# results are stored in the Cursor object. The Cursor attribute
# description contains metadata about the results stored as a tuple of
# tuples. Each nested tuple’s first value is a column name in the query
# results. Cursor method fetchall returns the query result’s data as a
# list of tuples. Investigate the description attribute and fetchall
#  method. Open the books database and use Cursor method execute to
# select all the data in the titles table, then use description and
# fetchall to display the data in tabular format.

import sqlite3

# Opening the books database
conn = sqlite3.connect('books.db')

# Creating a cursor
cursor = conn.cursor()

# Executing a query that selects all data from the titles table
cursor.execute("SELECT * FROM titles")

# Getting the metadata using the description attribute
description = cursor.description

# Getting the data using the fetchall method
data = cursor.fetchall()

# Printing the results in a tabular format
for row in data:
    print("%-20s%-20s%-20s" % (row[0], row[1], row[2]))