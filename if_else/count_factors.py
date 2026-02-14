# Method called count_factors that return the number of factors of a given
# integer called number (passed as parameter)

def count_factors(number: int) -> int:
    count = 0
    for value in range (1, number + 1):
        if number % value == 0:
            count += 1
    return count
