# write a program that connects to db and fetches all records matching where category = "record" from "customers" table

```python
import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='python_db',
                                         user='pynative',
                                         password='pynative@#29')

    sql_select_Query = "select * from customers where category = 'record'"
    # can you fix the above query to use parameterized query instead of hardcoding the value?
    sql_select_Query = "select * from customers where category = %s"
    category = ("record",)
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    print("Total number of rows in python_developers is - ", cursor.rowcount)
    print("Printing each row's column values i.e.  developer record")
    for row in records:
        print("Id = ", row[0], )
        print("Name = ", row[1])
        print("JoiningDate  = ", row[2])
        print("Salary  = ", row[3], "\n")
except Error as e:
    print("Error reading data from MySQL table", e)


