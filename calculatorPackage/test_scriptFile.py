import unittest
from scripFile import *

class ScriptTest(unittest.TestCase):
   
   def test__script_class_exist(self):
      its_exist = Script()
      self.assertIsNotNone(its_exist)
      
   def test__that_the_sum_of_two_numbers_will_be_50(self):
       x = Script()
       sum_is_50 = x.return_true_if_sum_of_two_numbers_is_50(25, 25)
       self.assertTrue(sum_is_50, "No result found.")
  
   def test_that_first_number_will_return_true_if_its_50(self):
       x = Script()
       first_number_is_50 = x.return_true_if_first_number_is_50(50)
       self.assertTrue(first_number_is_50, "There was a problem whole trying to find result.")
      
   def test_that_second_number_will_return_true_if_its_50(self):
       x = Script()
       second_number_is_50 = x.return_true_if_second_number_is_50(50)
       self.assertTrue(second_number_is_50, "No result found for second number.")
      
   def test_assert_fail_if_both_numbers_are_not_50(self):
       x = Script()
       the_sum_will_throw_error = x.return_true_If_sum_of_two_numbers_is_50(3,4)
       self.assertTrue(the_sum_will_throw_error)
   
   def test_assert_fail_if_first_number_is_not_50(self):
       x = Script()
       first_number_will_fail = x.return_true_if_first_number_is_50(2)
       self.assertTrue(first_number_will_fail)
      
   def test_assert_fail_if_second_number_is_not_50(self):
       x = Script()
       second_number_will_fail = x.return_true_if_second_number_is_50(2)
       self.assertTrue(second_number_will_fail)

if __name__ == '__main__':
   unittest.main()
