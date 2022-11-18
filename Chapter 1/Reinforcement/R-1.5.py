"""Give a single command that computes the sum from Exercise R-1.4, relying
on Python’s comprehension syntax and the built-in sum function."""

def sum_of_squares2(n):
    return sum([k * k for k in range(0, n)])


print(sum_of_squares2(4))