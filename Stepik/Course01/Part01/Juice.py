# Класс "Сок"
class Juice:
    # Магический метод инициализации экземпляра класса
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity

    # Магический метод строкового представления объекта
    def __str__(self):
        return f'{self.name} ({self.capacity}L)'

    # Магический метод перегрузки оператора сложения
    def __add__(self, other):
        # Создаем новый объект Juice, который представляет собой смесь двух соков
        new_name = f'{self.name}&{other.name}'
        new_capacity = self.capacity + other.capacity
        return Juice(new_name, new_capacity)

    def func(self):
        pass


# Пример использования класса Juice
a = Juice('Orange', 1.5)
b = Juice('Apple', 2.0)

# Складываем два объекта типа Juice и выводим результат
result = a + b
print(result)
