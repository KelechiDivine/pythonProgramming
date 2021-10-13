import unittest
from numbers import *

class PositiveAndNegativeNumbersTest(unittest.TestCase):
   
   def test__that_positive_and_negative_numbers_class_exist(self):
      its_exist = PositiveAndNegativeNumbers()
      self.assertIsNotNone(its_exist)
      
   def test__return_true_if_two_numbers_are_positive(self):
      x = PositiveAndNegativeNumbers()
      its_positive = x.check_if_two_numbers_are_positive(2, 3)
      self.assertTrue(its_positive)

   def test__return_true_if_two_numbers_are_negative(self):
      x = PositiveAndNegativeNumbers()
      its_negative = x.check_if_two_numbers_are_negative(-2, -3)
      self.assertTrue(its_negative)
      
   def test__return_true_if_one_out_of_two_numbers_is_negative(self):
      x = PositiveAndNegativeNumbers()
      one_number_is_negative = x.check_if_two_numbers_are_negative(-2, 8)
      self.assertTrue(one_number_is_negative)
      
   def test_return_true_if_one_out_of_two_numbers_is_positive(self):
      x = PositiveAndNegativeNumbers()
      one_number_is_positive = x.check_if_two_numbers_are_positive(2, -4)
      self.assertTrue(one_number_is_positive)

   def test__return_true_if_first_number_is_positive(self):
      x = PositiveAndNegativeNumbers()
      first_number_is_positive = x.check_if_first_number_is_positive(2)
      self.assertTrue(first_number_is_positive)
      
   def test_return_true_if_first_number_is_negative(self):
      x = PositiveAndNegativeNumbers()
      first_number_is_negative = x.check_if_first_number_is_negative(-2)
      self.assertTrue(first_number_is_negative)
   
   def test_return_true_if_second_number_is_positive(self):
      x = PositiveAndNegativeNumbers()
      second_number_is_positive = x.check_if_second_number_is_positive(2)
      self.assertTrue(second_number_is_positive)
      
   def test_return_true_if_second_number_is_negative(self):
      x = PositiveAndNegativeNumbers()
      second_number_is_negative = x.check_if_second_number_is_negative(-9)
      self.assertTrue(second_number_is_negative)
      
if __name__ == '__main__':
   unittest.main()
