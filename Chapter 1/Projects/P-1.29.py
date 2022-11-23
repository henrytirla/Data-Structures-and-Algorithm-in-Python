"""Write a Python program that outputs all possible strings formed by using
the characters c , a , t , d , o , and g exactly once.




"""



def get_permutation(string, i=0):

    if i == len(string):
        print("".join(string))

    for j in range(i, len(string)):
        words = [c for c in string]

        # swap
        words[i], words[j] = words[j], words[i]
        get_permutation(words, i + 1)



print(get_permutation('abcd'))
