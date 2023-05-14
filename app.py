from flask import Flask, render_template, redirect, url_for
from data import get_data

app = Flask(__name__)

print(get_data()[1])

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True);

