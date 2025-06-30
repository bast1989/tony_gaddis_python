COEFFICIENT = 0.6214

def converter(kilometers):
    miles = kilometers * COEFFICIENT
    return miles


def get_kilometers():
    print('Введите расстояние в километрах', end='')
    kilometers = float(input(': '))
    return kilometers


def main():
    kilometers = get_kilometers()
    miles = converter(kilometers)
    print(f'Конвертировали {kilometers} километров в {miles:.2f} миль.')


if __name__ == '__main__':
    main()