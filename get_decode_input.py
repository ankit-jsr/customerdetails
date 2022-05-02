def get_decode_input():
    flag = "email"
    input_str = input("Enter email ID, order ID or phone number")
    if "@" in input_str:
        return input_str
    else:
        if len(input_str)>7:
            flag = "phone"
        else:
            flag = "order"

        return int(input_str), flag
    


