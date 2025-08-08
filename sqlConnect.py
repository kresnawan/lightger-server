import os
from dotenv import load_dotenv

load_dotenv()

mysqlhost = os.getenv('MYSQL_HOST')
mysqluser = os.getenv('MYSQL_USER')
mysqlpassword = os.getenv('MYSQL_PASSWORD')
mysqldb = os.getenv('MYSQL_DB')

def dbConnect():
    import mysql.connector

    mydb = mysql.connector.connect(
        host = mysqlhost,
        user = mysqluser,
        password = mysqlpassword,
        database = mysqldb
    )   
    return mydb

