# Write a function named compute_distance that accepts four integer coordinates
# x1, y1, x2, and y2 as parameters and computes the distance between points (x1,
# y1) and (x2, y2) on the Cartesian plane. The formula for the distance between
# two points is:
# d = √((x2 - x1)^2 + (y2 - y1)^2)
# For example, the call of compute_distance(10, 2, 3, 5) would return 
# 7.615773105863909.
import math

def compute_distance (x1: int, y1: int, x2: int, y2: int) -> float:
    d1 = (x2-x1)*(x2-x1)
    d2 = (y2-y1)*(y2-y1)
    return math.sqrt(d1 + d2)
