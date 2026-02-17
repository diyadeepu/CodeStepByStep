# Write a function named sum_of_range function that accepts two integer 
# parameters min and max and returns the sum of the integers from min through 
# max inclusive. For example, the call of sum_of_range(3, 7) returns 3 + 4 + 5 +
# 6 + 7 or 25. If min is greater than max, return 0.

def sum_of_range(a: int,b: int) -> int:
    if (a >= b):
        return 0
    sum = 0
    while a < b:
        sum += a
        a+=1
    sum += b
    return sum
