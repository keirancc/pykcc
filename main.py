class Note:
    def __init__(self, title: str, desc: str, tags: list) -> None:
        self.title = title
        self.desc = desc
        self.tags = tags


def main() -> None:
    pass


def create_note(
    title: str = "Untitled Note", desc: str = "No description provided", tags: list = []
):

    note = Note(title, desc, tags)
    return note


def list_notes(notes: dict) -> None:
    for note in enumerate(notes):
        print(note)


if __name__ == "__main__":
    main()
