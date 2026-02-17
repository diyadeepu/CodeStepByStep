# Write a function named count_digits that accepts an integer parameter and 
# returns the number of digits in that integer. For example, count_digits(38015)
# returns 5. For negative numbers, return the same value as if the number were 
# positive. For example, count_digits(-72) returns 2.

def count_digits(n: int) -> int:
    n = abs(n)
    count = 1
    if (n > 0):
        n = n//10
        count += 1
    return count
