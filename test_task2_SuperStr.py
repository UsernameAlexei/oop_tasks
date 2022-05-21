# Python 3.10.0

import unittest
from task2_SuperStr import SuperStr


class testSuperStr(unittest.TestCase):
    """
    Класс для тестирования задачи 2.
    """

    def setUp(self) -> None:
        self.s = SuperStr('123123123123')
        self.p = SuperStr('123_321')

    def test_is_repeatance(self):
        """
        Тестирование метода is_repeatance.
        Возвращает True или False в зависимости от того,
        может ли строку быть получена целым количеством повторов строки.
        """
        self.assertTrue(self.s.is_repeatance('123'))
        self.assertTrue(self.s.is_repeatance('123123'))
        self.assertTrue(self.s.is_repeatance('123123123123'))
        self.assertFalse(self.s.is_repeatance('12312'))
        self.assertFalse(self.s.is_repeatance(123))

    def test_is_palindrom(self):
        """
        Тестирование метода is_palindrom.
        Возвращает True или False в зависимости от того, является ли строка палиндромом
        """
        self.assertFalse(self.s.is_palindrom())
        self.assertIsInstance(self.s, str)
        self.assertIsInstance(int(self.s), int)
        self.assertEqual(self.s + 'qwe', '123123123123qwe')
        self.assertTrue(self.p.is_palindrom())
