# Write a function named factor_count that accepts an integer (assumed to be 
# positive) as its parameter and returns a count of its positive factors. For 
# example, the eight factors of 24 are 1, 2, 3, 4, 6, 8, 12, and 24, so the call
# of factor_count(24) should return 8.

def factor_count(n1: int) -> int:
    if n1 == 1:
        return n1
    i = 2
    count = 0
    while i <=n1:
        if n1 % i == 0:
            count= count+1
        i = i + 1
    return count+1
