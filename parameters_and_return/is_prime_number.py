# Write a function named is_prime_number that accepts an integer as a parameter
# and returns True if that integer is a prime number. A prime number is an
# integer that has no factors other than 1 and itself. The number 2 is defined 
# as the smallest prime number.

def is_prime_number(n: int) -> bool:
    if (n <= 1):
        return False
    for i in range (2, n):
        if (n % i == 0):
            return False
    return True
