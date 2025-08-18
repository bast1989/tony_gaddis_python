def counting_vowels(line):
    vowels = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
    count = 0
    for ch in line:
        if ch.lower() in vowels:
            count += 1
    return count

def counting_consonants(line):
    consonants = [
        'б', 'в', 'г', 'д', 'ж', 'з', 'й',
        'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т',
        'ф', 'х', 'ц', 'ч', 'ш', 'щ'
    ]
    count = 0
    for ch in line:
        if ch.lower() in consonants:
            count += 1
    return count

def intro_menu(line):
    print('Введите "г" что бы посчитать гласные или "с" что бы посчитать согласные')
    menu_item = input('Что будем считать: ')
    check_list = ['г', 'с']
    while menu_item not in check_list:
        print('\nВы ввели неверное значение\n')
        print('Введите "г" что бы посчитать гласные или "с" что бы посчитать согласные')
        menu_item = input('Что будем считать: ')
    if menu_item == 'г':
        print(f'Гласных с слове "{line}": {counting_vowels(line)}')
    elif menu_item == 'с':
        print(f'Гласных с слове "{line}": {counting_consonants(line)}')


def main():
    line = input('Введите слово или фразу: ')
    intro_menu(line)


if __name__ == '__main__':
    main()