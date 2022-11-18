"""Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the odd positive integers smaller than n."""

def odd_squares(n):
    sum_n=0

    for i in range(n):
        if i % 2 != 0:
            sum_n+= i*i

    return sum_n

print(odd_squares(7))