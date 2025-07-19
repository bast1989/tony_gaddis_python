START = 1
STOP = 101

def main():
    number_file = open('number_list.txt', 'w')

    for i in range(START, STOP):
        number_file.write(f'{str(i)}\n')

    number_file.close()


if __name__ == '__main__':
    main()
