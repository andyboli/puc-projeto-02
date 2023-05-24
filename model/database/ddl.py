import mysql.connector
from mysql.connector import (errorcode, MySQLConnection)

from controller import reader
from model.database.constants import (
    CONNECTION_CONFIG, DB, DB_CREATE_QUERY, DB_DROP_QUERY)
from model.database.connection import get_connection


def create_database(db_name: str = DB, db_query=DB_CREATE_QUERY):
    """Creates a database in the MySQLConnection created by open_connection_iterator.

    Args:
        db_name (str, optional): Database name. Defaults to DB.
        db_query (str, optional): Create database query. Defaults to DB_CREATE_QUERY.

    Returns:
        success (str): Success message.
        error (str): Error message.
    """
    connection, _, _ = next(get_connection)
    success = ''
    error = ''
    try:
        cursor = connection.cursor()
        cursor.execute(db_query)
        connection.database = db_name
        cursor.close()
        success = reader.read_text(
            'create_database_success').format(db_name)
    except mysql.connector.Error as err:
        error = reader.read_text(
            'create_database_error').format(db_name, err)
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
    connection, _, _ = next(get_connection)
    success = ''
    error = ''
    try:
        cursor = connection.cursor()
        cursor.execute(db_query.format(db_name))
        cursor.close()
        success = reader.read_text(
            'drop_database_success').format(db_name)
    except mysql.connector.Error as err:
        error = reader.read_text(
            'drop_database_error').format(db_name, err)
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
    connection, _, _ = next(get_connection)
    success = ''
    error = ''
    try:
        cursor = connection.cursor()
        cursor.execute(table_query)
        cursor.close()
        success = reader.read_text(
            'create_table_success').format(table_name)
    except mysql.connector.Error as err:
        error = reader.read_text(
            'create_table_error').format(table_name, err)
    finally:
        return success, error


def insert_table(data: list, table_name: str, table_query: str):
    """Populates a table in the MySQLConnection created by open_connection_iterator

    Args:
        data (list): Data to be populated in table
        table_name (str, optional): Table name. Defaults to PUC_DB_HOMELESS.
        table_query (str, optional): Create table query. Defaults to PUC_DB_HOMELESS_INSERT_QUERY.

    Returns:
        success (str): Success message.
        error (str): Error message.
    """
    connection, _, _ = next(get_connection)
    success = ''
    error = ''
    try:
        cursor = connection.cursor()
        cursor.executemany(table_query, data)
        connection.commit()
        cursor.close()
        success = reader.read_text('insert_table_success').format(
            cursor.rowcount, table_name)
    except mysql.connector.Error as err:
        error = reader.read_text(
            'insert_table_error').format(table_name, err)
    finally:
        return success, error
