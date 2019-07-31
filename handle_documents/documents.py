from flask import url_for

with open("handle_documents/essays/basketball-for-nerds.html", "r") as f:
    basketball = f.read()

ESSAYS = {
    "an-essay-title": {
        "title": "An Essay Title",
        "date": "3 July 2019",
        "url": "Essays/an-essay-title",
        "description": "This is an essay about a topic that relates ideas in a unique way.",
        "body": "<p>This is an essay about a topic that relates ideas in a unique way</p>",
        "category": "Essay",
        "classes": "card-essay",
    },
    "basketball-for-nerds": {
        "title": "Basketball for Nerds",
        "date": "10 April 2019",
        "url": "Essays/basketball-for-nerds",
        "body": basketball,
        "description": "Exploring statistics with Python.",
        "readTime": "4 min read",
        "category": "Essay",
        "classes": "card-essay",
    },
}

LINKS = {
    "detecting-emotions-with-azure-cognitive-services": {
        "title": "Detecting Emotion with Azure Cognitive Services",
        "date": "6 April 2019",
        "url": "https://github.com/t-eckert/detecting-emotion-with-azure-cognitive-services-en",
        "description": "Use Azure Cognitive Services to detect faces in an image and their dominant emotion.",
        "category": "Repository",
        "classes": "card-code",
    },
    "copy-codepy-to-circuitpy-on-macos": {
        "title": "Copy <code>code.py</code> to CIRCUITPY on MacOS",
        "date": "2 April 2019",
        "url": "https://gist.github.com/t-eckert/66ca8f83f35aff64fbe37326ffdb440f",
        "description": "This script deploys code from your working directory to an Adafruit CircuitPlayground Express",
        "category": "Repository",
        "classes": "card-code",
    },
}

COLLECTIONS = {"Essays": ESSAYS, "Links": LINKS}
