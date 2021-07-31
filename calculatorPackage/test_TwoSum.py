import unittest
import TwoSum

class TwoSumClass(unittest.TestCase):
    def test_is_two_sum(self):
        user_input_list = TwoSum.two_Sum([2, 2, 12, 15], 4)
        self.assertEqual([0,1], user_input_list)
        
if __name__ == '__main__':
    unittest.main()
