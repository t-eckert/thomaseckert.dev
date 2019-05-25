import json
from pathlib import Path
from dataclasses import dataclass

EMOJI = {"article": "✏️"}


def set_emoji(kind: str) -> str:
    return EMOJI[kind]


@dataclass
class Post:
    name: str
    kind: str
    url: str


def from_json(json_object):
    name = json_object.get("name")
    kind = json_object.get("kind")
    url = json_object.get("url")
    return Post(name, kind, url)


cwd = Path.cwd()

with open(cwd / "post_catcher" / "posts.json", "r") as f:
    posts_json = json.load(f)

posts = [from_json(post) for post in posts_json]
print(posts)
