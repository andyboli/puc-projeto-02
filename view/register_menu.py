import inquirer
from inquirer.themes import GreenPassion

from controller import reader, orchestrator
from view import main_menu, meals_menu, monthly_transactions_menu, parameters_menu, utils


register_menu_choices = {
    "resgiter_monthly_transactions": reader.read_text(
        "menu_resgiter_monthly_transactions"),
    "resgiter_meals": reader.read_text(
        "menu_resgiter_meals"),
    "resgiter_params": reader.read_text(
        "menu_resgiter_params"),
    "change_monthly_transactions": reader.read_text(
        "menu_change_monthly_transactions"),
    "change_meals": reader.read_text(
        "menu_change_meals"),
    "change_params": reader.read_text(
        "menu_change_params"),
    "create_restaurant": reader.read_text(
        "menu_create_restaurant"),
}


def filter_register_menu_choices(choice: str):
    hasMeals = bool(utils.menu_state['meals'])
    hasParams = bool(utils.menu_state['parameters'])
    hasMonthly_Transactions = bool(utils.menu_state['monthly_transactions'])
    if choice == register_menu_choices["resgiter_monthly_transactions"]:
        return False if hasMonthly_Transactions else True
    if choice == register_menu_choices["resgiter_meals"]:
        return False if hasMeals else True
    if choice == register_menu_choices["resgiter_params"]:
        return False if hasParams else True
    if choice == register_menu_choices["change_monthly_transactions"]:
        return True if hasMonthly_Transactions else False
    if choice == register_menu_choices["change_meals"]:
        return True if hasMeals else False
    if choice == register_menu_choices["change_params"]:
        return True if hasParams else False
    if choice == register_menu_choices["create_restaurant"]:
        return True if hasMonthly_Transactions and hasMeals and hasParams else False


register_menu_key = 'register_menu_choices'


def build_register_menu() -> str:
    utils.build_register_menu_header()
    register_menu_current_choices = list(filter(
        lambda choice: filter_register_menu_choices(choice), register_menu_choices.values()))
    answers = inquirer.prompt(
        [inquirer.List(register_menu_key,
                       message=reader.read_text(
                           "menu_choose_action"),
                       choices=register_menu_current_choices)],
        theme=GreenPassion())
    answer = answers[register_menu_key]
    if answer == register_menu_choices["resgiter_monthly_transactions"] or answer == register_menu_choices["change_monthly_transactions"]:
        monthly_transactions_menu.build_monthly_transactions_menu()
    if answer == register_menu_choices["resgiter_meals"] or answer == register_menu_choices["change_meals"]:
        meals_menu.build_meals_menu()
    if answer == register_menu_choices["resgiter_params"] or answer == register_menu_choices["change_params"]:
        parameters_menu.build_parameters_menu()
    if answer == register_menu_choices["create_restaurant"]:
        orchestrator.create_restaurant()
    return main_menu.build_main_menu()
