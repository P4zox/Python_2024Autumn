from flask import Flask
# app=Flask(__name__)
app=Flask(__name__, static_folder="static", static_url_path="/static")

@app.route("/")
def index():
    return "Welcome to my web!"
@app.route("/member/<name>")
def sayHi(name):
    return "Hello, our favorite member: "+name

@app.route("/admin/<level>")
def login(level):
    if level=="A":
        return "Login here!"
    else:
        return "You can not login in!"
    


app.run()