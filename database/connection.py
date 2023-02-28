import mysql.connector
from mysql.connector import (errorcode, MySQLConnection)

from controller.reader import lang
from database.constants import (
    CONNECTION_CONFIG, DB, DB_CREATE_QUERY, DB_DROP_QUERY)


def open_connection():
    """Opens a connection to the MySQL server.

    Returns:
        connection (MySQLConnection): MySQL oppened connection.
        success (str): Success message.
        error (str): Error message.
    """
    connection = None
    success = ''
    error = ''
    try:
        connection: MySQLConnection = mysql.connector.connect(
            **CONNECTION_CONFIG)
        if not connection.is_connected():
            error = lang('open_connection_error').format(err)
        server_info = connection.get_server_info()
        success = lang('open_connection_success').format(server_info)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            error = lang('open_connection_crendentials_error')
        else:
            error = lang('open_connection_error').format(err)
    finally:
        return connection, success, error


def open_connection_iterator():
    """Calls open_connection once and returns the same connection each time called.

    Yields:
        connection (MySQLConnection): MySQL oppened connection.
        success (str): Success message.
        error (str): Error message.
    """
    connection, message, error = open_connection()
    while True:
        yield connection, message, error


connect_mysql = open_connection_iterator()


def close_connection():
    """Closes the MySQLConnection created by open_connection_iterator.

    Returns:
        success (str): Success message.
        error (str): Error message.
    """
    connection, _, _ = next(connect_mysql)
    success = ''
    error = ''
    try:
        if connection.is_connected():
            server_info = connection.get_server_info()
            connection.close()
            success = lang('close_connection_success').format(server_info)
        else:
            error = lang('close_connection_error').format(
                errorcode.ER_NO_DB_ERROR)
    except Exception as err:
        error = lang('close_connection_error').format(err)
    finally:
        connect_mysql.close()
        return success, error


def create_database(db_name: str = DB, db_query=DB_CREATE_QUERY):
    """Creates a database in the MySQLConnection created by open_connection_iterator.

    Args:
        db_name (str, optional): Database name. Defaults to DB.
        db_query (str, optional): Create database query. Defaults to DB_CREATE_QUERY.

    Returns:
        success (str): Success message.
        error (str): Error message.
    """
    connection, _, _ = next(connect_mysql)
    success = ''
    error = ''
    try:
        cursor = connection.cursor()
        cursor.execute(db_query)
        connection.database = db_name
        cursor.close()
        success = lang('create_database_success').format(db_name)
    except mysql.connector.Error as err:
        error = lang('create_database_error').format(db_name, err)
    finally:
        return success, error


def drop_database(db_name: str = DB, db_query=DB_DROP_QUERY):
    """Drops a database in the MySQLConnection created by open_connection_iterator.

    Args:
        db_name (str, optional): Database name. Defaults to DB.
        db_query (str, optional): Create database query. Defaults to DB_DROP_QUERY.

    Returns:
        success (str): Success message.
        error (str): Error message.
    """
    connection, _, _ = next(connect_mysql)
    success = ''
    error = ''
    try:
        cursor = connection.cursor()
        cursor.execute(db_query.format(db_name))
        cursor.close()
        success = lang('drop_database_success').format(db_name)
    except mysql.connector.Error as err:
        error = lang('drop_database_error').format(db_name, err)
    finally:
        return success, error


def create_table(table_name: str, table_query: str):
    """Creates a table in the MySQLConnection created by open_connection_iterator

    Args:
        table_name (str, optional): Table name.
        table_query (str, optional): Create table query.

    Returns:
        success (str): Success message.
        error (str): Error message.
    """
    connection, _, _ = next(connect_mysql)
    success = ''
    error = ''
    try:
        cursor = connection.cursor()
        cursor.execute(table_query)
        cursor.close()
        success = lang('create_table_success').format(table_name)
    except mysql.connector.Error as err:
        error = lang(
            'create_table_error').format(table_name, err)
    finally:
        return success, error
