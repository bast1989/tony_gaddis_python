def main():
    total = 0
    cn = 0
    try:
        num_file = open('numbers.txt', 'r')
        for line in num_file:
            line = int(line.rstrip('\n'))
            total += line
            cn += 1
        num_file.close()
    except Exception as err:
        print(err)

    print(f'Сумма чисел в файле: {total}')
    print(f'Количество чисел в файле: {cn}')


if __name__ == '__main__':
    main()