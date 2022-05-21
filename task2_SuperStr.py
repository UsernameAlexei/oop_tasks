# Python 3.10.0
"""
Задание 2
Разработать класс SuperStr, который наследует функциональность
стандартного типа str и содержит 2 новых метода:
    ● метод is_repeatance (s), который принимает 1 аргумент s и
    возвращает True или False в зависимости от того, может ли
    текущая строку быть получена целым количеством повторов
    строки s. Вернуть False, если s не является строкой. Считать, что
    пустая строка не содержит повторов.

    ● метод is_palindrom (), который возвращает True или False в
    зависимости от того, является ли строка палиндромом. Регистрами
    символов пренебрегать. Пустую строку считать палиндромом
"""


class SuperStr(str):

    def is_repeatance(self, s: str) -> bool:
        """
        Принимает 1 аргумент s и возвращает True или False в зависимости от того,
        может ли текущая строку быть получена целым количеством повторов строки s.
        Вернуть False, если s не является строкой. Считать, что пустая строка не содержит повторов
        """
        if not isinstance(s, str):
            return False
        n = len(self) // (len(s) or 1)
        return self == n * s

    def is_palindrom(self):
        """
        Возвращает True или False в зависимости от того, является ли строка палиндромом.
        Регистрами символов пренебрегать. Пустую строку считать палиндромом
        """
        s = self.lower()
        return s == s[::-1]


if __name__ == '__main__':
    s = SuperStr('123123123123')
    print(s.is_repeatance('123'))
    print(s.is_repeatance('123123'))
    print(s.is_repeatance('123123123123'))
    print(s.is_repeatance('12312'))
    print(s.is_repeatance(123))
    print(s.is_palindrom())
    print(type(s))
    print(type(int(s)))
    print(s + 'qwe')
    p = SuperStr('123_321')
    print(p.is_palindrom())
