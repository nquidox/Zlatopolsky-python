#Задачник Златопольского, Глава 4.

import random
import math


#Разделитель текста в терминале просто для удобства чтения вывода
def devide():
    print("\n")

#Начало
 

#Простой условный оператор


#Задание 4.1
print("4.1 Рассчитать значение у при заданном значении х.")

x41 = random.randint(-11, 11)
print("x = {}".format(x41))

if x41 > 0:
    y = math.pow(math.sin(x41), 2)
    print("y = sin^2(x) при x > 0: y = {}".format(y))

else:
    y = 1 + 2 * math.pow(math.sin(x41), 2)
    print("y = 1 - 2 * sin(x^2) в остальных случаях: y = {}".format(y))
devide()


# Задачи до 4.5 включительно практически аналогичные.


#Задание 4.8
print("4.8 Известны два расстояния: одно в километрах, другое — в футах. Какое из расстояний меньше?")
kilometers48 = random.randint(1, 100)
foots48 = random.randint(1, 1000)

if kilometers48 > foots48 * 0.305:
    print("Расстояние в километрах больше.")

elif kilometers48 < foots48 * 0.305:
    print("Расстояние в футах больше.")

else:
    print("Расстояния одинаковы.")
devide()


#Задание 4.13 + 14
print("4.13 Даны вещественные числа a, b, c (a != 0). Выяснить, имеет ли уравнение ax^2+bx+c=0 вещественные корни.")
print("4.14 Найти корни уравнения при их наличии.")
a413 = random.randint(1, 3)
b413 = random.randint(-2, 2)
c413 = random.randint(-3, 3)

discr413 = (math.pow(b413, 2) - 4 * a413 * c413)

if discr413 < 0:
    print("Дискриминант меньше ноля {}, корней нет.".format(discr413))

elif discr413 == 0:
    root413_1 = -b413 + math.sqrt(discr413) / 2 * a413
    print("Дискриминант равен нолю {}, один корень: {}".format(discr413, root413_1))

elif discr413 > 0:
    root413_2 = -b413 + math.sqrt(discr413) / 2 * a413
    root413_3 = -b413 - math.sqrt(discr413) / 2 * a413
    print("Дискриминант больше ноля {}, два корня: {}, {}".format(discr413, root413_2, root413_3))
devide()


#Задание 4.15
#Странная задача, максимум можно сравнить только года на совпадение.
#Поскольку это совсем примитив - пропускаю.


#Задание 4.16
print("4.16 Известны площади круга и квадрата. Определить:")
s416_circle = random.randint(1, 11)
s416_square = random.randint(1, 11)

circle_radius416 = math.sqrt(s416_circle / math.pi)
outer_radius416 = math.sqrt(2 * s416_square) / 2
inner_radius416 = math.sqrt(s416_square) / 2

if circle_radius416 >= outer_radius416:
    print("Квадрат уместится в круге.")

elif circle_radius416 <= inner_radius416:
    print("Круг уместится в квадрате")

else:
    print("Ни какая фигура не уместится в другой фигуре.") 
devide()

#Целочисленная арифметика и условный оператор
#Пропущено


#Использование сложных условий


#Задание 4.37
print("4.37 Проверить, принадлежит ли число, введенное с клавиатуры, интервалу (–5, 3).")

input_num437 = random.randint(-11, 11)

if input_num437 >= -5 and input_num437 <= 3:
    print("Число {} попадает в указанный интервал.".format(input_num437))

else:
    print("Число {} НЕ попадает в указанный интервал.".format(input_num437))
devide()


#4.38 - 39 аналогичны предыдущей задаче


#Задание 4.41
print("4.41 Дано вещественное число x. Вычислить f(x)")

x441 = random.uniform(0.1, 2.0)

if x441 >= 0.2 and x441 <= 0.9:
    print(math.sin(x441))

else:
    print(1)
devide()


#Задание 4.42
print("4.42 Даны три вещественных числа a, b, c.")

a442 = random.randint(1, 11)
b442 = random.randint(1, 11)
c442 = random.randint(1, 11)
rez_1, rez_2 = False, False

if all((a442 < b442, b442 < c442)):
    rez_1 = True

if all((b442 > a442, a442 > c442)):
    rez_2 = True

print(a442, b442, c442)
print("а) выполняется ли неравенство a < b < c, {}".format(rez_1))
print("б) выполняется ли неравенство b > a > c, {}".format(rez_2))
devide()


#Задание 4.45
print("4.45 Даны три вещественных числа a, b, c. Определить, имеется ли среди них хотя бы одна пара равных между собой чисел.")

a445 = random.randint(1, 11)
b445 = random.randint(1, 11)
c445 = random.randint(1, 11)

print(a445, b445, c445)

if any((a445 == b445, b445 == c445, a445 == c445)):
    print("Есть хотя бы одна пара равных чисел.")
devide()


#Задание 4.49
#Аналогично 4.13 + 14, просто с элементарной проверкой равенства корней.


#Задание 4.52
print("4.52 Вася пытается высунуть голову в форточку размерами a и b см.  \n \
Приняв условно, что его голова — круглая диаметром d см, определить,  \n \
сможет ли Вася сделать это. Для прохождения головы в форточку необходим зазор  \n \
в 1 см с каждой стороны.")

fort_a452 = random.randint(1, 11)
fort_b452 = random.randint(1, 11)
head_d452 = random.randint(1, 11)

fort_square452 = fort_a452 * fort_b452
fort_inner_radius452 = math.sqrt(fort_square452) / 2
head_radius452 = (head_d452 - 2) / 2

if head_radius452 >= fort_inner_radius452:
    print("Голова Васи пролезет в форточку.")

else:
    print("Голова Васи НЕ пролезет в форточку.")
devide()


#Задание 4.53
print("4.53 Даны вещественные положительные числа a, b, c, x, y. Выяснить, пройдет ли\n \
кирпич с ребрами a, b, c в прямоугольное отверстие со сторонами x и y. \n \
Просовывать кирпич в отверстие разрешается только так, чтобы каждое из его \n \
ребер было параллельно или перпендикулярно каждой из сторон отверстия.\n")

a453 = random.randint(1, 11)
b453 = random.randint(1, 11)
c453 = random.randint(1, 11)
x453 = random.randint(1, 11)
y453 = random.randint(1, 11)

if any((a453 <= x453 and b453 <= y453, a453 <= x453 and c453 <= y453, b453 <= x453 and c453 <= y453)):
    print("Кирпич пролезет в отверстие.")

else:
    print("Кирпич НЕ пролезет в отверстие.")
devide()


#Задание 4.56
print("4.56 Дано двузначное число. Определить:")

a456 = random.randint(10, 99)
rez_a456, rez_b456 = False, False
tens456 = a456 // 10
ones456 = a456 % 10

if any((tens456 == 4, tens456 == 7, ones456 == 4, tens456 == 7)):
    rez_a456 = True

if any((tens456 == 3, tens456 == 6, tens456 == 9, ones456 == 3, ones456 == 6, ones456 == 9)):
    rez_b456 = True    

print("Двузначное число: {}".format(a456))
print("а) входят ли в него цифры 4 или 7: {}".format(rez_a456))
print("б) входят ли в него цифры 3, 6 или 9: {}".format(rez_b456))
devide()


#Задание 4.61
print("4.61 Дано натуральное число n (n<=9999). Выяснить, является ли оно палиндромом.")

palin_num461 = random.randint(1000, 9999)
#palin_num461 = 1221
thou461 = palin_num461 // 1000
hund461 = palin_num461 % 1000 // 100
tens461 = palin_num461 % 100 // 10
ones461 = palin_num461 % 10

if thou461 * 10 + hund461 == ones461 * 10 + tens461:
    print("Число {} является палиндромом.".format(palin_num461))

else:
    print("Число {} НЕ является палиндромом.".format(palin_num461))
devide()


#Задание 4.62
print("4.62 Дано натуральное число n (n<=9999). Выяснить, верно ли, что это число \n \
содержит ровно три одинаковые цифры с учетом четырех цифр.")

num462 = random.randint(1000, 9999)
thou462 = num462 // 1000
hund462 = num462 % 1000 // 100
tens462 = num462 % 100 // 10
ones462 = num462 % 10

cond462_1 = thou462 == hund462 and thou462 == tens462 and ones462 != thou462
cond462_2 = thou462 == hund462 and thou462 == ones462 and tens462 != thou462
cond462_3 = thou462 == tens462 and thou462 == ones462 and hund462 != thou462
cond462_4 = hund462 == tens462 and hund462 == ones462 and thou462 != hund462

if any((cond462_1, cond462_2, cond462_3, cond462_4)):
    print("Число {} содержит ровно 3 одинаковые цифры.".format(num462))

else:
    print("Число {} НЕ содержит ровно 3 одинаковые цифры.".format(num462))
devide()


#Задание 4.65 
print("4.65 Проверка високосности года.")
random_year465 = random.randint(400, 2500)

if random_year465 % 4 == 0 and random_year465 % 400 == 0:
    print("Год {} является високосным.".format(random_year465))

else:
    print("Год {} НЕ является високосным.".format(random_year465))
devide()


#Задание 4.67 
print("4.67 Определить каким днем недели будет случайный день года, \n \
если 1 января - понедельник.")
random_day467 = random.randint(1, 365)

if random_day467 % 7 == 1:
    print("{} день года - понедельник, рабочий день.".format(random_day467))

elif random_day467 % 7 == 2:
    print("{} день года - вторник, рабочий день.".format(random_day467))

elif random_day467 % 7 == 3:
    print("{} день года - среда, рабочий день.".format(random_day467))

elif random_day467 % 7 == 4:
    print("{} день года - четверг, рабочий день.".format(random_day467))

elif random_day467 % 7 == 5:
    print("{} день года - пятница, рабочий день.".format(random_day467))

elif random_day467 % 7 == 6:
    print("{} день года - суббота, выходной день.".format(random_day467))

elif random_day467 % 7 == 1:
    print("{} день года - воскресенье, выходной день.".format(random_day467))
devide()


#Задание 4.70
print("4.70 .Даны два различных вещественных числа. Определить наибольшее из них, \n \
не используя полный условный оператор, а применив:\n")

#а) два неполных условных оператора
a470 = random.randint(1, 11)
b470 = random.randint(1, 11)
print ("а) два неполных условных оператора. Числа: {}, {}.".format(a470, b470))
min470 = 0
max470 = 0

if a470 > b470:
    min470 = b470
    max470 = a470
    print("a1) {} наименьшее, {} набольшее.".format(min470, max470))

if a470 < b470:
    min470 = a470
    max470 = b470
    print("a2) {} наименьшее, {} набольшее.".format(min470, max470))
devide()


#б) один неполный условный оператор
a470 = random.randint(1, 11)
b470 = random.randint(1, 11)
print ("б) один неполный условный оператор. Числа: {}, {}.".format(a470, b470))
min470 = 0
max470 = 0

if a470 > b470:
    min470 = b470
    max470 = a470
    print("б1) {} наименьшее, {} набольшее.".format(min470, max470))

min470 = a470
max470 = b470
print("б2) {} наименьшее, {} набольшее.".format(min470, max470))
devide()


#Задание 4.77
print("4.77 Даны два числа. Если квадратный корень из второго числа меньше первого\n \
числа, то увеличить второе число в пять раз.")
num1_477 = random.randint(1, 11)
num2_477 = random.randint(1, 11)

print(num1_477, num2_477)

if math.sqrt(num2_477) < num1_477:
    num2_477 *= 5

print(num2_477)
devide()


#Задание 4.78 - 80
num1_477 = random.randint(-11, 11)
num2_477 = random.randint(-11, 11)
num3_477 = random.randint(-11, 11)
print("4.78 - 80 Даны три целых числа: {}, {}, {}.".format(num1_477, num2_477, num3_477))

print("Вывести на экран те из них, которые являются четными.")
if num1_477 % 2 == 0:
    print(num1_477)

if num2_477 % 2 == 0:
    print(num2_477)

if num3_477 % 2 == 0:
    print(num3_477)
devide()

print("Возвести в квадрат те из них, значения которых неотрицательны.")
if num1_477 >= 0:
    print(math.pow(num1_477, 2))

if num2_477 >= 0:
    print(math.pow(num2_477, 2))

if num3_477 >= 0:
    print(math.pow(num3_477, 2))
devide()

print("Вывести на экран те из них, которые принадлежат интервалу (1,6—3,8)")
if num1_477 >= 1.6 and num1_477 <= 3.8:
    print(num1_477)

if num2_477 >= 1.6 and num2_477 <= 3.8:
    print(num2_477)

if num3_477 >= 1.6 and num3_477 <= 3.8:
    print(num3_477)
devide()

print("Вывести на экран те из них, которые принадлежат интервалу (0,7—5,1)")
if num1_477 >= 0.7 and num1_477 <= 5.1:
    print(num1_477)

if num2_477 >= 0.7 and num2_477 <= 5.1:
    print(num2_477)

if num3_477 >= 0.7 and num3_477 <= 5.1:
    print(num3_477)
devide()



#Задание 4.81
print("4.81. Даны четыре вещественных числа. Определить, сколько из них отрицательных.")
num1_481 = random.randint(-11, 11)
num2_481 = random.randint(-11, 11)
num3_481 = random.randint(-11, 11)
num4_481 = random.randint(-11, 11)
counter481 = 0

if num1_481 < 0:
    counter481 += 1

if num2_481 < 0:
    counter481 += 1

if num3_481 < 0:
    counter481 += 1

if num4_481 < 0:
    counter481 += 1

print("Числа: {}, {}, {}, {}.".format(num1_481, num2_481, num3_481, num4_481))
print("Количество отрицательных чисел: {}.".format(counter481))
devide()


#Задачи до 4.103 включительно пропущены. 


#В python нет конструкции типа switch case, как вариант предлагают использовать словари
#но делать этого в этой главе я не буду


#Все оставшиеся задачи до конца главы пропущены.


print("Конец заданий четвертой главы.")

#Расскоментируйте следующую строку, чтоб окно терминала не закрывалось сразу после выполнения скрипта.
#input()