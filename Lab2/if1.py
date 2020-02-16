R = int(input("Введите R: "))
x = float(input("Введите x: "))

if -10 <= x <= -6:
    y = ((R ** 2 - (x + 8) ** 2) ** 0.5) - 2
elif -6 < x <= 2:
    y = 0.5 * x + 1
elif 2 < x < 6:
    y = 0
elif 6 <= x <= 8:
    y = (x - 6) ** 2
else:
    print("Неверное значение x")

print(y)
