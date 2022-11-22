"""Write a Python function that takes a sequence of numbers and determines
if all the numbers are different from each other (that is, they are distinct)."""

#
# def distinc_num(data):
#     if len(set(data)) != len(data):
#         return False
#     return True
#
# print(distinc_num([1,2,3,4,5]))
# print(distinc_num([1,1,2]))


def distinc_num(data):
    res = data[0]
    for i in range(1,len(data)):
        if res == data[i]:
           return False
        else:
            res = data[i]
    return True

print(distinc_num([1,2,3,4,4,5]))
print(distinc_num([1,2,3,4,5]))



