"""Write a Python program that can take a positive integer greater than 2 as
input and write out the number of times one must repeatedly divide this
number by 2 before getting a value less than 2."""


string="abc"


def get_permutation(string, i=0):

    if i == len(string):
        print("".join(string))

    for j in range(i, len(string)):

        words = [c for c in string]

        # swap
        words[i], words[j] = words[j], words[i]
        get_permutation(words, i + 1)


print(get_permutation('abcd'))