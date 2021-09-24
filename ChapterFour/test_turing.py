import unittest
from turing import *

class TuringTest(unittest.TestCase):
    
    def test_turing_polls_exists(self):
        new_turing = Turing()
        self.assertIsNotNone(new_turing)
        
    def test_calPoint_will_execute(self):
        turing = Turing()
        myList = ["5", "2", "C", "D", "+"]
        
        self.assertEqual(turing.calPoint(myList), 30)
        
if __name__ == '__main__':
    unittest.main()
