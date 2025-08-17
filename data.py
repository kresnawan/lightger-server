from sqlConnect import dbConnect
from datetime import datetime

db = dbConnect()
cursor = db.cursor()

def setFunds(id, add):
    cursor.execute(f"UPDATE funds SET fund = '{add}' WHERE userId = '{id}'")
    db.commit()
    return cursor.rowcount

def resetFunds(id):
    cursor.execute(f"UPDATE funds SET fund = '0' WHERE userId = '{id}'")
    db.commit()
    return cursor.rowcount

def getUserTransaction(id):
    cursor.execute(f"SELECT * from user_transactions WHERE userId= '{id}' ")
    data = cursor.fetchall()
    return data

def getUserFunds(id):
    cursor.execute(f"SELECT * from funds WHERE userId='{id}'")
    data = cursor.fetchall()
    return data

def inputUserTransaction(status, nominal, id, title, desc):

    if(status == 0):
        cursor.execute(f"SELECT fund from funds WHERE userId = '{id}'")
        data = cursor.fetchall()

        totalFund = int(data[0][0])
        resultFund = totalFund - nominal

        cursor.execute(f"UPDATE funds SET fund = '{resultFund}' WHERE userId = '{id}'")
    
    if(status == 1):
        cursor.execute(f"SELECT fund from funds WHERE userId = '{id}'")
        data = cursor.fetchall()

        totalFund = int(data[0][0])
        resultFund = totalFund + nominal

        cursor.execute(f"UPDATE funds SET fund = '{resultFund}' WHERE userId = '{id}'")

    now = datetime.now()
    sqlInput = "INSERT INTO user_transactions (status, nominal, date, userId, title, description) VALUES (%s, %s, %s, %s, %s, %s)"
    vl = (status, nominal, str(now), id, title, desc)
    cursor.execute(sqlInput, vl)
    ress = cursor.rowcount
    db.commit()
    return ress


def syncFundUser():
    cursor.execute("SELECT * from users")
    data = cursor.fetchall()

    for x in data:
        cursor.execute(f"UPDATE funds SET fund = '500000' WHERE userId = '{x[0]}'")
        db.commit()
# inputUserTransaction(0, 12000, 9, "Geprek kak rose", "Geprek crispy")
# inputUserTransaction(0, 12000, 10, "Geprek kak rose", "Geprek crispy")
# inputUserTransaction(0, 12000, 10, "Geprek kak rose", "Geprek crispy")
# inputUserTransaction(0, 12000, 8, "Geprek kak rose", "Geprek crispy")
# inputUserTransaction(0, 12000, 14, "Geprek kak rose", "Geprek crispy")
# inputUserTransaction(0, 12000, 14, "Geprek kak rose", "Geprek crispy")
# inputUserTransaction(0, 12000, 8, "Geprek kak rose", "Geprek crispy")
inputUserTransaction(0, 12000, 9, "Geprek kak rose", "Geprek crispy")
# print(setFunds(14, 500000))
# syncFundUser()
# print(resetFunds(14))

