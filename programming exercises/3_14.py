LOW = 18.5
HIGH = 25

weight = float(input('Введите ваш вес в килограммах: '))
height = float(input('Введите ваш рост в сантиметрах: '))

height = height / 100

imt = weight / (height ** 2)

if imt < LOW:
    print('Низкий вес')
elif imt > HIGH:
    print('Высокий вес')
else:
    print('Вес в норме')