def main():
    name = 'Джим'
    dct = {'Джим': 123}

    print(dct)

    if name in dct:
        del dct[name]
        print(f'Имя: {name} удалено.')
    else:
        print(f'Имя: {name} нет в словаре.')

    print(dct)

    if name in dct:
        del dct[name]
        print(f'Имя: {name} удалено.')
    else:
        print(f'Имя: {name} нет в словаре.')


if __name__ == '__main__':
    main()