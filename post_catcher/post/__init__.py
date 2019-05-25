class Post:
    EMOJI = {"article": "✏️", "repository": "🗄", "gist": "📓"}

    def __init__(self, name: str, kind: str, url: str, description: str):
        self.name = name
        self.kind = kind
        self.url = url
        self.description = description
        self.set_emoji()

    def set_emoji(self) -> str:
        try:
            self.emoji = self.EMOJI[self.kind]
        except KeyError:
            self.emoji = ""


def from_json(json_object):
    name = json_object.get("name")
    kind = json_object.get("kind")
    url = json_object.get("url")
    description = json_object.get("description")
    return Post(name, kind, url, description)
