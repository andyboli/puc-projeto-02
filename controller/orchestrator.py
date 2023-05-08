from controller import reader, mock
from database.connection import close_connection, connect_mysql, create_database, create_table, drop_database
from database.constants import (DB, DB_CLIENT, DB_CLIENT_CREATE_QUERY, DB_MEAL, DB_MEAL_CREATE_QUERY, DB_ORDER,
                                DB_ORDER_CREATE_QUERY, DB_ORDER_MEAL, DB_ORDER_MEAL_CREATE_QUERY, DB_MEAL_STOCK, DB_MEAL_STOCK_CREATE_QUERY, DB_STOCK_ORDER, DB_STOCK_ORDER_CREATE_QUERY, DB_TRANSACTION, DB_TRANSACTION_CREATE_QUERY)
from view import utils, main_menu


def create_restaurant_iterator():
    """Start the app.

    Yields:
        success (str): Success message.
        loading (str): Loading message.
        error (str): Error message.
    """
    mock.mock_data()
    yield reader.read_text('open_connection_start'), '', ''
    _, success, error = next(connect_mysql)
    yield success, '', error

    yield '', reader.read_text('create_database_start').format(DB), ''
    success, error = create_database()
    yield success, '', error

    yield '', reader.read_text('create_table_start').format(DB_CLIENT), ''
    success, error = create_table(
        table_name=DB_CLIENT, table_query=DB_CLIENT_CREATE_QUERY)
    yield success, '', error

    yield '', reader.read_text('create_table_start').format(DB_MEAL), ''
    success, error = create_table(
        table_name=DB_MEAL, table_query=DB_MEAL_CREATE_QUERY)
    yield success, '', error

    yield '', reader.read_text('create_table_start').format(DB_ORDER), ''
    success, error = create_table(
        table_name=DB_ORDER, table_query=DB_ORDER_CREATE_QUERY)
    yield success, '', error

    yield '', reader.read_text('create_table_start').format(DB_ORDER_MEAL), ''
    success, error = create_table(
        table_name=DB_ORDER_MEAL, table_query=DB_ORDER_MEAL_CREATE_QUERY)
    yield success, '', error

    yield '', reader.read_text('create_table_start').format(DB_MEAL_STOCK), ''
    success, error = create_table(
        table_name=DB_MEAL_STOCK, table_query=DB_MEAL_STOCK_CREATE_QUERY)
    yield success, '', error

    yield '', reader.read_text('create_table_start').format(DB_STOCK_ORDER), ''
    success, error = create_table(
        table_name=DB_STOCK_ORDER, table_query=DB_STOCK_ORDER_CREATE_QUERY)
    yield success, '', error

    yield '', reader.read_text('create_table_start').format(DB_TRANSACTION), ''
    success, error = create_table(
        table_name=DB_TRANSACTION, table_query=DB_TRANSACTION_CREATE_QUERY)
    yield success, '', error


create_restaurant_iterator_instance = create_restaurant_iterator()


def restart_app_iterator():
    """Calls drop_database and close_connection with default values.

    Yields:
        success (str): Success message.
        loading (str): Loading message.
        error (str): Error message.
    """
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


"""


""" try:
        while True:
            try:
                success, loading, error = next(start_app)
                if loading:
                    print(loading)
                elif success:
                    print(success)
                elif error:
                    print(error)
            except StopIteration:
                answers = inquirer.prompt(questions)
                if answers['leave'] == 'Yes':
                    break
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
