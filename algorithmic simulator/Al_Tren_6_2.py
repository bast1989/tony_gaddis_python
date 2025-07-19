def main():
    file_name = open('my_name.txt', 'r')

    name = file_name.read()

    print(name)


if __name__ == '__main__':
    main()