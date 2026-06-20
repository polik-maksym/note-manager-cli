#
#
#
#
###############################################################################

from storage import load_notes, save_notes
from utils import generate_id, get_timestamp, parse_tags, make_separator

def create_note()-> None:
    print("\n=== Створення нотатки ===")

    title = input("Введіть заголовок: ").strip()
    text = input("Введіть текст нотатки: ").strip()
    tags_input = input("Введіть теги (через кому): ")

    tags = parse_tags(tags_input)

    if not title:
        print("Заголовок не може бути порожнім.")
        return

    if not text:
        print("Текст нотатки не може бути порожнім.")
        return

    notes = load_notes()
    new_id = generate_id()

    note = {
        "id": new_id,
        "title": title,
        "text": text,
        "tags": tags,
        "created_at": get_timestamp()
    }

    notes.append(note)
    save_notes(notes)

    print(f"Нотатку створено. ID: {new_id}")

def list_notes()-> None:
    notes = load_notes()
    if not notes:
        print("Нотаток поки немає.")
        return

    for index, note in enumerate(notes, start=1):
        print(f"{index}) Заголовок: {note['title']}")
        print(f"Текст: {note['text']}")
        print(make_separator(note['text'], len(note['text']), "-"))
        print()


def get_note_by_number(notes: list[dict], number: int)-> dict | None:
    if 1 <= number <= len(notes):
        return notes[number-1]
    return None
