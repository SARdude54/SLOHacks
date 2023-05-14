from flask import Flask, render_template, redirect, url_for
from data import get_data

app = Flask(__name__)


def results(data: list[dict]) -> str:
    result_html = ""
    for incident in data:
        result_html += f"""
        
        <div>
        
        <p>Name: {incident["name"]}</p>

        </div>
        
        """

    return result_html


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/9<city>")
def results(city):
    return render_template("results.html", city=city, result_list=results(get_data()))


if __name__ == "__main__":
    app.run(debug=True, port=8000)
