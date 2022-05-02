def decode_input(input_str):
    flag = "email"
    
    if "@" in input_str:
        return input_str, flag
    else:
        if len(input_str) == 10:
            flag = "phone"
        elif len(input_str<=7):
            flag = "order"
        else:
            return "Please enter a valid input. Phone number needs to have 10 digits"

        return int(input_str), flag


