import inquirer
from inquirer.themes import GreenPassion

from controller import reader
from view import register_menu, utils


monthly_transactions_menu_choices = {
    "monthly_transactions_amount": reader.read_text(
        "menu_monthly_transactions_amount"),
    "monthly_transactions_rental": reader.read_text(
        "menu_monthly_transactions_rental"),
    "monthly_transactions_salaries": reader.read_text(
        "menu_monthly_transactions_salaries"),
    "monthly_transactions_maintenance": reader.read_text(
        "menu_monthly_transactions_maintenance")
}


def build_monthly_transactions_menu() -> str:
    utils.build_register_menu_header()
    reader.show_text('menu_resgiter_monthly_transactions')
    utils.menu_state["monthly_transactions"] = inquirer.prompt(
        list(map(lambda key, value: inquirer.Text(
            key,
            message=value,
            validate=utils.validate_number,
        ), monthly_transactions_menu_choices.keys(), monthly_transactions_menu_choices.values())),
        theme=GreenPassion())
    return register_menu.build_register_menu()
