# Write a function named get_first_digit that returns the first digit of an 
# integer. For example, get_first_digit(3572) should return 3.

def get_first_digit(n: int) -> int:
    n = abs(n)
    while n >= 10:
        n = n//10
    return n
