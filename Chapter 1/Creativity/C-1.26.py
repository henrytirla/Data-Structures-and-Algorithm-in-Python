"""Write a short program that takes as input three integers, a, b, and c, from
the console and determines if they can be used in a correct arithmetic
formula (in the given order), like “a+b = c,” “a = b−c,” or “a ∗ b = c.”"""



def func26():
    done = False
    para = []
    while not done:
        console = input('Please enter 1 integer  3x times press enter when done: ')
        if console == '':
            done = True
            break
        para.append(console)
    a = int(para[0])
    b = int(para[1])
    c = int(para[2])
    if a + b == c or a == b - c or a * b == c:
        return True
    return False


print(func26())