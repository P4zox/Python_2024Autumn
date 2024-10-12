from flask import Flask
app=Flask(__name__)
# app=Flask(__name__, static_folder="static", static_url_path="/static")

@app.route("/")
def index():
    return "Welcome to my web!"

@app.route("/journal/<classes>")
def class1(classes):
    if classes == "class1":
        return "<h1> 我的心情小天地 </h1> <hr> <h3> 關於我 </h3> <p> 我叫科翰，我喜歡電動、耍廢和<strong>寫程式</strong> </p> <h3> 關我的每一天 </h3> <h6> 2024-02-25 </h6> <p> 今天上課，老師教了我如何用html來做網頁</p> <br> <h6> 2024-03-02 </h6> <p> 今天是寫酷博功課的第一天~ T_T</p>"
    elif classes == "class2":
        return "<h1> 我的歷年成績紀錄 </h1><hr><table border='1'>  <caption> 國一成績單 </caption><tr> <th> 學期 </th><th> 國文 </th><th> 數學 </th><th> 英文 </th></tr><tr> <td> 上 </td><td> 20 </td><td> 30 </td><td> 77 </td></tr><tr> <td> 下 </td><td> 77 </td><td> 99 </td><td> 50 </td></tr></table><br><h3> 學年總結 </h3><br><ul> <li> 英文成績退步了，要更加努力讀<strong> 英文 </strong></li><li> 國文和數學的學習方式正確! <em> 繼續保持! </em> </li></ul><hr><table border='1'>  <caption> 國二成績單 </caption><tr> <th> 學期 </th><th> 國文 </th><th> 數學 </th><th> 英文 </th></tr><tr> <td> 上 </td><td> 45 </td><td> 67 </td><td> 80 </td></tr><tr> <td> 下 </td><td>  </td><td>  </td><td>  </td></tr></table>"
app.run()