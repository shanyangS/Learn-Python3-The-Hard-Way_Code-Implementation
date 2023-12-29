from flask import Flask
from flask import render_template

app = Flask(__name__)
# 在Web开发中，“根目录”通常指的是网站的主页, 这里的@是装饰器
@app.route('/')
def index():
    greeting = "Hello World"
    return render_template("index.html", greeting=greeting)

if __name__ == "__main__":
    app.run()