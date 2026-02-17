# Write a function named larger_abs_val that takes two integers as parameters 
# and returns the larger of the two absolute values. For example, a call of 
# larger_abs_val(11, 2) would return 11, and a call of larger_abs_val(4, -5) 
# would return 5.

def larger_abs_val(a: int, b: int) -> int:
    a = abs(a)
    b = abs(b)
    if a < b:
        return b
    return a
