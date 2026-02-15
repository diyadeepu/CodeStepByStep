# Write code to read an integer from the user, then print even if that number is
# an even number or odd otherwise. You may assume that the user types a valid 
# integer. The input/output should match the following example:
# Type a number: 14
# even

a = int(input("Type a number: "))
if (a % 2 == 0):
    print("even")
else:
    print("odd")
