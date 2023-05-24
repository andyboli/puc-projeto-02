import inquirer
import os
from pprint import pprint

from controller import reader
from view import utils

menu_state = {
    'meals': [],
    'parameters': {},
    'monthly_transactions': {},
    'created': True
}


def build_menu_header():
    if not utils.menu_state['created']:
        os.system("cls")
    reader.show_text('menu_title')


def build_register_menu_header():
    build_menu_header()
    reader.show_text('menu_register_restaurant')
    pprint(menu_state, indent=2)
    print("\n")


def validate_number(_, current: str):
    try:
        float(current)
        return True
    except:
        raise inquirer.errors.ValidationError(
            "", reason=reader.read_text(
                "menu_number_error"))
