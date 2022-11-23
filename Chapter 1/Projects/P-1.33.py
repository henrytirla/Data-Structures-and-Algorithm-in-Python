"""Write a Python program that simulates a handheld calculator. Your program
should process input from the Python console representing buttons
that are “pushed,” and then output the contents of the screen after each operation
is performed. Minimally, your calculator should be able to process
the basic arithmetic operations and a reset/clear operation."""


def divide(x, y):
    # divide
    if y == 0:
        print('0 cannot be used as a denominator')
        return
    else:
        return x / y


ss = input()
while '#' not in ss:
    for i in range(len(ss)):
        if ss[i] in ['-', '+', '*', '/']:
            choice = ss[i]
            num1 = float(int(ss[0:i]))
            num2 = float(int(ss[i + 1:len(ss)]))
    if choice == '+':
        print("{}+{}={}".format(num1, num2, num1 + num2))
    elif choice == '-':
        print("{}-{}={}".format(num1, num2, num1 - num2))
    elif choice == '*':
        print("{}x{}={}".format(num1, num2, num1 * num2))
    elif choice == '/':
        print("{}/{}={}".format(num1, num2, divide(num1, num2)))
    else:
        print("The selected operation is an invalid input")
    ss = input()