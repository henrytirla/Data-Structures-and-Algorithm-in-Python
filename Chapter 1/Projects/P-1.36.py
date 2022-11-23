"""Write a Python program that inputs a list of words, separated by white-space, and outputs how many times each word appears in the list. You need not worry about efficiency at this point, however,
as this topic is something that will be addressed later in this book."""

st = 'my name is Henry Tirla. I am using MacOs.'


def solut(st):
    lst = st.split()
    res = {}
    for items in lst:
        if items in res:
            res[items] += 1
        else:
            res[items] = 1
    print(res)
    return res


solut(st)