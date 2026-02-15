# Write a function named floyds_triangle that accepts an integer k as a 
# parameter and prints a k-row version of Floyd's triangle. Floyd's triangle is
# a sequence of increasing numbers, starting with 1, where each Nth row of 
# numbers displays the next N numbers in the sequence. For example, the call of 
# floyds_triangle(5); should print the following console output:
"""
# START OF OUTPUT #
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
# END OF OUTPUT #
"""

# If k is 0 or negative, print no output.

def floyds_triangle(k: int) -> None:
    if k <= 0:
        print("")
    else:
        c = 1
        for i in range(1, k+1):
            s = ""
            for j in range (1, i+1):
                s = s+ str(c) + " ";
                c += 1
            print(s)
