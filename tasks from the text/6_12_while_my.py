def main():
    length_file = open('length_of_the_roller.txt', 'r')
    line = length_file.readline()
    total = 0
    count = 1
    while line != '':
        line = int(line)
        print(f'Длина отрезка {count}: {line}')
        total += line
        count += 1
        line = length_file.readline()
    length_file.close()

    print(f'Общая длина ролика составила: {total}')


if __name__ == '__main__':
    main()
