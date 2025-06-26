# Эта программа демонстрирует передачу в функцию двух
# строковых аргументов.

def main():
    first_name = input('Введите имя: ')
    last_name = input('Введите фамилию: ')
    print('Ваши имя и фамилия в обратном порядке: ')
    reverse_name(first_name, last_name)


def reverse_name(first, last):
    print(last, first)

# Вызвать главную цию.
if __name__ == '__main__':
    main()