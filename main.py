from calculator_functions import Calculator
from user_interface import UserInterface
from style import Styling
from add_UI_functions import UpdatedUserInterface

header = Styling()
user_input = UserInterface()
calculator_initialize = Calculator()
update_UI = UpdatedUserInterface()

while True:
    operation_name, operation_function = user_input.operation_picker()
    print(f"You are now using \033[1;32m{operation_name}\033[0m")


    first_number = user_input.first_number_input()
    second_number = user_input.second_number_input()
    try:
        update_UI.print_result(operation_function,first_number,second_number)
    except:
        pass
    response = user_input.retry()
    if response == False:
        break