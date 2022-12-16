# DESCRIPTION:
# Return an array containing the numbers from 1 to N, where N is the parametered value.

# Replace certain values however if any of the following conditions are met:

# If the value is a multiple of 3: use the value "Fizz" instead
# If the value is a multiple of 5: use the value "Buzz" instead
# If the value is a multiple of 3 & 5: use the value "FizzBuzz" instead
# N will never be less than 1.



#solution

def fizzbuzz(n):
    word_list = []
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            word_list.append("FizzBuzz")
        elif i % 3 == 0:
            word_list.append("Fizz")
        elif i % 5 == 0:
            word_list.append("Buzz")
        else:
            word_list.append(i)
    return word_list