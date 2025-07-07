from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/monday")
def monday():
    return render_template("monday.html")

@app.route("/tuesday")
def tuesday():
    return render_template("tuesday.html")

if __name__ == "__main__":
    app.run(debug=True)

