import inquirer
from inquirer.themes import GreenPassion
import sys

from controller import reader
from view import register_menu, utils


main_menu_choices = {
    "register_restaurant": reader.read_text(
        "menu_register_restaurant"),
    "exit_app": reader.read_text(
        "menu_exit_app")
}

main_menu_key = 'main_menu_choices'


def build_main_menu() -> str:
    utils.build_menu_header()
    answers = inquirer.prompt(
        [inquirer.List(main_menu_key,
                       message=reader.read_text(
                           "menu_choose_action"),
                       choices=main_menu_choices.values())],
        theme=GreenPassion())
    answer = answers[main_menu_key]
    if answer == main_menu_choices["register_restaurant"]:
        return register_menu.build_register_menu()
    if answer == main_menu_choices["exit_app"]:
        return sys.exit()
