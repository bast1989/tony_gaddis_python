def main():
    num_file = open('number.txt', 'r')

    for line in num_file:
        line = line.rstrip('\n')
        print(line)

    num_file.close()


if __name__ == '__main__':
    main()