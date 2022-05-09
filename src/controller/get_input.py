from check_input import *
def get_input():
    while 1:
        input_str = input("Enter email ID, order ID or phone number: ")
        
        if check_input(input_str)[0]:
            return check_input(input_str)[1]
        else:
            print("Enter valid input.")
def send_input():
    pass

print(get_input())
