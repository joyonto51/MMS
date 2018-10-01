def print_int_as_str(number):
    return str(number)

def print_int(my_function, number):
    print(type(my_function(number)))
    return

print_int(print_int_as_str,130)
