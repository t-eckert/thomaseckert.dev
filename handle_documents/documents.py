from flask import url_for

ESSAYS = {
    "an-essay-title": {
        "title": "An Essay Title",
        "date": "3 July 2019",
        "url": "essays/an-essay-title",
        "description": "This is an essay about a topic that relates ideas in a unique way.",
        "body": "<p>This is an essay about a topic that relates ideas in a unique way</p>",
    },
    "basketball-for-nerds": {
        "title": "Basketball for Nerds",
        "date": "10 April 2019",
        "url": "https://dev.to/teckert/basketball-for-nerds-5bf0",
        "description": "Exploring statistics with Python.",
    },
}

LINKS = {
    "detecting-emotions-with-azure-cognitive-services": {
        "title": "Detecting Emotion with Azure Cognitive Services",
        "date": "6 April 2019",
        "url": "https://github.com/t-eckert/detecting-emotion-with-azure-cognitive-services-en",
        "description": "Use Azure Cognitive Services to detect faces in an image and their dominant emotion.",
        "cardClass": "card-code",
    },
    "copy-codepy-to-circuitpy-on-macos": {
        "title": "Copy `code.py` to CIRCUITPY on MacOS",
        "date": "2 April 2019",
        "url": "https://gist.github.com/t-eckert/66ca8f83f35aff64fbe37326ffdb440f",
        "description": "This script deploys code from your working directory to an Adafruit CircuitPlayground Express",
        "cardClass": "card-code",
    },
}

COLLECTIONS = {"Essays": ESSAYS, "Links": LINKS}
