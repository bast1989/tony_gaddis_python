def main():
    step_file = open('steps.txt', 'r')
    month = open('months.txt', 'r')

    for line in month:
        print(line)


if __name__ == '__main__':
    main()