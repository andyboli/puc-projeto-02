import inquirer
from inquirer.themes import GreenPassion

from controller import reader
from view import register_menu, utils


parameters_menu_choices = {
    "clients_qnt": reader.read_text(
        "menu_clients_qnt"),
    "orders_avg": reader.read_text(
        "menu_orders_avg"),
    "avg_ticket": reader.read_text(
        "menu_avg_ticket"),
}


def build_parameters_menu():
    utils.build_register_menu_header()
    reader.show_text('menu_resgiter_params')
    utils.menu_state['parameters'] = inquirer.prompt(
        list(map(lambda key, value: inquirer.Text(
            key,
            message=value,
            validate=utils.validate_number,
        ), parameters_menu_choices.keys(), parameters_menu_choices.values())),
        theme=GreenPassion())
    return register_menu.build_register_menu()
