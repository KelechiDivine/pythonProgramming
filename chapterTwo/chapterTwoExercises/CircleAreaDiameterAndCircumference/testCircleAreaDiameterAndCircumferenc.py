import unittest
import MethodForCircleAreaCAndDiameters


class circle(unittest.TestCase):
    def test_area(self):
        """Testing if our area method is passing"""
        area_test = MethodForCircleAreaCAndDiameters.get_area_of_a_circle(4)
        self.assertEqual(area_test, 50.26548245743669)
        
    def test_circumference(self):
        """Test for circumference function is passing"""
        circumference = MethodForCircleAreaCAndDiameters.get_circumference_of_a_circle(4)
        self.assertEqual(circumference, 25.132741228718345)
        
    def test_radius(self):
        """Test for radius function is passing"""
        radius = MethodForCircleAreaCAndDiameters.get_radius_of_a_circle_function(6)
        self.assertEqual(radius, 3, "Error")
    
    def test_diameter(self):
        """Test for diameter function is passing"""
        diameter = MethodForCircleAreaCAndDiameters.get_diameter_of_circle_function(4)
        self.assertEqual(diameter, 8)

if __name__ == '__main__':
    unittest.main()
