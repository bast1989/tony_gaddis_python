def main():
    str_list = ['Мигнуть', 'Моргнуть', 'Кивнуть']
    len_list = []

    for line in str_list:
        len_list.append(len(line))

    print(str_list)
    print(len_list)


if __name__ == '__main__':
    main()