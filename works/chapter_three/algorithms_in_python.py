# TODO: Set total to zero
#  Set grade counter to zero
#  Set grades to a list of the ten grades
#  For each grade in the grades list:
#  Add the grade to the total
#  Add one to the grade counter
#  Set the class average to the total divided by the number of grades
#  Display the class average


total = 0
grade_counter = 0
grades = [98, 76, 71, 87, 83, 90, 57, 79, 82, 94]

for grade in grades:
    total += grade
    grade_counter += 1

average = total / grade_counter
print(f'Class average is {average}')
