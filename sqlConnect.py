def dbConnect():
    import mysql.connector

    mysqlhost = open("C:/Users/Kris/Documents/code/ledger_server/mysqlhost.txt", "r").read()
    mysqluser = open("C:/Users/Kris/Documents/code/ledger_server/mysqluser.txt", "r").read()
    mysqlpassword = open("C:/Users/Kris/Documents/code/ledger_server/mysqlpassword.txt", "r").read()
    mysqldb = open("C:/Users/Kris/Documents/code/ledger_server/mysqldb.txt", "r").read()

    mydb = mysql.connector.connect(
        host = mysqlhost,
        user = mysqluser,
        password = mysqlpassword,
        database = mysqldb
    )   
    return mydb

