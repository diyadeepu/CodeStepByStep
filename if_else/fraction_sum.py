# Write a function named fraction_sum that accepts an integer parameter n and
# returns the sum of the first n terms of the sequence:

# In other words, the function should generate the following sequence: 
# 1 + (1/2) + (1/3) + (1/4) + (1/5) + ... + (1/n) 
# You may assume that the parameter n is non-negative.

def fraction_sum (n):
    sum = 0
    for i in range (1, n+1):
        sum += 1/i
    return sum
