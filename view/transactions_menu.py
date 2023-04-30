import inquirer
from inquirer.themes import GreenPassion

from controller import reader
from view import register_menu, utils


transactions_menu_choices = {
    "transactions_amount": reader.read_text(
        "menu_transactions_amount"),
    "transactions_rental": reader.read_text(
        "menu_transactions_rental"),
    "transactions_salaries": reader.read_text(
        "menu_transactions_salaries")
}


def build_transactions_menu() -> str:
    utils.build_register_menu_header()
    reader.show_text('menu_resgiter_transactions')
    utils.menu_state["transactions"] = inquirer.prompt(
        list(map(lambda key, value: inquirer.Text(
            key,
            message=value,
            validate=utils.validate_number,
        ), transactions_menu_choices.keys(), transactions_menu_choices.values())),
        theme=GreenPassion())
    return register_menu.build_register_menu()
