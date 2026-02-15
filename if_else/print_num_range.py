# Write a function named print_num_range that accepts two integers as parameters
# and prints the sequence of numbers between the two arguments, separated by 
# commas and enclosed in square brackets. Print an increasing sequence if the 
# first argument is smaller than the second; otherwise, print a decreasing 
# sequence. If the two numbers are the same, that number should be printed by 
# itself. Here are some sample calls to print_num_range: print_num_range(2, 7) 
# print_num_range(19, 11) print_num_range(5, 5)

def print_num_range (a: int, b: int) -> None:
    list = []
    if (a == b):
        list.append(a)
    elif (a < b):
        i = a
        for i in range (a, b+1):
            list.append (i)
    else:
        for i in range (b, a+1):
            list.insert (0,i)
    print(list)
