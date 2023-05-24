import inquirer
from inquirer.themes import GreenPassion
import functools


from controller import reader
from model import api
from view import register_menu, utils


select_categories_key = 'select_categories'
select_meals_key = 'select_meals'


def join_meals(meals_list_A, meals_list_B):
    return meals_list_A + meals_list_B


def build_meals_menu():
    utils.build_register_menu_header()
    reader.show_text('menu_resgiter_meals')
    categories = api.get_meals_categories()
    selected_categories = inquirer.prompt(
        [inquirer.Checkbox(select_categories_key,
                           message=reader.read_text(
                               "menu_meals_categories"),
                           choices=categories)],
        theme=GreenPassion())[select_categories_key]
    meals = list(functools.reduce(join_meals,
                                  map(lambda category: api.get_meals_by_category(category),
                                      selected_categories)))
    meals_names = list(map(lambda meal: meal['name'], meals))
    selected_meals_names = inquirer.prompt(
        [inquirer.Checkbox(select_meals_key, message=reader.read_text(
            "menu_meals"), choices=meals_names)], theme=GreenPassion())[select_meals_key]
    selected_meals = list(
        filter(lambda meal: True if meal['name'] in selected_meals_names else False, meals))
    other_meals_fileds_choices = list(functools.reduce(join_meals, map(lambda meal: [inquirer.Text(
        "costPrice-" + meal['mealId'],
        message=reader.read_text(
            "menu_meals_cost_price").format(meal['name']),
        validate=utils.validate_number,
    ), inquirer.Text(
        "sellerPrice-" + meal['mealId'],
        message=reader.read_text(
            "menu_meals_seller_price").format(meal['name']),
        validate=utils.validate_number,
    )], selected_meals)))
    all_meals_fields_choices = [inquirer.Text(
        'meals_qnt',
        message=reader.read_text(
            "menu_meals_qnt"),
        validate=utils.validate_number),
        inquirer.Text(
        'meals_lowest_qnt',
        message=reader.read_text(
            "menu_meals_lowest_qnt"),
        validate=utils.validate_number
    )]
    answers = inquirer.prompt(
        [*other_meals_fileds_choices, *all_meals_fields_choices], theme=GreenPassion())
    filled_selected_meals = list(
        map(lambda meal: {**meal,
                          "sellerPrice": answers["sellerPrice-" + meal['mealId']],
                          "costPrice": answers["costPrice-" + meal['mealId']],
                          "currentQuantity": answers["meals_qnt"],
                          "lowestQuantity": answers["meals_lowest_qnt"]
                          }, selected_meals))
    utils.menu_state['meals'] = filled_selected_meals
    return register_menu.build_register_menu()
