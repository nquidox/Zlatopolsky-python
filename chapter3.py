#Задачник Златопольского, Глава 2.

import math
import random


#Разделитель текста в терминале просто для удобства чтения вывода
def devide():
    print("\n")

#Начало

# Вычисление логических выражений

#Задание 3.1, 3.3, 3.5
print("3.1 Вычислить значение логического выражения при следующих значениях \n \
логических величин А, В и С: А = Истина, В = Ложь, С = Ложь:")
a31 = True
b31 = False
c31 = False

#3.1
print("3.1")
rez31_1 = a31 or b31
rez31_2 = a31 and b31
rez31_3 = b31 or c31
print("А или В: {}.".format(rez31_1))
print("А и В: {}.".format(rez31_2))
print("В или С: {}.".format(rez31_3))

#3.3
print("3.3")
rez33_1 = not a31 and b31
rez33_2 = a31 or not b31
rez33_3 = a31 and b31 or c31
print("не А и В: {}.".format(rez33_1))
print("А или не В: {}.".format(rez33_2))
print("А и В или С: {}.".format(rez33_3))

#3.5
print("3.5")
rez35_1 = a31 or b31 and not c31
rez35_2 = not a31 and not b31
rez35_3 = not (a31 and c31) or b31
rez35_4 = a31 and not b31 or c31
rez35_5 = a31 and (not b31 or c31)
rez35_6 = a31 or (not (b31 and c31))
print("А или В и не С: {}.".format(rez35_1))
print("не А и не В: {}.".format(rez35_2))
print(" не (А и С) или В: {}.".format(rez35_3))
print("А и не В или С: {}.".format(rez35_4))
print("А и (не В или С): {}.".format(rez35_5))
print("А или (не (В и С)): {}.".format(rez35_6))
devide() 

#3.7 и 3.9 аналогичны, только выражения длиннее

#Задание 3.11
print("3.11 Вычислить значение логического выражения.")

xa311 = 1
ya311 = -1
a311 = math.pow(xa311, 2) + math.pow(ya311, 2)<=4
print("a) x^2 + y^2 <= 4 при x=1 y=-1: {}.".format(a311))

xg311 = 2
yg311 = 1
g311 = (xg311 * yg311 != 0) and (yg311 > xg311)
print("г) (x * y != 0) и (y > x) при x=2 y=1: {}.".format(g311))

xd311 = 2
yd311 = 1
d311 = (xd311 * yd311 != 0) or (yd311 < xd311)
print("д) (x * y != 0) или (y < x) при x=2 y=1: {}.".format(d311))
devide() 


#Задание 3.13
print("3.11 Вычислить значение логического выражения при всех возможных значениях \n \
логических величин А и В:")
a313 = True
b313 = False
print("Значения А и В: {}, {}".format(a313, b313))
print("a) не (А и В): {}".format(not(a313 and b313)))
print("б) не А или В: {}".format(not a313 or b313))
print("в) А или не В: {}".format(a313 or not b313))
devide() 

a313 = False
b313 = True
print("Значения А и В: {}, {}".format(a313, b313))
print("a) не (А и В): {}".format(not(a313 and b313)))
print("б) не А или В: {}".format(not a313 or b313))
print("в) А или не В: {}".format(a313 or not b313))
devide() 

a313 = True
b313 = True
print("Значения А и В: {}, {}".format(a313, b313))
print("a) не (А и В): {}".format(not(a313 and b313)))
print("б) не А или В: {}".format(not a313 or b313))
print("в) А или не В: {}".format(a313 or not b313))
devide() 

a313 = False
b313 = False
print("Значения А и В: {}, {}".format(a313, b313))
print("a) не (А и В): {}".format(not(a313 and b313)))
print("б) не А или В: {}".format(not a313 or b313))
print("в) А или не В: {}".format(a313 or not b313))
devide() 


#Задания до 3.26 аналогичны


#Задание 3.30
print("3.30 Записать условие, которое является истинным, когда: ")
a330 = random.randint(1, 10)
print("а) целое А кратно двум или трем: {}, {}".format(a330, a330 % 2 == 0 or a330 % 3 == 0))
print("б) целое А не кратно трем и оканчивается нулем: {}, {}".format(a330, a330 % 3 != 0 and a330 % 10 == 0))
devide()


#Задание 3.31
print("3.31 Записать условие, которое является истинным, когда: ")
n331 = random.randint(1, 10)
print("а) целое N кратно пяти или семи: {}, {}".format(n331, n331 % 5 == 0 or n331 % 7 == 0))
print("б) целое N кратно четырем и не оканчивается нулем: {}, {}".format(n331, n331 % 4 == 0 and n331 % 10 != 0))
devide()


#Остальные задачи пропустил, потому что они простые и не интересные.


print("Конец заданий второй главы.")


#Расскоментируйте следующую строку, чтоб окно терминала не закрывалось сразу после выполнения скрипта.
#input()