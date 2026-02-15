# Write a function named has_midpoint that accepts three integers as 
# parameters and returns True if one of the integers is the midpoint 
# between the other two integers; that is, if one integer is exactly halfway 
# between them. Your function should return False if no such midpoint 
# relationship exists. The integers could be passed in any order; the midpoint 
#could be the 1st, 2nd, or 3rd. You must check all cases.

# Calls such as the following should return True:
# has_midpoint(4, 6, 8)
# has_midpoint(2, 10, 6)
# has_midpoint(8, 8, 8)
# has_midpoint(25, 10, -5)
# Calls such as the following should return False:
#has_midpoint(3, 1, 3)
#has_midpoint(1, 3, 1)
#has_midpoint(21, 9, 58)
#has_midpoint(2, 8, 16)

def has_midpoint(a, b, c):
    if a == b and b == c:
        return True
    if a == b and a != c or b == c and a != b or a == c and b != c:
        return False
    if a < b and a < c:
        min = a
        if b < c:
            max = c
            if ((min + max)/2 == b):
                return True
        else:
            max = b
            if ((min + max)/2 == c):
                return True
    elif b < a and b < c:
        min = b
        if a < c:
            max = c
            if ((min + max)/2 == a):
                return True
        else:
            max = a
            if ((min + max)/2 == c):
                return True
    else:
        min = c
        if a < b:
            max = b
            if ((min + max)/2 == a):
                return True
        else:
            max = a
            if ((min + max)/2 == b):
                return True
    return False
