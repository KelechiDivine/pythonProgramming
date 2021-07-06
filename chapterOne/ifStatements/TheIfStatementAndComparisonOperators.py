print("Enter two integers and I will tell you the relationships they satisfy.")

numberOne = int(input("Enter first integer: "))

numberTwo = int(input("Enter second integer: "))

if numberOne == numberTwo:
    print(numberOne, 'is equal to', numberTwo)
    
if numberOne != numberTwo:
    print(numberOne, "is not equal to", numberTwo)
    
if numberOne < numberTwo:
    print(numberOne, 'is greater than', numberTwo)
    
if numberOne > numberTwo:
    print(numberOne, 'is lesser than', numberTwo)
    
if numberOne <= numberTwo:
    print(numberOne, 'is less than or equal to', numberTwo)
    
if numberOne >= numberTwo:
    print(numberOne, 'is greater than or equal to', numberTwo)