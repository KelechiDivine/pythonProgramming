import OddAndEven

userInput = int(input("Enter number: "))

if userInput == OddAndEven.is_odd(userInput):
    print("\nThis number is odd")

if userInput == OddAndEven.is_even(userInput):
    print("\nThis number is an even number")