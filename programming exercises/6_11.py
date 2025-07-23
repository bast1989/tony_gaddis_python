PLUG_NAME = '%name%'
PLUG_DESCR = '%description%'


def main():
    name = input('Введите имя: ')
    descr = input('Введите описание: ')

    open_file = open('index.html', 'r', encoding='cp1251')
    pers_file = open('personal_page.html', 'w')

    for line in open_file:
        line = line.strip()
        if line == PLUG_NAME:
            pers_file.write(f'{name}\n')
        elif line == PLUG_DESCR:
            pers_file.write(f'{descr}\n')
        else:
            pers_file.write(f'{line}\n')

    open_file.close()


if __name__ == '__main__':
    main()
