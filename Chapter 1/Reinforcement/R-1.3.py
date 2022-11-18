"""Write a short Python function, minmax(data), that takes a sequence of
one or more numbers, and returns the smallest and largest numbers, in the
form of a tuple of length two. Do not use the built-in functions min or
max in implementing your solution.
"""

def minmax(data):
    largest_num =data[0]
    smallest_num =data[0]
    for num in data:
        if num > largest_num:
            largest_num =num
        elif num < smallest_num:
            smallest_num = num
    return largest_num,smallest_num


print(minmax([6,1,2,5,9,12]))






#print(minmax([1,2,3,6]))