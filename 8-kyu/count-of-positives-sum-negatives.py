# DESCRIPTION:
# Given an array of integers.

# Return an array, where the first element is the
#  count of positives numbers and the second element
#   is sum of negative numbers. 0 is neither positive
#    nor negative.

# If the input is an empty array or is null, return an
#  empty array.

#solution

def count_positives_sum_negatives(arr):
    if len(arr) == 0:
        return[]
    else:
        return[len([num for num in arr if num > 0]), sum(num for num in arr if num <= 0)]
