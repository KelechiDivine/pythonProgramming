import math

def get_diameter_of_circle_function(find_diameter):
    """Function the user input diamter"""
    diameter = 2 * find_diameter
    return diameter

def get_radius_of_a_circle_function(find_radius):
    """Function for user input raidus"""
    radius = find_radius / 2
    return radius

def get_circumference_of_a_circle(find_circumference):
    """Function for user input circumference"""
    circumference = 2 * math.pi * find_circumference
    return circumference

def get_area_of_a_circle(find_area):
    """Function for user input area"""
    area = math.pi * (find_area * find_area)
    return area
