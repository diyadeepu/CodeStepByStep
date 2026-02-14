# The following code contains a logic error. Examine the code and figure out
# the case(s) in which the code would print something that is untrue about
# the number that was entered. Then correct the logic error in the code. You 
# should retain the original printed messages (and not add any new ones), but 
# make them print at appropriate times such that the message printed is always 
# a true statement about the integer typed.

number = int(input("Type a number: "))
if number % 2 == 0:
    if number % 3 == 0:
        print("Divisible by 6.")
else:
    print("Odd.")
