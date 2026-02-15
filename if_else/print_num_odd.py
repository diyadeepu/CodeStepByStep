# This function should return how many of its three parameters are odd numbers.

def print_num_odd(n1: int, n2: int, n3: int) -> None:
    count = 0
    if n1 % 2 != 0:
        count += 1
    if n2 % 2 != 0:
        count += 1
    if n3 % 2 != 0:
        count += 1
    print(count, "of the 3 numbers are odd.")
