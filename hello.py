import mysql.connector
from flask import Flask
from flask import request


mydb = mysql.connector.connect(
    host = "212.85.25.153",
    user = "kris",
    password = "Krisnauwu875",
    database = "mydb"
)



sqlInsert = "INSERT INTO users (namaDepan, namaBelakang, username, password) VALUES(%s, %s, %s, %s)"
vl = ("Tri", "Habibi", "trihabibi", "Hab123")


mycursor = mydb.cursor()
app = Flask(__name__)



@app.route("/")
def hello_world():
    return "<h1>Hello world!</h1>"

@app.route("/users")
def showdata():
    mycursor.execute("SELECT * from users")
    resultan = mycursor.fetchall()
    return resultan

@app.route("/user/<username>")
def user_show(username):
    return f"This is {username}'s page!"

@app.route("/login", methods=['POST'])
def login():
    return f"This request sent by {request.form["user"]} that's aged {request.form["age"]} years old!"
# mycursor.execute('DELETE FROM users WHERE id = 2')
# mydb.commit()




# for x in mycursor:
#     print(x)