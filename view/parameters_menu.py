import inquirer
from inquirer.themes import GreenPassion

from controller import reader
from view import register_menu, utils


parameters_menu_choices = {
    "profit_percentage": reader.read_text(
        "menu_params_profit_percentage"),
    "clients_qnt": reader.read_text(
        "menu_params_clients_qnt"),
    "orders_avg": reader.read_text(
        "menu_params_orders_avg"),
    "avg_ticket": reader.read_text(
        "menu_params_avg_ticket"),
}

choose_param_key = 'choose_param_key'


def build_parameters_menu():
    utils.build_register_menu_header()
    reader.show_text('menu_resgiter_params')
    choosed_param = inquirer.prompt([inquirer.List(choose_param_key, message=reader.read_text(
        "menu_choose_params"), choices=parameters_menu_choices.values())])[choose_param_key]
    utils.menu_state['parameters'] = inquirer.prompt(
        list(map(lambda item: inquirer.Text(
            name=item[0],
            message=item[1],
            validate=utils.validate_number,
        ), list(filter(lambda item: item[1] != choosed_param, parameters_menu_choices.items())))),
        theme=GreenPassion())
    return register_menu.build_register_menu()
