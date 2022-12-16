#DESCCRIPTION

# Give the summation of all even numbers in a Fibonacci sequence up to, but not including, the number passed to your function. Or, in other words, sum all the even Fibonacci numbers that are lower than the given number n (n is not the nth element of Fibonacci sequence) without including n.

# The Fibonacci sequence is a series of numbers where the next value is the addition of the previous two values. The series starts with 0 and 1:

# 0 1 1 2 3 5 8 13 21...


#solution 1

def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def even_fib(m):
    first = fib()
    answer = next(first)
    new_list = []
    while answer < m:
        if answer % 2 == 0:
            new_list.append(answer)
        answer = next(first)
    return sum(new_list)


# solution 2

def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def even_fib(m):
    return sum([x for x in fib(50) if x % 2 == 0 and x < m])