# Write a function named vertical that accepts a string as its parameter and 
# prints each letter of the string on separate lines. For example, a call of 
# vertical("hey now") should produce the following output:
# h
# e 
# y
#
# n
# o
# w

def vertical (abc: str) -> None:
    for i in range (0,len(abc)):
        print(abc[i:i+1])
