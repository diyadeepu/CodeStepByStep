# Write a function named print_powers_of_n that accepts a base and exponent as 
# parameters and prints each power of the base from base0 (1) up to that maximum
# power, inclusive, separated by spaces. For example, the call of 
# print_powers_of_n(5, 6) should produce the following output:
# 1 5 25 125 625 3125 15625
# You may assume that the exponent passed is 0 or greater.

def print_powers_of_n (b: int, n: int) -> None:
    i = 0
    while i <= n:
        print(pow(b,i), end = " ")
        i = i+1
