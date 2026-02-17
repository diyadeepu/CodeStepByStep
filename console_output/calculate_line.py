# Write an interactive console program that calculates y coordinates on a line. 
# First, it prompts the user for a slope m, and an intercept b (as seen in the 
# line equation of the form y = m x + b). Then the program prompts the user for
# x values until the user enters a -1. For each entered number, print the y 
# value on that line for that entered x value. Here is a sample run of the 
# program (user input is shown like this):

# This program calculates y coordinates for a line.
# Enter slope (m): 2
# Enter intercept (b): 4
# Enter x: 5
# f(5) = 14
# Enter x: 1
# f(1) = 6
# Enter x: -1

print("This program calculates y coordinates for a line.")
m = int(input("Enter slope (m): "))
b = int(input("Enter intercept (b): "))
user = int(input("Enter x: "))
while (user != -1):
    print("f(" + str(user) + ") = " + str(m*user + b))
    user = int(input("Enter x: "))
