import unittest
import OddAndEven

class TestEvenAndOdd(unittest.TestCase):
    
    def test_odd_number(self):
        odd_number = OddAndEven.is_odd(3)
        self.assertTrue(odd_number, True)
        
    def test_even_number(self):
        even_number = OddAndEven.is_even(4)
        self.assertTrue(even_number, True)

if __name__ == '__main__':
    unittest.main()
