from flask import Flask, render_template, url_for
from documents import get_document, get_cards

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("content/home.html", active_page="index")


@app.route("/about")
def about():
    return render_template("content/about.html", active_page="about")


@app.route("/assets")
def assets():
    return render_template("assets.html")


@app.route("/<collection>")
def browse(collection: str):
    return render_template(
        "content/browse.html", active_page=collection, collection=get_cards(collection)
    )


@app.route("/<collection>/<name>")
def read(collection: str, name: str):
    return render_template(
        "content/read.html",
        active_page=collection,
        document=get_document(collection, name),
    )


@app.route("/humans.txt")
def humans():
    return "Hello fellow human."


@app.route("/404")
def page_404():
    return render_template("content/404.html", active_page="home")

