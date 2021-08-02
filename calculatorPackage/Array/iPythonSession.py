"""Create a one-dimensional array from a list comprehension that
produces the even integers from 2 through 20. """

import numpy as np
number = np.array([
    index for index in range (2, 21, 2)
])

print(number)