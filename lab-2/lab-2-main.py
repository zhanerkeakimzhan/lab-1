# Жители страны Малевии часто экспериментируют
# с планировкой комнат. Комнаты бывают треугольные,
# прямоугольные и круглые. Чтобы быстро вычислять
# жилплощадь, требуется написать программу, на
# вход которой подаётся тип фигуры комнаты и
# соответствующие параметры, которая бы выводила
# площадь получившейся комнаты.

room = str(input())
if room == 'треугольник':
    a = int(input())
    b = int(input())
    c = int(input())
    p = (a + b + c)/2
    s = (p * (p-a) * (p-b) * (p-c))**0.5
    print(s)
elif room == 'прямоугольник':
    a = int(input())
    b = int(input())
    print(a * b)
elif room == 'круг':
    r = int(input())
    pi = 3.14
    print(pi * r**2)
else:
    print("Введите треугольник, круг или прямоугольник")