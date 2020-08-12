#Zlatopolsky Chapter 1

import math
import random

def devide():
    print("\n")


#Арифметические выражения.


#Задание 1.1
print("1.1 Вывести на экран число Пи с точностью до сотых: " + format(math.pi, ".2f"))
devide()


#Задание 1.2 
print("1.2 Вывести на экран число Е с точностью до десятых: " + format(math.e, ".1f"))
devide()


#Задание 1.3 (без проверки на тип вводимых данных)
input_13 = input("1.3 Введите число: ")
print("Вы ввели число - " + input_13)
devide()


#Задание 1.4
input_14 = input("1.4 Введите число: ")
print(input_14 + " - вот какое число вы ввели.")
devide()


#Задание 1.5
n151, n152, n153 = 1, 13, 49
print("1.5 Вывести на одной строке числа через один пробел: {} {} {}".format(n151, n152, n153))
devide()


#Задание 1.6
n161, n162, n163 = 7, 15, 100
print("1.6 Вывести на одной строке числа через два пробела: {}  {}  {}".format(n161, n162, n163))
devide()


#Задание 1.7
n171 = random.randint(1, 11)
n172 = random.randint(11, 21)
n173 = random.randint(21, 31)
print("1.7 Вывести на экран одну строку трех любых чисел через два пробела: {}  {}  {}".format(n171, n172, n173))
devide()


#Задание 1.8
n181 = random.randint(1, 11)
n182 = random.randint(11, 21) 
n183 = random.randint(21, 31)
n184 = random.randint(31, 41)
print("1.8 Вывести на экран в одну строку четыре любые числа через один пробел: {} {} {} {}".format(n181, n182, n183, n184))
devide()


#Задание 1.9
print("1.9 Вывести на экран числа 50 и 10 одно под другим: \n", 50, "\n", 10)
devide()


#Задание 1.10
print("1.10 Вывести на экран числа 5, 10 и 21 одно под другим:\n{}\n{}\n{}".format(5, 10, 21))
devide()


#Задание 1.11
n1111 = random.randint(1, 11)
n1112 = random.randint(11, 21)
n1113 = random.randint(21, 31)
n1114 = random.randint(31, 41)
print("1.11 Вывести на экран столбиком четыре любых числа:\n{}\n{}\n{}\n{}".format(n1111, n1112, n1113, n1114))
devide()


#Задание 1.12
print("1.12 Вывод по столбикам")
t112 = int(input("Введите число для переменной t :"))
v112 = int(input("Введите число для переменной v :"))
x112 = int(input("Введите число для переменной x :"))
y112 = int(input("Введите число для переменной y :"))
print("Вариант А:\n{} {}\n{} {}".format(5, 10, 7, "см"))
print("Вариант Б:\n{} {}\n{} {}".format(100, t112, 1949, v112))
print("Вариант В:\n{} {}\n{} {}".format(x112, 25, x112, y112))
devide()


#Задание 1.13
print("1.13 Вывод по столбикам")
#Ввод данных используется от предыдущего задания
print("Вариант А:\n{} {}\n{} {}".format(2, "кг", 13, 17))
print("Вариант Б:\n{} {}\n{} {}".format(t112, 1, 19, v112))
print("Вариант В:\n{} {}\n{} {}".format(x112, y112, 5, y112))
devide()


#Задание 1.14
x114 = 68
y114 = 41
a114 = 23
b114 = 43
n114 = -53
alpha114 = 1
beta114 = -1
print("1.14 Запись математических выражений.")
print("Вариант А : {}".format(2*x114))
print("Вариант Б : {}".format(math.sin(x114)))
print("Вариант В : {}".format(math.pow(a114, 2)))
print("Вариант Г : {}".format(math.sqrt(x114)))
print("Вариант Д : {}".format(math.fabs(n114)))
print("Вариант Е : {}".format(5 * math.cos(y114)))
print("Вариант Ж : {}".format(-7,5 * math.pow(a114,2)))
print("Вариант З : {}".format(3 * math.sqrt(x114)))
print("Вариант И : {}".format(math.sin(alpha114) * math.cos(beta114) + math.cos(alpha114) * math.sin(beta114)))
print("Вариант К : {}".format(a114 * math.sqrt(2 * b114)))
print("Вариант Л : {}".format(3 * math.sin(2 * alpha114) * math.cos(3 * beta114)))
print("Вариант М : {}".format(-5 * math.sqrt(x114 + math.sqrt(y114))))
devide()


#Задание 1.15
c115 = 12
print("1.15 Получить линейную запись выражений.")
print("Вариант А : {}".format(-1 / math.pow(x114, 2)))
print("Вариант Б : {}".format(a114 / (b114 * c115)))
print("Вариант В : {}".format((a114 / b114) * c115))
print("Вариант Г : {}".format((a114 + b114) / 2))
print("Вариант Д : {}".format(5,45 * ((a114 + 2 * b114) / (2 - a114))))
print("Вариант Е : {}".format((-b114 + math.sqrt(math.pow(b114,2) - 4 * a114 * c115)) / 2 * a114))
print("Вариант Ж : {}".format((-b114 + (1 / a114)) / (2 / c115)))
print("Вариант З : {}".format(1 / (1 + ((a114 + b114) / 2))))
print("Вариант И : {}".format(1 / (1 + (1 / (2 + (1 / (2 + (3 / 5))))))))
m115 = 3
n115 = 2
print("Вариант К : {}".format(math.pow(2, math.pow(m115, n115))))
devide()


#Задание 1.16
R116 = 2
d116 = 7
print("1.16 Перевести из линейной записи в обычную.")
print("Вариант А : {}".format(a114 / b114 / c115))
print("Вариант Б : {}".format(a114 * (b114 / c115)))
print("Вариант В : {}".format((a114 / b114) * c115))
print("Вариант Г : {}".format(a114 + (b114 / c115)))
print("Вариант Д : {}".format((a114 + b114) / c115))
print("Вариант Е : {}".format(a114 + (b114 / (b114 + c115))))
print("Вариант Ж : {}".format((a114 + b114) / (b114 + c115)))
print("Вариант З : {}".format(a114 / math.sin(b114)))
print("Вариант И : {}".format(1 / 2 * a114 * b114 * math.sin(x114)))
print("Вариант К : {}".format((2 * b114 * c115 * math.cos(a114 / 2)) / (b114 + c115)))
print("Вариант Л : {}".format(4 * R116 * math.sin(a114 / 2) * math.sin(b114 / 2) * math.sin(c115 / 2)))
print("Вариант М : {}".format((a114 * (x114 + b114)) / ((c115 * x114) + d116)))
print("Вариант Н : {}".format(((2 * math.sin(a114 + b114)) / (2 * math.cos(a114 - b114))) / 2))
print("Вариант О : {}".format(math.fabs(2 * math.sin(-3 * math.fabs(x114 / 2)))))
devide()


#Задание 1.17
I117 = 17
print("1.17 Записать математические выражения.")
print("Вариант В : {}".format((v112 * t112) + (a114 * math.pow(t112, 2) / 2)))
print("Вариант Ж : {}".format(2 * math.pi * R116))
print("Вариант К : {}".format(math.pow(I117, 2) * R116))
print("Вариант Л : {}".format(a114 * b114 * math.sin(c115)))
devide()


#Задание 1.18
print("1.18 Указать значение величины s после выполнения операторов присваивания.")
s118 = -7.5
s118 = 2 * s118
print("Вариант В : {}".format(s118))
devide()


#Задание 1.20
print("1.20 Указать значения величин s и k после выполнения операторов присваивания.")
s120 = 14
k120 = -3
d120 = s120 + 1
s120 = d120
k120 = 2 * s120
print("Вариант А, s = {}, k = {}.".format(s120, k120))
devide()


#Вычисления по известным формулам


#Задание 1.22
print("1.22 Вычисление значения функции.")
x122 = random.randint(1, 11)
print("Вариант А, вычисление значения функции y = 7x²-3x+6 при любом значении x")
print("Значение x: {}, решение: y = {}".format(x122, (7 * math.pow(x122, 2)) - (3 * x122) + 6))
devide()


#Задание 1.23
print("1.23 Вычисление значения функции.")
a123 = random.randint(1, 11)
print("Вычисление значения функции y = (a*a + 10) / sqrt(a*a+1) при любом значении a")
print("Значение a: {}, решение: y = {}".format(a123, (a123 * a123 + 10) / math.sqrt(a123 * a123 + 1)))
devide()


#Задание 1.24
print("1.24 Вычисление значения функции.")
a124 = random.randint(1, 11)
print("Вариант А, вычисление значения функции x = sqrt((2a+sin|3a|)/3,56) при любом значении a")
print("Значение a: {}, решение: x = {}".format(a124, math.sqrt((2 * a124 + math.sin(math.fabs(3 * a124))) / 3.56)))
#В модуле тут нет никакого смысла, так как при отрицательном значении а выражение
#под корнем в любом случае будет отрицательным и интерпретатор будет ругаться на этот счет.
devide()


#Задание 1.25
print("1.25 Вычисление периметра квадрата.")
square_side125 = random.randint(1, 11)
print("Периметр квадрата со стороной {} равен {}.".format(square_side125, square_side125*4))
devide()


#Задание 1.26
print("1.26 Вычисление диаметра окружности.")
circle_radius126 = random.randint(1, 11)
print("Диаметр окружности с радиусом {} равен {}.".format(circle_radius126 , circle_radius126*2))
devide()


#Задание 1.27
print("1.27 Вычисление расстояния до горизонта.")
earth_ideal_radius127 = 6350
point_of_view127 = random.randint(1,11)
distance127 = math.pow(math.pow(earth_ideal_radius127+point_of_view127, 2) - math.pow(earth_ideal_radius127, 2), 0.5)
print("При высоте точки обзора в {} км, расстояние до горизонта равно {} км.".format(point_of_view127, distance127))
print("По другой формуле {} км.".format(1.06 * math.sqrt(point_of_view127 * (2 * earth_ideal_radius127 + point_of_view127))))
devide()


#Задание 1.28
print("1.28 Куб.")
cube_side128 = random.randint(1, 11)
print("Длинна ребра куба: {}, объем: {}, площадь боковой поверхности: {}".format(cube_side128, math.pow(cube_side128, 3), math.pow(cube_side128, 2)))
devide()


#Задание 1.29
print("1.29 Окружность.")
circle_radius129 = random.randint(1, 11)
print("Радиус окружности: {}, длинна окружности: {}, площадь круга: {}".format(circle_radius129, 2 * math.pi * circle_radius129, math.pi * math.pow(circle_radius129, 2)))
devide()


#Задание 1.30
print("1.30 Вычислить значения функции при любых значениях x и y")
print("Функция z = x^3 - 2,5xy+1,78x^2-2,5y+1")
x130 = random.randint(1, 11)
y130 = random.randint(11, 21)
print("Значения x и y: {} {}, решение: {}".format(x130, y130, math.pow(x130, 3) - 2.5 * x130 * y130 + 1.78 * math.pow(x130, 2) - 2.5 * y130 + 1))
devide()


#Задание 1.31
print("1.31 Найти среднее арифметическое и геометрическое для двух целых чисел.")
x131 = random.randint(1, 11)
y131 = random.randint(11, 21)
print("Значения x и y: {} {}, среднее арифметическое: {}, среднее геометрическое: {}".format(x131, y131, (x131 + y131)/2, math.pow((x131 * y131), 1 / 2)))
devide()


#Задание 1.32
print("1.32 Определить плотность тела - 1 кг ртути, объем 0,07382 литра")
print("Плотность тела: {} г/см3".format(1 * 1000/(0.07382 * 1000)))
devide()


#Задание 1.33
print("1.33 Определить плотность населения в государстве")
square132 = random.randint(20, 40)
density132 = random.randint(2000, 4000)
print("Площадь государства: {} км2, объем населения: {} чел, плотность населения: {} чел/км2".format(square132, density132, density132 / square132))
devide()