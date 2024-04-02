# Класс "Проверка списка"
class ListChecker:
    @staticmethod
    def has_duplicates(input_list):
        '''
        Проверяет наличие дубликатов в списке.

        Args:
            input_list (list): Список для проверки на наличие дубликатов.

        Returns:
            bool: True, если в списке есть дубликаты, False в противном случае.
        '''
        return len(input_list) != len(set(input_list))
    

# Пример использования класса
checker = ListChecker()  # созданме объекта класса ListChecker

# Список для проверки на наличие дубликатов
input_list = [1, 2, 3, 4, 5]
# Проверяем список на наличие дубликатов
print(checker.has_duplicates(input_list))  # вывод: False

# Изменяем список, добавляя дубликат
input_list = [1, 2, 3, 4, 5, 5]
# Проверяем измененный список на наличие дубликатов
print(checker.has_duplicates(input_list))  # вывод: True

def func():
    pass

func()
