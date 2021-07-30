import unittest
import methodMultiples

class Multiple(unittest.TestCase):
    def test_is_not_multiple(self):
        self.assertEqual(methodMultiples.function_multiples(2, 8), True)
    
if __name__ == '__main__':
    unittest.main()
