import math


def square(a):
    return math.ceil(a * a)


storona = float(input('Введите сторону: '))
print(square(storona))
