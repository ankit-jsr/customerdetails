def check_input(input_str):
    if "@" in input_str and "." in input_str:
        #Check for email validity. Emails need to have @ and .
        return 1, input_str
    elif len(input_str) == 10 and int(input_str)>999999999:
        return 1, input_str
    elif len(input_str)>10 and input_str[0] == '+' and int(input_str)>0:
        inp = input_str[-10:]
        return 1, inp
    elif len(input_str) == 7 and int(input_str)>0:
        return 1, input_str
    else:
        return 0, 0


