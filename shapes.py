import math


class Shape:
    def __init__(self):
        pass

    def get_volume(self):
        pass

    def get_surface_area(self):
        pass


class Cube(Shape):
    def __init__(self, side):
        super().__init__()
        self.side = side

    def get_volume(self):
        return self.side ** 3

    def get_surface_area(self):
        return 6 * self.side ** 2


class Sphere(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def get_volume(self):
        return 4 / 3 * math.pi * self.radius ** 3

    def get_surface_area(self):
        return 4 * math.pi * self.radius ** 2


class Cylinder(Shape):
    def __init__(self, radius, height):
        super().__init__()
        self.radius = radius
        self.height = height

    def get_volume(self):
        return math.pi * self.radius ** 2 * self.height

    def get_surface_area(self):
        return 2 * math.pi * self.radius * (self.radius + self.height)


class Parallelepiped(Shape):
    def __init__(self, a, b, c):
        super().__init__()
        self.a = a
        self.b = b
        self.c = c

    def get_volume(self):
        return self.a * self.b * self.c

    def get_surface_area(self):
        return 2 * (self.a * self.b + self.b * self.c + self.c * self.a)


class Ellipsoid(Shape):
    def __init__(self, a, b, c):
        super().__init__()
        self.a = a
        self.b = b
        self.c = c

    def get_volume(self):
        return 4 / 3 * math.pi * self.a * self.b * self.c

    def get_surface_area(self):
        return 4 * math.pi * (
                    (self.a * self.b) ** (4 / 3) + (self.a * self.c) ** (4 / 3) + (self.b * self.c) ** (4 / 3)) / 3


def find_big_shapes(shapes):
    total_volume = 0
    big_shapes = []
    for shape in shapes:
        volume = shape.get_volume()
        total_volume += volume
    for shape in shapes:
        volume = shape.get_volume()
        if volume >= total_volume - volume:
            big_shapes.append(shape)
    return big_shapes


cube = Cube(4)
sphere = Sphere(3)
cylinder = Cylinder(2, 6)
parallelepiped = Parallelepiped(2, 3, 4)
ellipsoid = Ellipsoid(3, 4, 25)

print("Площадь поверхности куба:", cube.get_surface_area())
print("Объем куба:", cube.get_volume())
print("Площадь поверхности сферы:", sphere.get_surface_area())
print("Объем сферы:", sphere.get_volume())
print("Площадь поверхности цилиндра:", cylinder.get_surface_area())
print("Объем цилиндра:", cylinder.get_volume())
print("Площадь поверхности параллелепипеда:", parallelepiped.get_surface_area())
print("Объем параллелепипеда:", parallelepiped.get_volume())
print("Площадь поверхности эллипсоида:", ellipsoid.get_surface_area())
print("Объем эллипсоида:", ellipsoid.get_volume())

shapes = [cube, sphere, cylinder, parallelepiped, ellipsoid]
result = find_big_shapes(shapes)

if len(result) > 0:
    print("Найдены фигуры с объемом, равным или большим суммарному объему остальных фигур:")
    for shape in result:
        print(shape.__class__.__name__, "объем:", shape.get_volume())
else:
    print("Фигур с объемом, равным или большим суммарному объему остальных фигур, не найдено.")
