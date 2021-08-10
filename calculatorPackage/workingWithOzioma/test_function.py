import unittest
import practice as fn
# from practice import multiplication_function as mf
# from practice import *

class Calculator(unittest.TestCase):
   
   """This function is to multiply two numbers"""
   
   def test_multiplication(self):
       # multiplication_objects = mf(2,3)
       multiplication_objects= fn.multiplication_function(2,3)
       self.assertEqual(7,multiplication_objects,'Blood everywhere')


if __name__ == '__main__':
    unittest.main()
