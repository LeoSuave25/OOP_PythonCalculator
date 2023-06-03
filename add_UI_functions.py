from user_interface import UserInterface

class UpdatedUserInterface(UserInterface):
    def print_result(self,operation, first_number, second_number):
        result = operation(first_number,second_number)
        print("\033[1;34mResult: "+str(result)+"\033[0m")