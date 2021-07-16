import unittest

from Calculator import adding_two_numbers as atn
from Calculator import subtracting_two_numbers as stn
from Calculator import multiplying_two_numbers as mtn
from Calculator import dividing_two_numbers as dtn

class Adding(unittest.TestCase):
    def test_adding_two_number(self):
        sum_value = atn(5,3)
        self.assertEqual(8, sum_value)
        
    def test_subtracting_two_numbers(self):
        minus_value = stn(4, 6)
        self.assertEqual(-2, minus_value)
        
    def test_multiplying_two_numbers(self):
        multiply_value = mtn(3, 4)
        self.assertEqual(12, multiply_value)
        
    def test_dividing_two_numbers(self):
        divide_value = dtn(4, 2)
        self.assertEqual(2, divide_value)
        
if __name__ == '__main__':
    unittest.main()
