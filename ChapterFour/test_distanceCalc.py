import unittest
from distanceCalc import *

class DistanceCalculationTest(unittest.TestCase):
    
    def test_distance_class_exist(self):
        distanceCalculation = DistanceCalculation()
        p = distanceCalculation.distance_method_can_not_be_null()
        self.assertTrue(True)
        
    
    def test_calculateDistance(self):
        calculateDistance = DistanceCalculation()
        p = calculateDistance.calculateDistance(1, 2, 3, 4)
        self.assertEqual(1.4142135623730951, p)


if __name__ == '__main__':
    unittest.main()
