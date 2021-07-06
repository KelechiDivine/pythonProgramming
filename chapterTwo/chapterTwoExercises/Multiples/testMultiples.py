import unittest
import methodMultiples


class Multiple(unittest.TestCase):
    
    def test_is_multiple(self):
        variable_is_multiple = methodMultiples.is_multiples(2, 4)
        self.assertTrue(variable_is_multiple, True)

if __name__ == '__main__':
    unittest.main()
