from calculator_functions import Calculator

class UpdatedCalculator(Calculator):
    def divide(self, first_number, second_number):
        try:
            return first_number / second_number
        except ZeroDivisionError:
            print("\033[1;31mError: division by zero!\033[0m")