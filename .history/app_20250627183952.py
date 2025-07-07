from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/pre")
def pre_home():
    return render_template("pre_home.html")

@app.route("/grade3")
def grade3_home():
    return render_template("grade3_home.html")

@app.route("/grade8")
def grade8_home():
    return render_template("grade8_home.html")

if __name__ == "__main__":
    app.run(debug=True)

