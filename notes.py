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
        print(make_separator())
        print()


def get_note_by_number(notes: list[dict], number: int)-> dict | None:
    if 1 <= number <= len(notes):
        return notes[number - 1]
    return None


def print_note(note: dict)->None:
    print(f"Заголовок: {note['title']}")
    print(f"Текст: {note['text']}")
    print(f"Теги: {", ".join(note['tags'])}")
    print(f"Створено: {note['created_at']}")
    print(make_separator())


def select_note()-> tuple[list[dict], dict, int] | None:
    notes = load_notes()

    if not notes:
        print("Нотаток ще немає.")
        return

    list_notes()

    number = int(input("Вкажіть номер нотатки: "))

    note = get_note_by_number(notes, number)
    if not note:
        print("Нотатки за таким номером не існує.")
        return

    return notes, note, number


def view_note()-> None:
    result = select_note()

    if not result:
        return

    _, note, _ = result

    print_note(note)


def delete_note()-> None:
    result = select_note()

    if not result:
        return

    notes, note, number = result

    answer = input(
        f"Ви впевнені, що бажаєте видалити нотатку № {number}? ('y/n'): "
            ).strip().lower()

    while answer not in ("y", "n"):
        answer = input("Неправильний ввід! " 
                        "Введіть або y або n: ").strip().lower()

    if answer == 'n':
        return

    notes.remove(note)
    save_notes(notes)

    print(f"Нотатка № {number} успішно видалена.")


def edit_note()-> None:
    result = select_note()

    if not result:
        return

    notes, note, number = result


    print_note(note)

    new_title = input(f"Новий заголовок [{note['title']}]: ").strip()

    if new_title:
        note['title'] = new_title

    new_text = input(f"Новий текст [{note['text']}]: ").strip()

    if new_text:
        note['text'] = new_text

    current_tags = ", ".join(note['tags'])
    new_tags = input(f"Нові теги [{current_tags}]: ").strip()

    if new_tags:
        note["tags"] = parse_tags(new_tags)

    save_notes(notes)

    print(f"Нотатку № {number} успішно оновлено.")
