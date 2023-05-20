from calculator_functions import Calculator
from user_interface import UserInterface
from style import Styling

header = Styling()
user_input = UserInterface()
calculator_initialize = Calculator()

while True:
    operation_name, operation_function = user_input.operation_picker()
    print(f"You are now using \033[1;32m{operation_name}\033[0m")


    first_number = user_input.first_number_input()
    second_number = user_input.second_number_input()
    try:
        print(f"\033[1;34mResult: {operation_function(first_number,second_number)}\033[0m")
    except ZeroDivisionError:
        print("\033[1;31mError: division by zero!\033[0m")
        continue
    response = user_input.retry()
    if response == False:
        break