firstUserInput = int(input("Enter first number: "))
secondUserInput = int(input("Enter second number: "))

if secondUserInput % firstUserInput == 0:
    print("First number is a multiple of the second number.")
    
if secondUserInput % firstUserInput == 1:
    print("First number is not multiple of the second number")
    
if firstUserInput % secondUserInput == 0:
    print("null")