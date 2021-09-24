import unittest
from turing import *

class TuringTest(unittest.TestCase):
    
    def test_turing_polls_exists(self):
        new_turing = Turing()
        self.assertIsNotNone(new_turing)
        
    def test_calPoint_will_execute(self):
        turing = Turing()
        turing.calPoint(["5", "2", "1", "D", "C", "+"])
        self.assertTrue(True)
        
if __name__ == '__main__':
    unittest.main()
