def get_str(str):
    return str.split('>')


def main():
    mystring = 'пирожки>молоко>стряпня>яблочный пирог>мороженое'

    print(get_str(mystring))

if __name__ == '__main__':
    main()