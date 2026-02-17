# Write a function named print_stars that takes a number as a parameter and 
# outputs that many stars. You should output 1 star per line. For example, the 
# call print_stars(3) would print:
# *
# *
# *

def print_stars(n1: int) -> None:
    for i in range(n1):
        print("*")
