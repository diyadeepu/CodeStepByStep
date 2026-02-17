# Write a function named sum_of_digits that accepts an integer parameter and 
# computes and returns the sum of all the digits of that number. For example, 
# sum_of_digits(38015) returns 3+8+1+0+5 or 17. For negative numbers, return the
# same value as if the number were positive. For example, sum_of_digits(-72) 
# returns 7+2 or 9.

def sum_of_digits(n: int) -> int:
    n = abs(n)
    sum = 0
    while n >= 10:
        sum += n % 10
        n = n//10
    sum += n
    return sum
