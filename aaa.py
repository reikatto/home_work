import math


class Vector2D:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Vector2D({}, {})".format(self.x, self.y)

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

    def length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def angle(self):
        return math.atan2(self.y, self.x)

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def dot(self, other):
        return self.x * other.x + self.y * other.y
v1 = Vector2D(3, 4)
v2 = Vector2D(1, 2)
v3 = v1 + v2
v4 = v1 - v2
dotproduct = v1.dot(v2)
print(v1.length())          #Вычисление длины
print(v1.angle())           #Вычисление угла наклона вектора по отношению к положительному направлению оси абсцисс
print(v3)                   #Сумма
print(v4)                   #Разность
print(dotproduct)          #Скалярное произведение