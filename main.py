from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/pest")
def pest():
    return render_template("pest.html")

@app.route("/swot")
def swot():
    return render_template("swot.html")

@app.route("/roadmap")
def roadmap():
    return render_template("roadmap.html")

if __name__ == "__main__":
    print("=== СЕРВЕР ЗАПУЩЕН ===")
    print("http://127.0.0.1:5000")
    app.run()