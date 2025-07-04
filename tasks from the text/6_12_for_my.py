def main():
    length_file = open('length_of_the_roller.txt', 'r')
    total = 0
    count = 1

    for line in length_file:
        line = int(line)
        print(f'Длина отрезка {count}: {line}')
        total += line
        count += 1

    length_file.close()
    print(f'Общая длина ролика составила: {total}')

if __name__ == '__main__':
    main()