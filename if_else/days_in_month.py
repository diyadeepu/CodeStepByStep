# Write a function named days_in_month that accepts a month (an integer between
# 1 and 12) as a parameter and returns the number of days in that month. For 
# example, the call days_in_month(9) would return 30 because September has 30
# days. Assume that the code is not being run during a leap year (that February
# always has 28 days). The following are the number of days in each month:

def days_in_month(m: int) -> int:
    if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
        return 31
    elif m == 4 or m == 6 or m == 9 or m == 11:
        return 30
    else:
        return 28
