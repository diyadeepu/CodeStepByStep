# Write a function named get_days_in_month that accepts an integer parameter 
# representing a month (between 1 and 12) and returns the number of days in that
# month in a non-leap year. For example, the call get_days_in_month(9) would 
# return 30 because September has 30 days.

def get_days_in_month(m: int) -> int:
    if (m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12):
        return 31
    elif (m == 4 or m == 6 or m == 9 or m == 11):
        return 30
    else:
        return 28
