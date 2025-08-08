from flask import Flask
from flask import request
from user import signup

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello world!</h1>"

@app.route("/signup", methods=['POST'])
def signup_():
    res = signup(request.form["nD"], request.form["nB"], request.form["usr"], request.form["pw"])
    if(res == 1):
        return "Telah berhasil membuat akun"
    else:
        return "Terjadi error"

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