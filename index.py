""" from controller.orchestrator import restart_app, start_app """
from view import main_menu
from controller import mock


if __name__ == "__main__":
    print(mock.mock_clients(2))
    """ main_menu.build_main_menu() """
