# Write a function named gcd that accepts two integers as parameters and returns
# the greatest common divisor of the two numbers. The greatest common divisor 
# (GCD) of two integers a and b is the largest integer that is a factor of both
# a and b. One efficient way to compute the GCD of two numbers is to use 
# Euclid's algorithm, which states the following: 
# GCD(A, B) = GCD(B, A % B) 
# GCD(A, 0) = Absolute value of A 
# In other words, if you repeatedly mod A by B and then swap the two values, 
# eventually B will store 0 and A will store the greatest common divisor. 

# For example: gcd(24, 84) returns 12, gcd(105, 45) returns 15, and gcd(0, 8) 
# returns 8.

def gcd(a: int, b: int) -> int:
    a = abs(a)
    b = abs(b)
    if (a == 0 or a == 1):
        return abs(b)
    elif (b == 0 or b == 1):
        return abs(a)
    else:
        if (a < b):
            if (b % a == 0):
                return a
            for i in range (1, a-1):
                if a % (a-i) == 0 and b % (a-i) == 0:
                    return a-i;
        elif (b < a):
            if (a % b == 0):
                return b
            for i in range (1, b-1):
                if b % (b-i) == 0 and a % (b-i) == 0:
                    return b-i
    return a
