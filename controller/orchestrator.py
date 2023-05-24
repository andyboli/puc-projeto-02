from controller import reader, mock
from model.database.connection import get_connection
from model.database.ddl import create_database, create_table, insert_table
from model.database.constants import (DB, DB_TRANSACTION, DB_TRANSACTION_CREATE_QUERY, DB_STOCK_ORDER, DB_STOCK_ORDER_CREATE_QUERY, DB_MEAL_STOCK, DB_MEAL_STOCK_CREATE_QUERY,
                                      DB_MEAL, DB_MEAL_CREATE_QUERY, DB_CLIENT, DB_CLIENT_CREATE_QUERY, DB_ADDRESS, DB_ADDRESS_CREATE_QUERY, DB_ORDER, DB_ORDER_CREATE_QUERY, DB_ORDER_MEAL, DB_ORDER_MEAL_CREATE_QUERY,
                                      DB_TRANSACTION_INSERT_QUERY, DB_MEAL_INSERT_QUERY, DB_MEAL_STOCK_INSERT_QUERY)
from view import utils, main_menu


def simulate_database_profit_percentage_iterator():

    transactions = mock.mock_transactions()
    print(transactions)
    """ yield '', reader.read_text('insert_table_start').format(transactions.size, DB_TRANSACTION), ''
    success, error = insert_table(
        table_name=DB_TRANSACTION, table_query=)
    yield success, '', error """


def create_tables_iterator():
    for table_name, table_query in [(DB_CLIENT, DB_CLIENT_CREATE_QUERY),
                                    (DB_ADDRESS, DB_ADDRESS_CREATE_QUERY),
                                    (DB_MEAL, DB_MEAL_CREATE_QUERY),
                                    (DB_ORDER, DB_ORDER_CREATE_QUERY),
                                    (DB_MEAL_STOCK, DB_MEAL_STOCK_CREATE_QUERY),
                                    (DB_ORDER_MEAL, DB_ORDER_MEAL_CREATE_QUERY),
                                    (DB_STOCK_ORDER, DB_STOCK_ORDER_CREATE_QUERY),
                                    (DB_TRANSACTION, DB_TRANSACTION_CREATE_QUERY)
                                    ]:
        yield '', reader.read_text('create_table_start').format(table_name), ''
        success, error = create_table(
            table_name=table_name, table_query=table_query)
        yield success, '', error


create_tables = create_tables_iterator()


def create_restaurant_iterator():
    """Start the app.

    Yields:
        success (str): Success message.
        loading (str): Loading message.
        error (str): Error message.
    """
    yield reader.read_text('open_connection_start'), '', ''
    _, success, error = next(get_connection)
    yield success, '', error

    yield '', reader.read_text('create_database_start').format(DB), ''
    success, error = create_database()
    yield success, '', error

    while True:
        try:
            success, loading, error = next(create_tables)
            if loading:
                print(loading)
            elif success:
                print(success)
            elif error:
                print(error)
        except StopIteration:
            break

    # Inserting Tables
    transactions = mock.mock_transactions()
    yield '', reader.read_text('insert_table_start').format(len(transactions), DB_TRANSACTION), ''
    success, error = insert_table(
        table_name=DB_TRANSACTION, table_query=DB_TRANSACTION_INSERT_QUERY, data=transactions)
    yield success, '', error

    meals = mock.mock_meals()
    yield '', reader.read_text('insert_table_start').format(len(meals), DB_MEAL), ''
    success, error = insert_table(
        table_name=DB_MEAL, table_query=DB_MEAL_INSERT_QUERY, data=meals)
    yield success, '', error

    meals_stock = mock.mock_meals_stock()
    yield '', reader.read_text('insert_table_start').format(len(meals_stock), DB_MEAL_STOCK), ''
    success, error = insert_table(
        table_name=DB_MEAL_STOCK, table_query=DB_MEAL_STOCK_INSERT_QUERY, data=meals_stock)
    yield success, '', error


create_restaurant_iterator_instance = create_restaurant_iterator()


def create_restaurant():
    try:

        while True:
            try:
                success, loading, error = next(
                    create_restaurant_iterator_instance)
                if loading:
                    print(loading)
                elif success:
                    utils.menu_state['created'] = True
                    print(success)
                elif error:
                    print(error)
            except StopIteration:
                return main_menu.build_main_menu()
    finally:
        """ while True:
            try:
                success, loading, error = next(restart_app)
                if loading:
                    print(loading)
                elif success:
                    print(success)
                elif error:
                    print(error)
            except StopIteration:
                break """


"""  

   



    



def restart_app_iterator():
    Calls drop_database and close_connection with default values.

    Yields:
        success (str): Success message.
        loading (str): Loading message.
        error (str): Error message.
    
    try:
        
        yield '', reader.read_text('drop_database_start').format(DB), ''
        success, error = drop_database()
        yield success, '', error 
        
        yield '', reader.read_text('close_connection_start'), ''
        success, error = close_connection()
        yield success, '', error
    except Exception as err:
        yield '', '', reader.read_text("restart_app_error").format(err)


restart_app = restart_app_iterator()


def create_restaurant():
    try:

        while True:
            try:
                success, loading, error = next(
                    create_restaurant_iterator_instance)
                if loading:
                    print(loading)
                elif success:
                    utils.menu_state['created'] = True
                    print(success)
                elif error:
                    print(error)
            except StopIteration:
                return main_menu.build_main_menu()
    finally:
        while True:
            try:
                success, loading, error = next(restart_app)
                if loading:
                    print(loading)
                elif success:
                    print(success)
                elif error:
                    print(error)
            except StopIteration:
                break


"""
