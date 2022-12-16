# DESCRIPTION:
# Complete the function to find the count of the most frequent item of an array. You can assume that input is an array of integers. For an empty array return 0

#solution
from collections import Counter

def most_frequent_item_count(collection):
    # Do your magic. :)
    counter_object = Counter(collection)
    return 0 if len(collection) ==0 else max(counter_object.values())