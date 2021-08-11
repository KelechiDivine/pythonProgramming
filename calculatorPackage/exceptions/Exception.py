while True:
    try:
        number1 = int(input("Enter a numerator: "))
        number2 = int(input("Enter denominator: "))
        results = number1 / number2
        
    except ValueError:
        print("You must enter two integers!\n")
        
    except ZeroDivisionError:
        print("Attempted to divide by zero!\n")
        
    # except IndexError:
    #     print("Entered an error.\n")
        
    else:
        print(f"{number1: 3f} / {number2:.3f} = {results:.3f}")
        break