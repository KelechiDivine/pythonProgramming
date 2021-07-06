# Use if statements to determine whether an integer is odd or even.
# [Hint: Use the remainder operator. An even number is a multiple of 2. Any multiple of 2
# leaves a remainder of 0 when divided by 2.]

userInput = int(input("Enter a number: "))


if userInput % 2 == 0:
    print("The number you entered is an even number.")
    
if userInput % 2 == 1:
    print("The number you entered is an odd number.")