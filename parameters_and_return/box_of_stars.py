# Write a function named box_of_stars that accepts two integer parameters 
# representing a width and height in characters, and prints to the console a 
# 'box' figure whose border is * stars and whose center is made of spaces. For 
# example, the call of box_of_stars(8, 5) should print the following output: 
"""
******** 
*      * 
*      * 
*      * 
********
"""
# You may assume that the values passed for the width and height are at least 2.

def box_of_stars(a: int, b: int) -> None:
    n = ""
    for i in range (0, b):
        for j in range (0, a):
            if ((i == 0) or (i == b-1)):
                n += "*"
            elif (j == 0 or j == a-1):
                n += "*"
            else:
                n += " "
        n += "\n"
    print(n)
