import math

sques_eq = math.sqrt(4)
print("linbra value ")
print(sques_eq)


def abc():
    print("my first function")


abc()


def abc(num1, num2):
    sum = num1 + num2
    print(sum)


abc(5, 4)


def find_sq(num):
    result = num * num
    return result


sques = find_sq(5)
print(sques)


def default_Values(num1=5, num2=9):
    sum = num1 + num2
    print(sum)


default_Values()
default_Values(2, 5)
default_Values(6)
default_Values(num2=20)


def default_String(firstName="lokesh", secondName="gorantla"):
    print(firstName)
    print(secondName)


default_String()


def find_arb(*numbers):
    result = 0

    for num in numbers:
        result = result + num

    print("sum value ", result)


find_arb(5, 3, 6)


def add(a, b):
    adding = a + b
    return adding
