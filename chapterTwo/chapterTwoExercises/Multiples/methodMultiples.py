def function_multiples(divisor, number):
    """function that checks if first number is a multiple of the second
    number"""
    
    is_multiples = False
    if (number % divisor)  == 0:
        print("Is mutiple.")
        is_multiples = True
    else:
        print("Is not multiple.")
    return is_multiples
