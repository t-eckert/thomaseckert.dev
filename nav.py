class Nav:
    ITEMS = ["links", "essays", "about"]

    def __init__(self):
        pass

    def get_without_active(self) -> str:
        return "\n".join(self.wrap_in_not_active(item) for item in ITEMS)

    def get_with_active(item: str) -> str:
        return ""

    def set_active(item: str) -> list:
        pass

    def wrap_in_not_active(item: str) -> str:
        return f'<a class="nav-item nav-link" href="/{item}">{item}</a>'

    def wrap_in_active(item: str) -> str:
        return f'<a class="nav-item nav-link active" href="/{item}">{item} <span class="sr-only">(current)</span></a>'

