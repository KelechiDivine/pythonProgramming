import unittest
import CircleAreaAndDiameters

class circle(unittest.TestCase):

    def test_area_of_a_circle(self):
        area_test = CircleAreaAndDiameters.get_area_of_a_circle(4)
        self.assertEqual(area_test, 50.26548245743669)
        
    def test_circumference_of_a_cirlcle(self):
        circumference = CircleAreaAndDiameters.get_circumference_of_a_circle(4)
        self.assertEqual(circumference, 25.132741228718345)
        
    def test_radius_a_circle(self):
        radius = CircleAreaAndDiameters.get_radius_of_a_circle(6)
        self.assertEqual(radius, 3, "Error")
    
    def test_diameter_a_circle(self):
        diameter = CircleAreaAndDiameters.get_diameter_of_circle(4)
        self.assertEqual(diameter, 8)

if __name__ == '__main__':
    unittest.main()
