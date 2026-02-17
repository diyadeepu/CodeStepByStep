# Write a function named is_multiple that accepts two non-negative parameters a 
# and b, and returns True if a is a multiple of b, and False otherwise. For 
# example, the call of is_multiple(15, 5) would return True because 15 = 5 * 3.
# You may assume that a and b are non-negative integers and that b is not 0.

def is_multiple(a: int, b: int) -> float:
    if a % b == 0:
        return True
    return False
