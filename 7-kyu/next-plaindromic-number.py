# DESCRIPTION:
# There were and still are many problem in CW about palindrome numbers and palindrome strings. We suposse that you know which kind of numbers they are. If not, you may search about them using your favourite search engine.

# In this kata you will be given a positive integer, val and you have to create the function next_pal()(nextPal Javascript) that will output the smallest palindrome number higher than val.

#solution

def next_pal(val):
    number = val + 1
    string_number = str(number)
    while string_number != string_number[::-1]:
        string_number = str(int(string_number) + 1)
    return int(string_number)
        