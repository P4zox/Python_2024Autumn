from flask import Flask
from flask import render_template
from flask import request
app=Flask(__name__)


@app.route('/journal')
def journal():
    return render_template('Hw1-1.html')

@app.route('/question')
def question():
    return render_template('Hw3-1.html')

@app.route('/hosting/<host>')
def indedx(host):
    return render_template('Hw1-1 copy.html',host=host)

@app.route('/request')
def requesting():
    print('請求方法: ', request.method)
    print('通訊協定: ', request.scheme)
    print('主機名稱: ', request.host)
    print('路徑: ', request.path)
    print('完整網路: ', request.url)
    print('瀏覽器作業系統: {}'.format(request.headers.get("user-agent")))
    print('語言偏好: {}'.format(request.headers.get("accept-language")))
    print('引薦網址: {}'.format(request.headers.get("referrer")))
    return "Hello Flask"

@app.route('/methods',methods=['GET'])
def getting():
    name = request.args.get('name')
    print('使用者名字是: ',name)
    return "Hello Flask and hello {}".format(name)

@app.route('/fruit')
def fruit():
    return"<form method='post' action='/fruit/submit'> <p>Enter your favorite fruit:</p> <input type='text' name='fruit_name' /> <button type='submit'>Submit</button></form>"

@app.route("/fruit/submit",methods=['POST'])
def submit():
    fruit_name = request.values['fruit_name']
    return 'I also like ' + fruit_name

@app.route('/login')
def login():
    return "<form method='post' action='/login/submit'> <p>Enter your username: </p> <input type='text' name='username' /> <p>Enter your password: </p> <input type='text' name='password' /> <button type='submit2'>Submit</button></form>"

@app.route('/login/submit', methods=['POST'])
def submit2():
    username = request.values['username']
    password = request.values['password']
    return "Hello {}, your password is {}".format(username, password)

app.run()