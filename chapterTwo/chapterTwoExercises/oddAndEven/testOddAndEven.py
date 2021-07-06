import unittest
import MethodOddAndEven

class ValidatingTwoNumbers(unittest.TestCase):
    
    def test_odd_number(self):
        """Test for odd number"""
        odd_number = MethodOddAndEven.is_odd(3)
        self.assertTrue(odd_number, True)
        
    def test_even_number(self):
        """Test for even number"""
        even_number = MethodOddAndEven.is_even(4)
        self.assertTrue(even_number, True)


if __name__ == '__main__':
    unittest.main()
