from flask import Flask
from flask import render_template
from flask import request
app=Flask(__name__)


@app.route('/')
def index():
    return "<h1> Welcome to my web</h1>"

@app.route('/question')
def question():
    return render_template('Hw3-1 copy.html')

@app.route('/question/submit', methods=['POST'])
def submit():
    username=request.values['account']
    email=request.values['email']
    radio=request.values['radio']
    return "<p>表單成功繳交!你的資料如下:</p> <p>姓名: {}\n </p><p>信箱: {}\n </p><p>有興趣的項目: {}</p>".format(username, email, radio)

app.run()



