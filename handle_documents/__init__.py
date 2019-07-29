from .documents import COLLECTIONS


def get_collection(collection: str) -> dict:
    return COLLECTIONS.get(collection).values()


def get_document(collection: str, document: str) -> dict:
    return COLLECTIONS.get(collection).get(document)
