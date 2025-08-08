import sys
import hashlib
sys.path.append("../")
from sqlConnect import dbConnect

db = dbConnect()
cursor = db.cursor()

def signup(nD, nB, usr, pw):
    cursor.execute("SELECT * from users")
    fetched = cursor.fetchall()

    # Memeriksa apakah username sudah dipakai / belum
    for x in fetched:
        if(x[3] == usr):
            return 23

    # Username belum dipakai, lanjut     
    hashedPw = hashlib.sha256(pw.encode()).hexdigest()
    sqlInsert = "INSERT INTO users (namaDepan, namaBelakang, username, password) VALUES(%s, %s, %s, %s)"
    vl = (nD, nB, usr, hashedPw)
    cursor.execute(sqlInsert, vl)
    db.commit()
    if(cursor.rowcount == 1):
        return 30
    else:
        return 25
    
def login(usr, pw):
    cursor.execute("SELECT * from users")
    fetched = cursor.fetchall()

    # Memeriksa apakah username ada
    for x in fetched:
        if(x[3] == usr):
            pwInputHashed = hashlib.sha256(pw.encode()).hexdigest()

            # Memeriksa apakah password benar
            if(pwInputHashed == x[4]):
                cursor.execute(f"UPDATE users SET isLoggedIn = '{x[3]}' WHERE id = {int(x[0])}")
                db.commit()
                return 31
            
            # Password salah
            return 29
    
    # username tidak ada
    return 27

def logout(usr):
    cursor.execute(f"UPDATE users SET isLoggedIn = null WHERE username = '{usr}'")
    db.commit()
    return 32

def deleteAccount(usr):
    cursor.execute(f"DELETE FROM users WHERE username='{usr}'")
    db.commit()
    return 33
    
    # username tidak ditemukan
    
# print(signup("Buda", "Soleh", "kresnawan", "kris123"))

    
