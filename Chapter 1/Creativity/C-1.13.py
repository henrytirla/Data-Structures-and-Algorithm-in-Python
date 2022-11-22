"""Write a pseudo-code description of a function that reverses a list of n
integers, so that the numbers are listed in the opposite order than they
were before, and compare this method to an equivalent Python function
for doing the same thing."""


# pseudocode
# Declare Function
      #pass in list
#     Declare Result Array
#     for i in range between 0 and list
#         append list[i] to Result Array
#     return Result Array


def reverse_list_of_integers(list):
    reversed_array=[]
    for i in range(0, len(list)):
        reversed_array.append(list[len(list)-i-1])
    return reversed_array

print(reverse_list_of_integers([1,2,3,4,5]))


