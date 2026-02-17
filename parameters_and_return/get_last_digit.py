# Write a function named get_last_digit that returns the last digit of an 
# integer. For example, the call of get_last_digit(3572) should return 2.

def get_last_digit (num1: int) -> int:
    num1 = abs(num1)
    return num1%10
