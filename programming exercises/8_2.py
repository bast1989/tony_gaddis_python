def main():
    nun_str = input('Введите строке: ')
    total = 0

    for ch in nun_str:
        total += int(ch)

    print(total)


if __name__ == '__main__':
    main()