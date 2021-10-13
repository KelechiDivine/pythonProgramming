import unittest
from subChargeFile import *

class SubChargeTest(unittest.TestCase):
   
   def test_subCategory_exist(self):
      subCharge = SubCharge()
      self.assertIsNotNone(subCharge)
      
   def test_if_subCharge_is_greater_than_10_add_plus_2(self):
       x = SubCharge()
       actual = x.add_with_subCharge(5, 7)
       self.assertEqual(2, actual)
      
   def test_if_subCharge_is_lesser_or_equals_10_add_plus_1(self):
       y = SubCharge()
       actual = y.add_with_subCharge(2, 3)
       self.assertEqual(1, actual)
  

if __name__ == '__main__':
   unittest.main()
