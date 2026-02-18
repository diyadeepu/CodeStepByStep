# Write a function named repeat that accepts a string and a number of 
# repetitions as parameters and returns the string concatenated that many times.
# For example, the call repeat("hello", 3) returns "hellohellohello". If the 
# number of repetitions is 0 or less, an empty string is returned.

def repeat (a: str, b: int) -> str:
    n = ""
    for i in range (0, b):
        n += a
    return n
