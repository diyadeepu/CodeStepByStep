# Write a function named factorial that accepts an integer n as a parameter and 
# prints the factorial of n, or n!, as output. A factorial of an integer is 
# defined as the product of all integers from 1 through that integer inclusive. 
# For example, the call of factorial(4) should print the following output:
# 4 factorial = 24 
# The factorial of 0 and 1 are defined to be 1. You may assume that the value 
# passed is non-negative and that its factorial can fit in the range of type
# int.

def factorial(n: int) -> None:
    product = 1
    for i in range (1,n+1):
        product *= i;
    print(str(n),"factorial =", product)
