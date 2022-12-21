def addition(x, y):
    result = x + y
    #    print(result)
    return result


def subtraction(y, x):
    result = (y - x)
    #    print(result)
    return result


def multiplication(x, y):
    result = x * y
    #    print(result)
    return result


def divide(x, y):
    result = x / y
    #    print(result)
    return result


def exponent(x, y):
    result = x ** y
    #    print(result)
    return result


while True:
    A = float(input("Enter the first number: "))
    B = float(input("Enter the second number: "))

    opr = input("Select the operator:\n1 for '+'\n2 for '-'\n3 for '*'\n4 for '/'\n5 for 'exp'\n")

    if opr == "1":
        print(addition(A, B))

    if opr == "2":
        print(subtraction(A, B))

    if opr == "3":
        print(multiplication(A, B))

    if opr == "4":
        print(divide(A, B))

    if opr == "5":
        print(exponent(A, B))

    more = input("Do you want to perform another calculation? (y/n)")
    if more == 'y':
        continue
    elif more == "n":
        print("Thank you for using calculator. Good Bye!")
        break



