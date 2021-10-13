import unittest
from arrayValue import *

class ArrayValueTest(unittest.TestCase):
   
   def test_array_value_class_exist(self):
      array_value_1 = ArrayValue()
      self.assertIsNotNone(array_value_1, "Test every line of code properly.")
      
   def test_can_be_converted_to_an_array(self):
      array_value = ArrayValue()
      actual: list = array_value.to_array(first_arg=2, second_arg=3)
      expected: list = [2,3]
      self.assertListEqual(expected,actual)


if __name__ == '__main__':
   unittest.main()
