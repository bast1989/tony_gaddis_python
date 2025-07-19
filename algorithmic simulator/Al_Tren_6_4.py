def main():
    number_file = open('number_list.txt', 'r')

    for line in number_file:
        line = line.rstrip('\n')
        print(line)

    number_file.close()


if __name__ == '__main__':
    main()