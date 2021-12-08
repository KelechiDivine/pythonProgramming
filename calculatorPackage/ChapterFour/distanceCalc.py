import math


class DistanceCalculation(object):
    
    def distance_method_can_not_be_null(self):
        print("Hey! Yo, This method isn't null...")


    def calculateDistance(self, x1, x2, y1, y2):
        distance = math.sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1))
        print(f"The distance between point x and y is: {distance}")
        return distance