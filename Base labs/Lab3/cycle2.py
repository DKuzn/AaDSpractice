for i in range(10):
    x = float(input("Введите x: "))
    y = float(input("Введите y: "))

    if y ** 2 + x ** 2 < 9 and x >= 0:
        print("Выстрел", i+1, "с координатами", "(", x, ",", y, ")", "попал в мишень.")
    elif y < abs(x) and y == 3 and y < -x and y == -3 and x < 0:
        print("Выстрел", i+1, "с координатами", "(", x, ",", y, ")", "попал в мишень.")
    else:
        print("Выстрел", i+1, "с координатами", "(", x, ",", y, ")", "не попал в мишень.")
