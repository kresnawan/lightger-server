from flask import Flask
from flask import request
from flask import make_response
from flask_cors import CORS
from user import signup, login, logout, deleteAccount
from data import getUserTransaction, getUserFunds

app = Flask(__name__)
CORS(app, resources={"/*" : {"origins" : "*"}}, supports_credentials=True)

@app.route("/")
def hello_world():
    return "<h1>Hello world!</h1>"

@app.route("/signup", methods=['POST'])
def signup_():
    
    res = signup(request.form["nD"], request.form["nB"], request.form["usr"], request.form["pw"])
    resp = make_response({'status': res})
    return resp

@app.route("/login", methods=['POST'])
def login_():
    usern = request.form["usr"]
    passw = request.form["pw"]
    res = login(usern, passw)
    if(res == 31):
        resp = make_response("Managed to login")
        resp.set_cookie("user", usern, domain='127.0.0.1')
        return resp
    
    return "Login gagal"

@app.route("/logout", methods=['GET'])
def logout_():
    res = logout(request.cookies["user"])
    resp = make_response({'status': res})
    resp.delete_cookie("user")
    return resp

@app.route("/deleteacc", methods=['POST'])
def deleteacc_():
    res = deleteAccount(request.form["usr"])
    resp = make_response({'status': res})
    resp.delete_cookie("user")
    return resp
    

    # res = make_response("Creating cookie")
    # res.set_cookie("user", "kris", domain='127.0.0.1')
    # return res

# mycursor.execute('DELETE FROM users WHERE id = 2')
# mydb.commit()



# for x in mycursor:
#     print(x)