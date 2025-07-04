def main():
    flag = 'д'
    length_file = open('length_of_the_roller.txt', 'w')
    while flag == 'д':
        length_roll = input('Введите длину файла: ')
        length_file.write(f'{length_roll}\n')
        flag = input('Хотите продолжить?: ')

    length_file.close()

if __name__ == '__main__':
    main()
