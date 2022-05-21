# Python 3.10.0
"""
Задание 1
Разработать класс Sphere для представления сферы в трехмерном
пространстве.
"""

import math


class Sphere:

    def __init__(self, r: float = 1.0, cx: float = 0.0, cy: float = 0.0, cz: float = 0.0):
        """
        :param r: действительное число, по умолчанию 1.0
        :param cx: действительное число, по умолчанию 0.0
        :param cy: действительное число, по умолчанию 0.0
        :param cz: действительное число, по умолчанию 0.0
        """
        self.r = r
        self.cx = cx
        self.cy = cy
        self.cz = cz

    def get_volume(self) -> float:
        """
        Возвращает действительное число — объем шара, ограниченной текущей сферой.
        """
        V = 4.0 / 3.0 * math.pi * self.r ** 3
        return V

    def get_square(self) -> float:
        """
        Возвращает действительное число — площадь внешней поверхности сферы.
        """
        square = 4 * math.pi * self.r ** 2
        return square

    def get_radius(self) -> float:
        """
        Возвращает действительное число — радиус сферы.
        """
        return self.r

    def get_center(self) -> tuple:
        """
        Возвращает тьюпл с 3 действительными числами — координатами центра сферы
        в том же порядке, в каком они задаются в конструкторе.
        """
        center = (self.cx, self.cy, self.cz)
        return center

    def set_radius(self, r: float) -> None:
        """
        Меняет радиус текущей сферы, ничего не возвращая.
        """
        self.r = r

    def set_center(self, x: float, y: float, z: float) -> None:
        """
        Меняет координаты центра сферы, ничего не возвращая.
        """
        self.cx = x
        self.cy = y
        self.cz = z

    def is_point_inside(self, x: float, y: float, z: float) -> bool:
        """
        Возвращает логическое значение True или False в зависимости от того, находится эта точка внутри сферы
        """
        x1 = math.pow((x - self.cx), 2)
        y1 = math.pow((y - self.cy), 2)
        z1 = math.pow((z - self.cz), 2)

        point = (x1 + y1 + z1)

        if point < (self.r ** 2):
            return True
        return False


if __name__ == '__main__':
    s0 = Sphere(0.5)
    print(s0.get_volume())
    print(s0.get_square())
    print(s0.get_radius())
    print(s0.get_center(), type(s0.get_center()))
    s0.set_radius(3.0)
    print(s0.get_radius())
    s0.set_center(1.0, 1.0, 1.0)
    print(s0.get_center(), type(s0.get_center()))
    print(s0.is_point_inside(10, 10, 10))
    print(s0.get_radius())
