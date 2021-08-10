import numpy as np

number= np.arange(1, 6)
# print(number)
number_two= number.copy()
# print(number_two)

number[1] *= 10
# print(number)
print(number_two)