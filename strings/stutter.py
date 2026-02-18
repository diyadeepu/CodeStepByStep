# Write a function named stutter that accepts a string parameter returns a new 
# string replacing each of its characters with two consecutive copies of that 
# character. For example, A call of stutter("hello") would return "hheelllloo".

def stutter(string: str) -> str:
    a = ""
    for i in range(0, len(string)):
        a = a+ string[i:i+1]
        a = a+ string[i:i+1]
    return a
