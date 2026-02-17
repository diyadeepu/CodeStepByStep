# Write a function named sphere_volume that accepts a radius as a parameter and 
# returns the volume of a sphere with those dimensions. For example, the call of
# sphere_volume(2.0) should return roughly 33.510321638291124. The formula for 
# the volume of a sphere with radius r is:
# volume = 4/3 * π * r^3
import math

def sphere_volume(radius: float) -> float:
    return (radius*radius*radius*4*math.pi)/3
