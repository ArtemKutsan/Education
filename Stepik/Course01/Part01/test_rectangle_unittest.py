import unittest  # импорт библиотеки для тестирования кода
from rectangle import Rectangle  # импорт класса "Прямоугольник" для его тестирования


class TestRectangle(unittest.TestCase):
    def setUp(self):
        self.rectangle = Rectangle(4, 3)

    def test_area(self):
        result = self.rectangle.area()
        self.assertEqual(result, 12)

    def test_perimeter(self):
        result = self.rectangle.perimeter()
        self.assertEqual(result, 14)


if __name__ == '__main__':
    unittest.main()