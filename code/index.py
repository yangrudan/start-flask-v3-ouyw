from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", name='index')

@app.route("/企业简介")
def 企业简介():
    return "企业简介"

@app.route("/下属企业")
def 企业简介():
    return "下属企业"

@app.route("/产品中心")
def 企业简介():
    return "产品中心"

@app.route("/主营业务")
def 企业简介():
    return "主营业务"

@app.route("/企业文化")
def 企业简介():
    return "企业文化"

@app.route("/企业招聘")
def 企业简介():
    return "企业招聘"

@app.route("/联系我们")
def 企业简介():
    return "联系我们"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000)
