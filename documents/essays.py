import requests

ESSAYS = {
    "basketball-for-nerds": {
        "title": "Basketball for Nerds",
        "date": "10 April 2019",
        "url": "essays/basketball-for-nerds",
        "body": requests.get(
            "https://thomaseckertdev.blob.core.windows.net/pages/basketball-for-nerds.min.html"
        ).text,
        "description": "Exploring statistics with Python.",
        "readTime": "4 min read",
        "classes": "card-essay",
    }
}
