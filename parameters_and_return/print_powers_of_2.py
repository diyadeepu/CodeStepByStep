# Write a function named print_powers_of_2 that accepts a maximum number as a
# parameter and prints each power of 2 from 20 (1) up to that maximum power, 
# inclusive, separated by spaces. For example, the call of print_powers_of_2(10)
# should produce the following output:
# 1 2 4 8 16 32 64 128 256 512 1024
# You may assume that the value passed is 0 or greater.

def print_powers_of_2 (n1: int) -> None:
    i = 0
    while i <= n1:
        print(pow(2,i), end = " ")
        i = i+1
