# Write a function named print_backward that accepts a String as its parameter 
# and prints the characters in the opposite order. For example, a call of 
# print_backward("hello there!") should print the following output: !ereht olleh
# If the empty string is passed, no output should be produced.

def print_backward(s: str) -> None:
    v = ""
    for i in range(0, len(s)):
        v += s[len(s)-1-i:len(s)-i]
    print(v)
