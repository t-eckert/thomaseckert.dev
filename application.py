from flask import Flask, render_template, url_for
from post_catcher import posts

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html", posts=posts)

