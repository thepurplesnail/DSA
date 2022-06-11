"""
Let’s say we have a staircase of N steps, and a person has the ability to climb
one, two, or three steps at a time. How many different possible “paths” can
someone take to reach the top?
"""
def count(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    return count(n - 1) + count(n - 2) + count(n - 3)

