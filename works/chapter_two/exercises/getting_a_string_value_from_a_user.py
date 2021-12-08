# TODO: Function print always return a string

value1 = input('Enter first number: ')
value2 = input('Enter second number: ')

result = value1 + value2
print(f"The result of {value1} and {value2} is {result}")

"""
        Rather than adding the integers from value1 and value2 to produce result , Python “adds” the string values from
        'value1' and 'value2' , producing the string 'value1value2' . This is known as STRING CONCATENATION. It creates 
        a new string containing the left operand’s value followed by the right operand’s value.
"""