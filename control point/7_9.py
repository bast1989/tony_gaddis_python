def main():
    list_1 = [1, 12, 2, 20, 3, 15, 4]
    list_2 = []

    for i in list_1:
        if i < 10:
            list_2.append(i)

    print(list_1)
    print(list_2)


if __name__ == '__main__':
    main()