#
#
#
#
###############################################################################

import constants
from notes import create_note, list_notes




def main_menu()-> None:

    options = [
        (constants.CREATE_NOTE, "Створити нотатку"),
        (constants.LIST_NOTES,  "Переглянути всі нотатки"),
        (constants.VIEW_NOTE,   "Переглянути нотатку за ID"),
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
        constants.QUIT: lambda: exit(),
    }

    action = actions.get(choice)

    #Перевірка валідності вводу
    if action:
        action()
    else:
        print("Невірний вибір.")

