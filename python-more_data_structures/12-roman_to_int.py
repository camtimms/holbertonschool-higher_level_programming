#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return (0)

    roman_numerals = {"M": 1000, "D": 500, "C": 100,
                      "L": 50, "X": 10, "V": 5, "I": 1}
    total = 0
    i = 0

    while i < len(roman_string):

        # Check if next value is more than the current and substract instead of
        #  add
        if (i + 1 < len(roman_string) and
                roman_numerals[roman_string[i]] <
                roman_numerals[roman_string[i + 1]]):

            total += (roman_numerals[roman_string[i+1]] -
                      roman_numerals[roman_string[i]])
            i += 1
        else:
            total += roman_numerals[roman_string[i]]
        i += 1
    return (total)
