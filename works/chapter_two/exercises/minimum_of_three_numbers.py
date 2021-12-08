number1 = int(input('Enter first integer: '))
number2 = int(input('Enter second integer: '))
number3 = int(input('Enter third integer: '))

# TODO:First, we assume that number1 contains the smallest value, so line 9 assigns it to
#  the variable minimum . Of course, it’s possible that number2 or number3 contains
#  the actual smallest value, so we still must compare each of these with minimum .

minimum = number1

if number2 < minimum:
    minimum = number2

if number3 < minimum:
    minimum = number3

print(f'The Minimum value is {minimum}')

print(min(2, 33, 4, 1))
