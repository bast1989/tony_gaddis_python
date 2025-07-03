COEFFICIENT = 12


def feet_to_inches(feet):
    return feet * COEFFICIENT

def main():
    feet = int(input('Введите количество футов: '))
    print(f'Футов {feet} ---> Дюймов {feet_to_inches(feet)}')


if __name__ == '__main__':
    main()
