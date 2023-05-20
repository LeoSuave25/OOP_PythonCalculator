# Create class
class Calculator:
# Add Method
    def add(self,first_number,second_number):
        return first_number + second_number
# Subtract Method
    def subtract(self,first_number,second_number):
        return first_number - second_number
# Multiplication method
    def multiply(self,first_number,second_number):
        return first_number * second_number
# Division Method
    def divide(self,first_number,second_number):
        try:
            return first_number / second_number
        except ZeroDivisionError:
            print("\033[1;31mError: division by zero!\033[0m")