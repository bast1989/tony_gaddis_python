def main():
    nums = [1]
    value = int(input('Введите число: '))

    for i in range(2, value + 1):
        true_chek = []
        for j in range(1, value + 1):
            if i % j == 0:
                true_chek.append(True)
        if len(true_chek) == 2:
            nums.append(i)

    print('Список простых чисел:')
    for i in nums:
        print(i)


if __name__ == '__main__':
    main()