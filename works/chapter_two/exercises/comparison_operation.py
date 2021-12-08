"""Comparing integers using if statements and comparison operators."""

print('Enter two integers, and I will tell you', 'the relationship they satisfy.')

number1 = int(input('Enter first integer: '))
number2 = int(input('Enter second integer: '))

if number1 == number2:
    print(f'{number1} is equal to {number2}')

if number1 != number2:
    print(f'{number1} is not equal to {number2}')

if number1 < number2:
    print(f'{number1} is lesser than {number2}')

if number1 > number2:
    print(f'{number1} is greater than {number2}')

if number1 <= number2:
    print(f'{number1} is lesser than or equals to {number2}')

if number1 >= number2:
    print(f'{number1} is greater than or equal to {number2}')
