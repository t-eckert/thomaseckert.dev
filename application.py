from flask import Flask, render_template, url_for
from post_catcher import posts
from handle_documents import get_collection, get_document

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("content/home.html", active_page="Index")


@app.route("/About")
def about():
    return render_template("content/about.html", active_page="About")


@app.route("/assets")
def assets():
    return render_template("assets.html")


@app.route("/<collection>")
def browse(collection: str):
    return render_template(
        "content/browse.html",
        active_page=collection.capitalize(),
        collection=get_collection(collection),
    )


@app.route("/<collection>/<document>")
def read(collection: str, document: str):
    return render_template(
        "content/read.html",
        active_page=collection,
        document=get_document(collection, document),
    )


@app.route("/404")
def page_404():
    return render_template("content/404.html", active_page="home")

