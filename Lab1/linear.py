import math
x = float(input("Введите x: "))
y = float(input("Введите y: "))
z1 = math.cos(x)**4 + math.sin(x)**2 + math.sin(2*x)**2 / 4 - 1
z2 = math.sin(y + x)*math.sin(y - x)
print(z1, z2)
