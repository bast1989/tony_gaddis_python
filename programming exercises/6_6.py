def main():
    total = 0
    cn = 0
    try:
        num_file = open('number.txt', 'r')
        for i in num_file:
            i = int(i.rstrip('\n'))
            total += i
            cn += 1
        print(f'Среднее равно: {total / cn:.2f}')
        num_file.close()
    except Exception as err:
        print(f'Ошибка: {err}')

if __name__ == '__main__':
    main()