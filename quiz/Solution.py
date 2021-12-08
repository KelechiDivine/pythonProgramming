for x in range(1, 101):
    if x % 15 == 0:
        print(f"{x} is a FizzBuzz...")

    elif x % 3 == 0:
        print(f"{x} is a Buzz...")

    elif x % 5 == 0:
        print(f"{x} is a Fizz...")

    else:
        print(x)
