import sys

def smallest_number(number1, number2, number3):
    smallest_number = sys.maxsize
    
    if number1 < smallest_number:
        smallest_number = number1
        if number2 < smallest_number:
            smallest_number = number2
            
            if number3 < smallest_number:
                smallest_number = number3
    return smallest_number

def largest_number(numberOne, numberTwo, numberThree):
    largest_number = sys.maxsize
    
    if numberOne > largest_number:
        largest_number = numberOne
        
        if numberTwo > largest_number:
            largest_number = numberTwo
            
            if number3 > largest_number:
                largest_number = number3
    return largest_number
        