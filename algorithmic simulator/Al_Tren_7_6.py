NAME = 'Руби'

def main():
    names = []
    names.append('Эйнштейн')
    names.append('Ньютон')
    names.append('Коперник')
    names.append('Кеплер')
    # names.append('Руби')
    print(names)

    if NAME in names:
        print(f'Привет, {NAME}!')


if __name__ == '__main__':
    main()