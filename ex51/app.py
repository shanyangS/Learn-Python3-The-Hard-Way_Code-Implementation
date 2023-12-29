from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/hello', methods=['POST', 'GET'])
def index():
    greeting = "Hello World"

    if request.method == "POST":
        name = request.form['name']
        greet = request.form['greet']
        greeting = f"{greet}, {name}"
        return render_template("index.html", greeting=greeting)
    else:
        return render_template("hello_form.html")
# 当一个表单被提交时，如果该表单的 method 属性被设置为 'POST'，那么发送到服务器的请求就是一个 'POST' 请求。在您的 Flask 应用中，如果您有一个 HTML 表单（假设在 hello_form.html 中）设置为 method='POST'，那么当用户填写该表单并点击提交按钮时，会向服务器发送一个 'POST' 请求
# 通常，当用户直接访问一个 URL（例如，通过在浏览器地址栏中输入 URL 或点击一个链接）时，浏览器会发送一个 'GET' 请求。在 Flask 应用中，如果 request.method 不是 'POST'，那通常意味着它是一个 'GET' 请求。在这种情况下，不涉及表单提交，而是简单地请求页面内容。

if __name__ == "__main__":
    app.run()