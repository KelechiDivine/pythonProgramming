"""Displaying a bar chart"""
numbers= [19, 3, 15, 7, 11]
print("\nCreating a bar chart from numbers: ")
print(f"Index{'Value':>8}  Bar" )

for index, value in enumerate(numbers):
    print(f"{index:>5}{value:>8}    {'*' * value}")