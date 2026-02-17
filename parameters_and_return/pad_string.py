# Write a function named pad_string that accepts two parameters: a string and an
# integer representing a length. The function should pad the end of the string 
# with spaces until its length is the given length. For example, the call of 
# pad_string("hello", 8) should return "hello   " with 3 spaces after the word. 
# If the string's length is already at least as long as the length parameter, 
# your function should return the original string. For example, the call of 
# pad_string("congratulations", 10) should return "congratulations" unmodified.

def pad_string(a: str, n: int) -> str:
    if (len(a) > n):
        return a
    else:
        b = n - len(a)
        for i in range (0, b):
            a += " "
        return a
