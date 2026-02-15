# Write a for loop that produces the following output: 
# 1 4 9 16 25 36 49 64 81 100 
# For added challenge, try to modify your code so that it does not need to use
# the * multiplication operator. (It can be done! Hint: Look at the differences
# between adjacent numbers.)

a = 0
n = ""
for i in range (1, 11):
    for j in range (1, i+1):
        a += i
    n += str(a) + " "
    a = 0
print(n)
