# DESCRIPTION:
# Description
# An infinite number of shelves are arranged one above the other in a staggered fashion.
# The cat can jump up to 3 shelves at the same time: from shelf 1 to shelf 2 or 4 (the cat cannot climb on the shelf directly above its head), according to the illustration:

#solution

def solution(start, finish): 
    import math
    maximum = finish - start
    if maximum < 3:
        return maximum
    return math.floor(maximum/3) + maximum%3