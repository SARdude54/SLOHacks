from flask import Flask, render_template, redirect, url_for
from data import get_data

app = Flask(__name__)

<<<<<<< HEAD
print(get_data()[1])
=======
>>>>>>> c5574ebc8290d46a3396c7c9462c0cefa35ddea5

@app.route("/")
def home():
    return render_template("index.html")
<<<<<<< HEAD
=======

>>>>>>> c5574ebc8290d46a3396c7c9462c0cefa35ddea5

if __name__ == "__main__":
    app.run(debug=True, port=8000)
