def half(num):
    result = num / 2
    return result

def main():
    num = float(input('Введите число: '))
    result = half(num)
    print(result)


if __name__ == '__main__':
    main()