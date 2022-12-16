# DESCRIPTION:
# An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

# Example: (Input --> Output)

# "Dermatoglyphics" --> true "aba" --> false "moOse" --> false (ignore letter case)

#solution

from collections import Counter

def is_isogram(string):
    new_string = [str(x).lower() for x in string]
    counter_object = Counter(new_string)
    for key, value in counter_object.items():
        if value > 1:
            return False
    return True
    