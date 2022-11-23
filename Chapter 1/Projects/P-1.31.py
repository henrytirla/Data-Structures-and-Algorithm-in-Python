"""Write a Python program that can “make change.” Your program should
take two numbers as input, one that is a monetary amount charged and the
other that is a monetary amount given. It should then return the number
of each kind of bill and coin to give back as change for the difference
between the amount given and the amount charged. The values assigned
to the bills and coins can be based on the monetary system of any current
or former government. Try to design your program so that it returns as
few bills and coins as possible."""


def ChangeMoney(m, n):
    money_type = (100, 50, 20, 10, 5, 1, 0.5, 0.1)
    if m < n:
        print('needs more money to charge!')
        return
    elif m == n:
        print('no need to return money!')
        return
    else:
        result = {}
        total = m - n
        for bill in money_type:
            num = total // bill
            result[str(bill) + '€'] = int(num)
            total = total - num * bill
    print(result)


ChangeMoney(200, 147)
