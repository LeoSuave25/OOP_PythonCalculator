from calculator_functions import Calculator

class UserInterface:
    def __init__(self):
        self.calcu_operators = Calculator()
        self.operations = {
            1: ("Addition", self.calcu_operators.add),
            2: ("Subtraction", self.calcu_operators.subtract),
            3: ("Multiplication", self.calcu_operators.multiply),
            4: ("Division", self.calcu_operators.divide),
        }
# Make an input method
    def first_number_input(self):
        while True:
            try:
                first_number = float(input("Enter the first number: "))
                return first_number
            except ValueError:
                print(f"\033[1;31mInvalid input. Please enter a valid number.\033[0m")

    def second_number_input(self):
        while True:
            try:
                second_number = float(input("Enter the second number: "))
                return second_number
            except ValueError:
                print(f"\033[1;31mInvalid input. Please enter a valid number.\033[0m")
# Make a retry method
    def retry(self):
        while True:
            response = input("\033[1;33mDo you want to retry? (y/n) \033[0m").lower()
            if response == "y":
                return True
            elif response == "n":
                print("\033[1;32mThank You!\033[0m")
                print("\033[32m","="*100,"\033[m")
                return False
            else:
                print("\033[1;31mInvalid Response! Please enter a valid Letter.\033[0m")
# Make an operation picker
    def operation_picker(self):
        while True:
            print("Choose an operation:")
            for operation_num, (operation_name, _) in self.operations.items():
                print(f"({operation_num}) {operation_name}")

            while True:
                try:
                    operation = int(input("Enter 1 | 2 | 3 | 4: "))
                    if operation not in self.operations:
                        raise ValueError("\033[1;31mInvalid operation! Please enter a valid operation number (1-4).\033[0m")
                    break
                except ValueError as error:
                    print(error)

            operation_name, operation_function = self.operations[operation]
            return operation_name, operation_function