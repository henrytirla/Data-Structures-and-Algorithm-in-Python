"""Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the positive integers smaller than n."""

def Sum_squares(n):
    sum_n = 0
    while n >0:
        n -=1
        sum_n += n*n
    return  sum_n

print(Sum_squares(4))