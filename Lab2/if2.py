x = float(input("Введите x: "))
y = float(input("Введите y: "))

if y * y + x * x < 9 and x >= 0:
    print("Попадание")
elif y < abs(x) and y == 3 and y < -x and y == -3 and x < 0:
    print("Попадание")
else:
    print("Промах")
