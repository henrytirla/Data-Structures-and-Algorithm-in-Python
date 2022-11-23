"""

The birthday paradox says that the probability that two people in a room
will have the same birthday is more than half, provided n, the number of
people in the room, is more than 23. This property is not really a paradox,
but many people find it surprising. Design a Python program that can test
this paradox by a series of experiments on randomly generated birthdays,
which test this paradox for n = 5,10,15,20, . . . ,100.
"""

from scipy.special import perm


def Probobility(n):
    return 1 - perm(365, n) / pow(365, n)


for n in range(5, 105, 5):
    print(Probobility(n))