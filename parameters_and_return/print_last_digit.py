# Write a function named print_last_digit that prints information about the last 
# digit of an integer in the following format. For example, the call of 
# print_last_digit(3572) should print:
# Last digit of 3572 is 2
# You may assume that the parameter passed will be a non-negative integer.

def print_last_digit (num1: int) -> None:
    print("Last digit of " + str(num1)+ " is " + str(num1%10))
