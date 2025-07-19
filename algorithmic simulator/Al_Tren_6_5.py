def main():
    total = 0
    number_file = open('number_list.txt', 'r')

    for line in number_file:
        line = int(line.rstrip('\n'))
        total += line

    number_file.close()

    print(total)


if __name__ == '__main__':
    main()