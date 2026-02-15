# Write for loops to produce the following output: 
# 1 
# 22 
# 333 
# 4444
# 55555

n = ""
for i in range (1, 6):
    for j in range (1, i+1):
        n += str(i)
    n += "\n"
print(n)
