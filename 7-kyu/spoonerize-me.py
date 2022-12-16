# DESCRIPTION:
# A spoonerism is a spoken phrase in which the first letters of two of the words are swapped around, often with amusing results.

# In its most basic form a spoonerism is a two word phrase in which only the first letters of each word are swapped:

# "not picking" --> "pot nicking"

# Your task is to create a function that takes a string of two words, separated by a space: words and returns a spoonerism of those words in a string, as in the above example. A "word" in the context of this kata can contain any of the letters A through Z in upper or lower case, and the numbers 0 to 9. Though spoonerisms are about letters in words in the domain of written and spoken language, numbers are included in the inputs for the random test cases and they require no special treatment.

# NOTE: All input strings will contain only two words. Spoonerisms can be more complex. For example, three-word phrases in which the first letters of the first and last words are swapped: "pack of lies" --> "lack of pies" or more than one letter from a word is swapped: "flat battery --> "bat flattery" You are NOT expected to account for these, or any other nuances involved in spoonerisms.

#solution

def spoonerize(words):
    split_string = words.split()
    first = split_string[0][0]
    last = split_string[-1][0]
    
    return split_string[0].replace(split_string[0][0], last, 1) + " " + split_string[-1].replace(split_string[-1][0], first, 1)
    