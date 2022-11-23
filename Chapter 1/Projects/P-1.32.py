"""Write a Python program that can simulate a simple calculator, using the
console as the exclusive input and output device. That is, each input to the
calculator, be it a number, like 12.34 or 1034, or an operator, like + or =,
can be done on a separate line. After each such input, you should output
to the Python console what would be displayed on your calculator."""


def divide(x, y):
    # divide
    if y == 0:
        print('0 cannot be used as a denominator')
        return
    else:
        return x / y


choice = input(
    "Please choose the operation:\n+, add\n-, subtract\n*, multiply\n/, divide\nPlease enter the operation (+/-/*//):")
num1 = float(input("Please enter the first number:"))
num2 = float(input("Please enter the second number:"))
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