# Method that return the median (middle) of three integer values

def median_of_3(num1: int, num2: int, num3: int) -> int:
    if num1 < num2:
        if num2 < num3:
            return num2
        elif num3 < num1:
            return num1
        else:
            return num3
    else:
        if num1 < num3:
            return num1 
        elif num3 < num2:
            return num2
        else:
            return num3
