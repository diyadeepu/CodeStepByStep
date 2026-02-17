# Write a function named sum_up_to function that accepts an integer parameter n 
# and returns the sum of the integers from 1 through n inclusive. For example,
# sum_up_to(5) returns 1 + 2 + 3 + 4 + 5 or 15. You may assume that the value of
# n is at least 1.

def sum_up_to(n: int) -> int:
    sum = 0
    while n > 0:
        sum += n
        n -= 1
    return sum
