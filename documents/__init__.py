from .essays import ESSAYS
from .links import LINKS

CARDS = {"essays": ESSAYS, "links": LINKS}


def get_cards(collection: str) -> dict:
    return CARDS.get(collection).values()


def get_document(collection: str, name: str) -> dict:
    return CARDS.get(collection).get(name)
