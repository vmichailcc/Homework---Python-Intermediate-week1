import math


class Point2D:

    _count = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y
        Point2D._count += 1

    def distance(self, point):
        dist = math.sqrt(((point.x - self.x) ** 2) + ((point.y - self.y) ** 2))
        return dist

    @property
    def count(self):
        return self._count


class Point3D(Point2D):

    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def distance(self, point):
        dist = math.sqrt(((point.x - self.x) ** 2) + ((point.y - self.y) ** 2) + ((point.z - self.z) ** 2))
        return dist


p1 = Point2D(1, 2)
p2 = Point2D(3, 4)
print("Pасстояние между 2мя точками на плоскости=", Point2D.distance(p1, p2))
print("Cчетчик созданных экземпляров класса-", Point2D._count)
p3 = Point3D(4, 5, 6)
p4 = Point3D(7, 8, 9)

print("Pасстояние между 2мя точками на плоскости=", Point3D.distance(p3, p4))
print("Cчетчик созданных экземпляров класса-",Point2D._count)
