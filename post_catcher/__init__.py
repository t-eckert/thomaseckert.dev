import json
from pathlib import Path
from . import post

cwd = Path.cwd()

with open(cwd / "post_catcher" / "posts.json", "r") as f:
    posts_json = json.load(f)

posts = [post.from_json(POST) for POST in posts_json]
