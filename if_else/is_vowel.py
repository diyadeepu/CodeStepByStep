# Write a function named is_vowel that returns whether a string is a vowel (a 
# single-letter string containing a, e, i, o, or u, case-insensitively).

def is_vowel (string_value: str) -> bool:
    if (string_value == "a" or string_value == "A"):
        return True
    elif (string_value == "e" or string_value == "E"):
        return True
    elif (string_value == "i" or string_value == "I"):
        return True
    elif (string_value == "o" or string_value == "O"):
        return True
    elif (string_value == "u" or string_value == "U"):
        return True
    return False
