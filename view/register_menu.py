import inquirer
from inquirer.themes import GreenPassion

from controller import reader
from view import main_menu, meals_menu, parameters_menu, transactions_menu, utils


register_menu_choices = {
    "resgiter_transactions": reader.read_text(
        "menu_resgiter_transactions"),
    "resgiter_meals": reader.read_text(
        "menu_resgiter_meals"),
    "resgiter_params": reader.read_text(
        "menu_resgiter_params"),
    "change_transactions": reader.read_text(
        "menu_change_transactions"),
    "change_meals": reader.read_text(
        "menu_change_meals"),
    "change_params": reader.read_text(
        "menu_change_params"),
    "create_restaurant": reader.read_text(
        "menu_create_restaurant"),
}


def filter_register_menu_choice(choice: str):
    hasMeals = bool(utils.menu_state['meals'])
    hasParams = bool(utils.menu_state['parameters'])
    hasTransactions = bool(utils.menu_state['transactions'])
    if choice == register_menu_choices["resgiter_transactions"]:
        return False if hasTransactions else True
    if choice == register_menu_choices["resgiter_meals"]:
        return False if hasMeals else True
    if choice == register_menu_choices["resgiter_params"]:
        return False if hasParams else True
    if choice == register_menu_choices["change_transactions"]:
        return True if hasTransactions else False
    if choice == register_menu_choices["change_meals"]:
        return True if hasMeals else False
    if choice == register_menu_choices["change_params"]:
        return True if hasParams else False
    if choice == register_menu_choices["create_restaurant"]:
        return True if hasTransactions and hasMeals and hasParams else False


register_menu_key = 'register_menu_choices'


def build_register_menu() -> str:
    utils.build_register_menu_header()
    register_menu_current_choices = list(filter(
        lambda choice: filter_register_menu_choice(choice), register_menu_choices.values()))
    answers = inquirer.prompt(
        [inquirer.List(register_menu_key,
                       message=reader.read_text("menu_choose_action"),
                       choices=register_menu_current_choices)],
        theme=GreenPassion())
    answer = answers[register_menu_key]
    if answer == register_menu_choices["resgiter_transactions"] or answer == register_menu_choices["change_transactions"]:
        transactions_menu.build_transactions_menu()
    if answer == register_menu_choices["resgiter_meals"] or answer == register_menu_choices["change_meals"]:
        meals_menu.build_meals_menu()
    if answer == register_menu_choices["resgiter_params"] or answer == register_menu_choices["change_params"]:
        parameters_menu.build_parameters_menu()
    return main_menu.build_main_menu()
