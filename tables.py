# -*- coding: utf-8 -*-
"""
Created on Sun Dec 19 10:54:49 2021

@author: gummadi
"""

import mysql.connector as sql


mydb = sql.connect(
  host="localhost",
  user="root",
  password="Grssn12345@",
  database="book_system"
)

print(mydb)

mycursor = mydb.cursor()

'''mycursor.execute("CREATE DATABASE book_system1")'''

mycursor.execute("CREATE TABLE stock_details1 (s_no int,stock_name char(40),order_qty int,order_type varchar(40),execute_qty int,price int,order_status varchar(40),order_date date)")

