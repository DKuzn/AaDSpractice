import math
import random as rd


def esum(x, n):
    s = 0
    for i in range(n):
        s += ((-1) ** (i + 1)) / ((2 * i + 1) * x ** (2 * i + 1))
    return s


x1 = float(input("Введите x1: "))
x2 = float(input("Введите x2: "))
dx = 1
print('-' * 70)
print('{:<1} {:<20} {:<1} {:<20} {:<1} {:20} {:<1}'.format('|', 'x', '|', 'y', '|', 'n', '|'))
print('-' * 70)

while x1 != x2 + 1:
    n = rd.randint(0, 100)
    if 1 < x1 <= x2:
        y = math.pi / 2 + esum(x1, n)
        print('{:<1} {:<20} {:<1} {:<20} {:<1} {:20} {:<1}'.format('|', x1, '|', y, '|', n, '|'))
    else:
        print('{:<1} {:<20} {:<1} {:<20} {:<1} {:20} {:<1}'.format('|', 'Неверное значение x.', '|', 'NO', '|', n, '|'))
    print('-' * 70)
    x1 += dx
