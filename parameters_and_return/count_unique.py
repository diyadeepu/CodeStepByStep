# Write a function named count_unique that takes three integers as parameters 
# and that returns the number of unique integers among the three. For example, 
# the call count_unique(18, 3, 4) should return 3 because the parameters have 3
# different values. By contrast, the call count_unique(6, 7, 6) should return 2 
# because there are only 2 unique numbers among the three parameters: 6 and 7.

def count_unique(a: int, b: int, c: int) -> int:
    if (a != b and b != c and a != c):
        return 3
    elif (a == b and b == c):
        return 1
    elif (a == b or b == c or a == c):
        return 2
    else:
        return 0
