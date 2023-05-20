# Create class
class UserInterface:
# Make an input method
    def first_number_input(self):
        first_number = float(input("Enter the first number: "))
        return first_number
    def second_number_input(self):
        second_number = float(input("Enter the second number: "))
        return second_number
# Make a retry method
    def retry(self):
        while True:
            response = input("Do you want to retry? (y/n) ").lower
            if response == "y":
                return True
            elif response == "n":
                print("Thank you")
                return False
            else:
                print("Invalid response, please enter Y or N only")
            