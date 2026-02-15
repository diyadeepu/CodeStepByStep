# Write a function named enough_time_for_lunch that accepts four integers hour1,
# minute1, hour2, and minute2 as parameters. Each pair of parameters represents
# a time on the 24-hour clock (for example, 1:36 PM would be represented as 13 
# and 36). The function should return True if the gap between the two times is 
# long enough to eat lunch: that is, if the second time is at least 45 minutes 
# after the first time. Otherwise the function should return False.
# 
# You may assume that all parameter values are valid: the hours are both 
# between 0 and 23, and the minute parameters are between 0 and 59. You may
# also assume that both times represent times in the same day, e.g. the first 
# time won't represent a time today while the second time represents a time 
# tomorrow. Note that the second time might be earlier than the first time; in 
# such a case, your function should return False.

def enough_time_for_lunch(hour1: int, min1: int, hour2: int, min2: int) -> bool:
    if (hour1 > hour2):
        return False
    elif (hour1 < (hour2 - 1)):
        return True
    elif (((60 - min1) + min2) < 45):
        return False
    return True
