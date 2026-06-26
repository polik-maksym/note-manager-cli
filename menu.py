#
#
#
#
###############################################################################

import constants
from notes import create_note, delete_note, edit_note, list_notes, view_note




def main_menu()-> None:

    options = [
        (constants.CREATE_NOTE, "Створити нотатку"),
        (constants.LIST_NOTES,  "Переглянути всі нотатки"),
        (constants.VIEW_NOTE,   "Переглянути нотатку"),
        (constants.EDIT_NOTE,   "Редагувати нотатку"),
        (constants.DELETE_NOTE, "Видалити нотатку"),
        (constants.SEARCH,      "Пошук"),
        (constants.EXPORT,      "Експорт"),
        (constants.QUIT,        "Вихід"),
    ]

    print("\n=== Менеджер нотаток ===")
    for code, text in options:
        print(f"{code:<1}) {text}")

    choice = input("Виберіть дію: ").strip()

    actions = {
        constants.CREATE_NOTE: create_note,
        constants.LIST_NOTES: list_notes,
        constants.VIEW_NOTE: view_note,
        constants.EDIT_NOTE: edit_note,
        constants.DELETE_NOTE: delete_note,
        constants.QUIT: lambda: exit(),
    }

    action = actions.get(choice)

    #Перевірка валідності вводу
    if action:
        action()
    else:
        print("Невірний вибір.")

