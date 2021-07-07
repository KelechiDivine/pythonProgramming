import unittest
import methodArithmeticSmallestAndLargest


class TestSmallestNumber(unittest.TestCase):
   
    def test_smallest(self):
        small = methodArithmeticSmallestAndLargest.smallest_number(2, 3, 6)
        self.assertEqual(3, small)


if __name__ == '__main__':
    unittest.main()
