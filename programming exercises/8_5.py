MUMS = (('A', 'B', 'C'),
        ('D', 'E', 'F'),
        ('G', 'H', 'I'),
        ('J', 'K', 'L'),
        ('M', 'N', 'O'),
        ('P', 'Q', 'R', 'S'),
        ('T', 'U', 'V'),
        ('W', 'X', 'Y', 'Z'))

def main():
    number = input('Введите номер: ')

    for ch in number:
        if ch.isalpha():
            for num in MUMS:
                if ch in num:
                    print(MUMS.index(num) + 2, end='')
        else:
            print(ch, end='')


if __name__ == '__main__':
    main()

