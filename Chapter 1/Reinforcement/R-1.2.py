"""Write a short Python function, is even(k), that takes an integer value and
returns True if k is even, and False otherwise. However, your function
cannot use the multiplication, modulo, or division operators."""

def is_even(k):
    n = 2
    while k>n:
       n+=2
    if n-k == 1:
       return False

    return True


print(is_even(17))

