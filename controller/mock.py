from faker import Faker
from view import utils
from datetime import datetime
import numpy
import random

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


def mock_data():
    parameters = utils.menu_state['parameters']
    utils.mocked_data = {"clients": mock_clients(parameters['clients_qnt'])}
    print(utils.mocked_data)
