# Write a function named first_digit that returns the first digit of an integer.
# For example, first_digit(3572) should return 3. It should work for negative 
# numbers as well. For example, first_digit(-947) should return 9.

def first_digit(number: int) -> int:
    number = abs(number)
    while number >= 10:
        number = number//10
    return number
