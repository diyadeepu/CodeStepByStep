# Write a function named month_apart that accepts four integer parameters 
# representing two calendar dates. Each date consists of a month (1 through 12) 
# and a day (1 through the number of days in that month [28-31]). Assume that
# all dates occur during the same year. The function returns whether the dates 
# are at least a month apart. For example, the following dates are all 
# considered to be at least a month apart from 9/19 (September 19): 2/14, 7/25, 
# 8/2, 8/19, 10/19, 10/20, and 11/5. The following dates are NOT at least a 
# month apart from 9/19: 9/20, 9/28, 10/1, 10/15, and 10/18. Note that the first
# date could come before or after (or be the same as) the second date. Assume 
# that all parameter values passed are valid.

def month_apart(a: int, b: int, c: int, d: int) -> bool:
    if (a == c):
        return False
    elif (a == c + 1 and b >= d):
        return True
    elif (a < c - 1 or a > c + 1):
        return True
    elif (a == c - 1 and b <= d):
        return True
    return False
