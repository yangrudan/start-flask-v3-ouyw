from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", name='index')

@app.route("/企业简介")
def 企业简介():
    return "企业简介"

@app.route("/news")
def news():
    return "latest news"



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000)
