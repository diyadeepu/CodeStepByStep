# Write a piece of code that reads a shorthand text description of a color and 
# prints the longer equivalent. Acceptable color names are B for Blue, G for
# Green, and R for Red. If the user types something other than B, G, or R, the 
# program should print an error message. Make your program case-insensitive so 
# that the user can type an uppercase or lowercase letter.

a = input("What color do you want? ")
if (a == "R" or a == "r"):
    print("You have chosen Red.")
elif (a == "G" or a == "g"):
    print("You have chosen Green.")
elif (a == "B" or a == "b"):
    print("You have chosen Blue.")
else:
    print("Unknown color: " + a)
