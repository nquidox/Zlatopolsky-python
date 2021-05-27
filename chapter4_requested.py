# Zlatopolsky Chapter 4 requested tasks: 4.116 - 4.141


# 4.118
print("Task 4.118")
a3, a2, a1 = 4, 3, 2
b2, b1 = 6, 9
print("Initial values:\na3 = %s, a2 = %s, a1 = %s \nb2 = %s, b1 = %s\n" % (a3, a2, a1, b2, b1))

a = (a3 * 100) + (a2 * 10) + a1
b = (b2 * 10) + b1

result_simple = a + b
print("Awaiting result = %s\n" % result_simple)


c3, c2, c1 = 0, 0, 0

if a1 + b1 > 9:
	c2 += (a1 + b1) // 10
	c1 = (a1 + b1) % 10
else:
	c1 = a1 + b1

if a2 + b2 + c2 > 9:
	c3 += (a2 + b2 + c2) // 10
	c2 = (a2 + b2 + c2) % 10
else:
	c2 = a2 + b2 + c2

c3 += a3

print("Final numbers: c3 = %s, с2 = %s, c1 = %s" % (c3, c2, c1))
result = (c3 * 100) + (c2 * 10) + c1
print("Are results equal?", result == result_simple)
print()


# 4.120
print("Task 4.118")
# г) белая ладья и черный слон
# chessboard-1.jpg
print("Problem 1")
rook1   = [6, 4]
bishop1 = [2, 5]
point1  = [3, 4]

if point1[0] == bishop1[0] + 1 and point1[1] == bishop1[1] - 1:
	print("Point is unsafe")
else:
	print("Point is safe")
print()

# з) белый ферзь и черный слон
# chessboard-2.jpg
print("Problem 2")
queen2  = [3, 2]
bishop2 = [5, 6]
point2  = [3, 6]
bishop2_attack = [(1, 2), (2, 3), (3, 4), (4, 5), (6, 7), (7, 8), (3, 8), (4, 7), (6, 5), (7, 4), (8, 3)]

if point2 in bishop2_attack:
	print("Point is unsafe")
else:
	print("Point is safe")
print()

# 4.122-124
a, b, c = 9, 12, 15


if any((a <= b + c, b <= a + c, c <= a + b)):
	print("Triange can be done")
else:
	print("Triangle can't be done")


if any(((a * a) == (b * b) + (c * c), (b * b) == (a * a) + (c * c), (c * c) == (a * a) + (b * b))):
	print("Triangle is right-angle")
else:
	print("Triangle is not right-angle")

import math
angle_a = math.degrees(math.acos((math.pow(a, 2) + math.pow(c, 2) - math.pow(b, 2)) / (2 * a * c)))
angle_b = math.degrees(math.acos((math.pow(a, 2) + math.pow(b, 2) - math.pow(c, 2)) / (2 * a * b)))
angle_c = math.degrees(math.acos((math.pow(b, 2) + math.pow(c, 2) - math.pow(a, 2)) / (2 * c * b)))

if any((angle_a > 90, angle_b > 90, angle_c > 90)):
	print("Triangle is tupoi")

if any((angle_a == 90, angle_b == 90, angle_c == 90)):
	print("Triangle is right-angle")

if angle_a < 90 and angle_a < 90 and angle_a < 90:
	print("Triangle is ostriy")

if any((angle_a == angle_b, angle_b == angle_c, angle_a == angle_c)):
	print("Triangle is ravnobedrenniy")

if angle_a == angle_b == angle_c:
	print("Triangle is ravnostoronniy")

print(angle_a, angle_b, angle_c)


