import CircleAreaAndDiameters

userInput = int(input("Enter number: "))

print(f"\nDiameter = {CircleAreaAndDiameters.get_diameter_of_circle(userInput)}")
print(f"Circumference = {CircleAreaAndDiameters.get_circumference_of_a_circle(userInput)}")
print(f"Area = {CircleAreaAndDiameters.get_area_of_a_circle(userInput)}")
print(f"Radius = {CircleAreaAndDiameters.get_radius_of_a_circle(userInput)}")