from flask import Flask, render_template, redirect, url_for, request
from data import get_data

app = Flask(__name__)


def get_result_list(data: list[dict], desired_city) -> str:
    result = []
    for incident in data:
        if incident["city"] == desired_city:
            result.append(incident)
        else:
            continue

    return result


@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        city = request.form["search"]
        return redirect(url_for("results", city=city))
    else:
        return render_template("index.html")

@app.route("/9<city>")
def results(city):
    return render_template("results.html", city=city, incidents=get_result_list(get_data(), desired_city=city))


if __name__ == "__main__":
    app.run(debug=True, port=8000)
