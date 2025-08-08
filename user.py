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
        return 1
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
                return 28
            
            # Password salah
            return 29
    
    # username tidak ada
    return 27

def deleteAccount(usr):
    cursor.execute("SELECT * from users")
    fetched = cursor.fetchall()

    for x in fetched:
        if(x[3] == usr):
            # hapus akun dari database
            cursor.execute(f"DELETE FROM users WHERE username='{x[3]}'")
            db.commit()
            return 1
    
    # username tidak ditemukan
    return 27
    
# print(signup("Buda", "Soleh", "kresnawan", "kris123"))

    
