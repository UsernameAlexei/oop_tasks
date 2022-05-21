# Python 3.10.0
import unittest
from task1_Sphere import Sphere


class testSphere(unittest.TestCase):
    """
    Класс для тестирования задачи 1.
    """

    def setUp(self):
        self.s0 = Sphere(0.5)

    def test_get_volume(self):
        """
        Тестирование метода get_volume.
        Возвращает действительное число — объем шара
        """
        result = 0.5235987755982988
        self.assertEqual(self.s0.get_volume(), result)
        self.assertIsInstance(self.s0.get_volume(), float)

    def test_get_square(self):
        """
        Тестирование метода get_square.
        Возвращает действительное число — площадь внешней поверхности сферы
        """
        result = 3.141592653589793
        self.assertEqual(self.s0.get_square(), result)
        self.assertIsInstance(self.s0.get_square(), float)

    def test_get_radius(self):
        """
        Тестирование метода get_radius.
        Возвращает действительное число — радиус сферы.
        """
        result = 0.5
        self.assertEqual(self.s0.get_radius(), result)
        self.assertIsInstance(self.s0.get_radius(), float)

    def test_get_center(self):
        """
        Тестирование метода get_radius.
        Возвращает действительное число — радиус сферы.
        """
        result = (0.0, 0.0, 0.0)
        self.assertEqual(self.s0.get_center(), result)

    def test_set_radius(self):
        """
        Тестирование метода set_radius.
        Меняет радиус текущей сферы, ничего не возвращая.
        """
        self.s0.set_radius(1.6)
        self.assertEqual(self.s0.get_radius(), 1.6)

    def test_set_center(self):
        """
        Тестирование метода set_center.
        Меняет координаты центра сферы, ничего не возвращая.
        """
        self.s0.set_center(1.0, 1.0, 1.0)
        result = (1.0, 1.0, 1.0)
        self.assertEqual(self.s0.get_center(), result)

    def test_is_point_inside(self):
        """
        Тестирование метода is_point_inside.
        Ввозвращает логическое значение True или False в зависимости от того, находится эта точка внутри сферы.
        """
        self.assertFalse(self.s0.is_point_inside(0, -1.5, 0))
        self.s0.set_radius(1.6)
        self.assertTrue(self.s0.is_point_inside(0, -1.5, 0))