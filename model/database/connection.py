import mysql.connector
from mysql.connector import (errorcode, MySQLConnection)

from controller import reader
from model.database.constants import (
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
            error = reader.read_text('open_connection_error').format(err)
        server_info = connection.get_server_info()
        success = reader.read_text(
            'open_connection_success').format(server_info)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            error = reader.read_text('open_connection_crendentials_error')
        else:
            error = reader.read_text('open_connection_error').format(err)
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


get_connection = open_connection_iterator()


def close_connection():
    """Closes the MySQLConnection created by open_connection_iterator.

    Returns:
        success (str): Success message.
        error (str): Error message.
    """
    connection, _, _ = next(connection)
    success = ''
    error = ''
    try:
        if connection.is_connected():
            server_info = connection.get_server_info()
            connection.close()
            success = reader.read_text(
                'close_connection_success').format(server_info)
        else:
            error = reader.read_text('close_connection_error').format(
                errorcode.ER_NO_DB_ERROR)
    except Exception as err:
        error = reader.read_text('close_connection_error').format(err)
    finally:
        return success, error
