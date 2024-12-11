class Note:
    def __init__(self, title: str, desc: str, tags: list) -> None:
        self.title: str = title
        self.desc: str = desc
        self.tags: list = tags


def main() -> None:
    print("Type 'c' to create a note")
    notes: list = []
    while True:
        cmd: str = input("> ")

        if cmd.lower()[0] == "c":
            title: str = input("Enter the note title: ")
            desc: str = input("Enter the note description: ")
            tags_str: str = input("Enter tags separated by spaces: ")
            tags: list = tags_str.split()

            notes.append(create_note(title=title, desc=desc, tags=tags))
            continue

        elif cmd.lower()[0] == "l":
            list_notes(notes)
            continue
        elif cmd.lower()[0] == "q":
            break


def create_note(
    title: str = "Untitled Note", desc: str = "No description provided", tags: list = []
) -> Note:

    note = Note(title, desc, tags)
    return note


def list_notes(notes: list) -> None:
    for note in range(len(notes)):
        print(notes[note])


if __name__ == "__main__":
    main()
