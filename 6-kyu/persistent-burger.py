# DESCRIPTION:
# Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, which is the number of times you must multiply the digits in num until you reach a single digit.



#solution

import math

def persistence(n):
    score = 1
    start = [int(i) for i in str(n)]
    if len(start) == 1:
        return 0
    while True:
        product = math.prod(start)
        split = [int(i) for i in str(product)]
        if len(split) != 1:
            score += 1
            start = [int(i) for i in str(product)]
        else:
            return score