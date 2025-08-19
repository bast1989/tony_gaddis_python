import random

# Класс Coin имитирует монету, которую
# можно подбрасывать.

class Coin:

    # Метод __init__ инициализирует
    # атрибут данных __sideup значением 'Орел'.

    def __init__(self):
        self.__sideup = 'Орёл'

    # Метод toss генерирует случайное число
    # в диапазоне от О до 1. Если это число
    # равно О, то __sideup получает значение 'Орел'.
    # В противном случае __sideup получает значение 'Решка'.

    def toss(self):
        if random.randint(0,1):
            self.__sideup = 'Орёл'
        else:
            self.__sideup = 'Решка'

    # Метод get_sideup возвращает значение,
    # на которое ссылается __sideup.

    def get_sideup(self):
        return self.__sideup