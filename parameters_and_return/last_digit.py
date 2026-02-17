# Write a function named last_digit that returns the last digit of an integer.
# For example, last_digit(3572) should return 2. It should work for negative 
# numbers as well; last_digit(-947) should return 7.

def last_digit (num1: int) -> int:
    num1 = abs(num1)
    return num1 % 10
