def get_input():
    while 1:
        input_str = input("Enter email ID, order ID or phone number")
        if len(input_str) == 7 or len(input_str) == 10 or "@" in input_str:
            return input_str
        else:
            print("Enter valid input")

    


