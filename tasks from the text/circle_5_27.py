# Модуль circle держит функции, которые выполняют
# вычисления, вязанные с кругами.
import math


# Функция area принимает радиус круга в качестве
6 # аргумента и возвращает площадь круга.
def area(radius):
    return math.pi * radius ** 2


# Функция circumference принимает радиус круга
# и возвращает длину окружности.
def circumference(radius):
    return 2 * math.pi * radius
