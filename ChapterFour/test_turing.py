import unittest
from turing import *

class TuringTest(unittest.TestCase):
    
    def test_turing_polls_exists(self):
        new_turing = Turing()
        self.assertIsNotNone(new_turing)


if __name__ == '__main__':
    unittest.main()
