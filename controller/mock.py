from faker import Faker
from view import utils
from datetime import datetime
import numpy
import random
from functools import reduce
import pandas as pd

from model import api
from view.utils import menu_state
from view.monthly_transactions_menu import monthly_transactions_menu_choices

fake = Faker(locale='pt_PT')

genders = {
    "M": "Masculino",
    "F": "Feminino",
    "NB": "Não Binário",
    "O": "Outro"
}


def mock_clients(clients_qnt: int):
    clients = []
    for _ in range(clients_qnt):
        gender = numpy.random.choice(
            [genders["M"], genders["F"], genders["NB"], genders["O"]], p=[0.4, 0.5, 0.08, 0.02]) if fake.boolean(chance_of_getting_true=60) else None
        name = fake.name_female() if gender == genders["F"] else fake.name_male(
        ) if gender == genders["M"] else fake.name_nonbinary() if gender == genders["NB"] else fake.name()
        address_qnt = random.randint(0, 3)
        print(address_qnt)
        clients.append({
            "name": name,
            "email": fake.unique.email(),
            "birthdate": fake.date_of_birth(maximum_age=100).strftime("%d/%m/%Y"),
            "password": fake.password(length=6),
            "gender": gender,
            "address": mock_address(address_qnt) if bool(address_qnt) else None
        })
    return clients


def mock_address(address_qnt: int):
    addresses = []
    for _ in range(address_qnt):
        address = fake.street_address()
        addresses.append({
            "address": address,
            "alias": fake.text(max_nb_chars=6)
        })
    return addresses


def mock_transactions():
    transactions_state: dict = menu_state['monthly_transactions']
    meals_state: list = menu_state['meals']
    date = datetime.now().replace(day=1)
    code = None
    transactions = []
    for key, value in transactions_state.items():
        name = monthly_transactions_menu_choices[key]
        transactions.append(
            (value, name, date, code))
    meals_total_value = 0
    for meal_state in meals_state:
        meals_total_value += int(meal_state['costPrice']) * \
            int(meal_state['currentQuantity'])
    transactions.append(
        (meals_total_value, "Initial Meal Stock", date, code))
    return transactions


def mock_meals():
    meals_state: list = menu_state['meals']
    meals = []
    for meal_state in meals_state:
        meal = api.get_meal_details(meal_state['mealId'])
        meals.append((int(meal['mealId']), meal['name'], float(meal_state['sellerPrice']),
                     meal['instructions'], meal['area'], meal['category'], meal['imageUrl']))
    return meals


def mock_meals_stock():
    meals_state: list = menu_state['meals']
    meals_stock = []
    for meal_state in meals_state:
        meals_stock.append((int(meal_state['mealId']), int(meal_state['currentQuantity']), int(
            meal_state['lowestQuantity']), float(meal_state['costPrice'])))
    return meals_stock


def mock_data():
    """ return {"clients": mock_clients(parameters['clients_qnt'])} """


""" 
    get_current_profit
    
    incomes =
     
    initial_amount = transactions_amount - transactions_rental - transactions_salaries - transactions_maintenance 
    
    profit_percentage = 
    
    
      "transactions_maintenance": "Maintanance",
  "transactions_amount": "Initial Amount",
  "transactions_rental": "Rental",
  "transactions_salaries": "Employees Salaries Amount"

  "profit_percentage": "Expectativa de Porcentagem de Lucro Mensal",
  "clients_qnt": "Quantidade de Clientes",
  "orders_avg": "Média de Pedidos por Cliente",
  "avg_ticket": "Ticket Médio por Pedido", 
  
  
  
  
  """
