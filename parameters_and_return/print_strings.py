# Write a function named print_strings that accepts a string and a number of 
# repetitions as parameters and prints that string the given number of times
# with a space after each time. For example, the call of print_strings("abc", 5)
# should print the following output:
# abc abc abc abc abc

def print_strings(string: str, n1: int) -> None:
    for i in range(n1):
        print(string, end = " ")
