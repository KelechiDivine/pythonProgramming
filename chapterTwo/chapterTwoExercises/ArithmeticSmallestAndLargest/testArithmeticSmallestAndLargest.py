import unittest
import ArithmeticSmallestAndLargest


class TestSmallestNumber(unittest.TestCase):
   
    def test_is_small(self):
        small = ArithmeticSmallestAndLargest.smallest_number(2, 3, 6)
        self.assertEqual(2, small)
        """Will come back and refactor my code here..."""
    def test_is_large(self):
        large= ArithmeticSmallestAndLargest.largest_number(2,4,323)
        self.assertEqual(323, large, "Not large")


if __name__ == '__main__':
    unittest.main()
