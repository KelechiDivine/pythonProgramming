numberOne = int(input("Enter first integer: "))
numberTwo = int(input("Enter second integer: "))
numberThree = int(input("Enter third integer: "))

minimum = numberOne

if numberTwo < minimum:
    minimum = numberTwo
    
if numberThree < minimum:
    minimum  = numberThree
    
print('Minimum value is', minimum)