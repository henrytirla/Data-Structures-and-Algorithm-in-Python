"""Write a short Python function that takes a string s, representing a sentence,
and returns a copy of the string with all punctuation removed. For example,
if given the string "Let s try, Mike.", this function would return
"Lets try Mike"."""



import string

a = "Let's try, Mike. May it be delicious!"
delset = string.punctuation


def delPunctuation(s):
    l = list(s)
    deltable = list(delset)
    for i in l:
        if i in deltable:
            l.remove(i)
    res = str()
    for i in l:
        res = res + i
    return res


print(delPunctuation(a))