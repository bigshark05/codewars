# DESCRIPTION:
# Your task is to create a function that
#  does four basic mathematical operations.

# The function should take three arguments
#  - operation(string/char), value1(number),
#   value2(number).
# The function should return result of 
# numbers after applying the chosen operation.

# solution

def basic_op(operator, value1, value2):
    if operator == "+":
        return value1 + value2
    elif operator == "-":
        return value1 - value2
    elif operator == "*":
        return value1 * value2
    else:
        return value1 / value2
        