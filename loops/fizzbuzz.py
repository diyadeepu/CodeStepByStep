# Write a console program that prompts the user for an integer, then prints all 
# of the numbers from one to that integer, separated by spaces. Use a loop to 
# print the numbers. But for multiples of three, print "Fizz" instead of the 
# number, and for the multiples of five print "Buzz". For numbers which are 
# multiples of both three and five print "FizzBuzz". Drop to a new line after 
# printing each 20 numbers.

a = int(input("Max value? "))
n = ""
for i in range (1, a + 1):
    if (i % 3 == 0 and i % 5 == 0):
        n += "FizzBuzz "
    elif (i % 3 == 0):
        n += "Fizz "
    elif (i % 5 == 0):
        n += "Buzz "
    else:
        n += str(i) + " "
    if (i % 20 == 0):
        n += "\n"
print(n)
