from flask import Flask, render_template, redirect, url_for, request
from data import get_data, get_result_list

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        city = request.form["search"]
        return redirect(url_for("results", city=city))
    else:
        return render_template("home.html")

@app.route("/9<city>")
def results(city):
    return render_template("results.html", city=city, incidents=get_result_list(get_data(), desired_city=city))


if __name__ == "__main__":
    app.run(debug=True, port=8000)
