from log import error_enter
from menu import input_contact_menu_choice


def choice():
    try:
        choice1 = int(input('Выберите пункт меню: '))
    except ValueError:
        print('Неверный пункт меню')
        error_enter()
        return input_contact_menu_choice()