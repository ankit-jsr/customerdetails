def decode_input(input_str):
    
    
    if "@" in input_str and "." in input_str:
        flag = "email"
    else:
        if len(input_str) == 10:
            flag = "phone"
        elif len(input_str)<=7:
            flag = "order"
        
        return int(input_str), flag


