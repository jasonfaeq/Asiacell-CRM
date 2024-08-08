# Steps to create a database in MySQL using Python
# Installed MySQL
# https://dev.mysql.com/downloads/installer/
# pip install mysql
# pip install mysql-connector
# pip install mysql-connector-python

import mysql.connector

dataBase = mysql.connector.connect(
    host= "localhost",
    user= "root",
    passwd= "root",
)


# Prepare a cursor object using cursor() method
cursorObject = dataBase.cursor()

# Create database
cursorObject.execute("CREATE DATABASE lvlupco")

print("Database created successfully")