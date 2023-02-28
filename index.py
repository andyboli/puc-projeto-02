import inquirer

from controller.orchestrator import restart_app, start_app


questions = [
    inquirer.List('leave',
                  message="Kill the program?",
                  choices=['Yes', 'No'],
                  ),
]


if __name__ == "__main__":
    try:
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
