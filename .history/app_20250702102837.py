from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/pre")
def pre_home():
    return render_template("pre.html")  # ✅ Matches template filename

@app.route("/grade3")
def grade3_home():
    return render_template("grade3.html")  # ✅ Matches template filename

@app.route("/grade8")
def grade8_home():
    return render_template("grade8.html")  # ✅ Matches template filename

if __name__ == "__main__":
    app.run(debug=True)

