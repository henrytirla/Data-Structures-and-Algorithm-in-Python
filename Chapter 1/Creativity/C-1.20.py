"""Python’s random module includes a function shuffle(data) that accepts a
list of elements and randomly reorders the elements so that each possible
order occurs with equal probability. The random module includes a
more basic function randint(a, b) that returns a uniformly random integer
from a to b (including both endpoints). Using only the randint function,
implement your own version of the shuffle function."""

from random import randint
def Shuffle_remix(arr):
    res=[]
    while len(res) != len(arr):
        random_num = randint(arr[0],arr[-1])
        if random_num not in res:
           res.append(random_num)

    return res

print(Shuffle_remix([1,2,3,4]))