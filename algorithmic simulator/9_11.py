def main():
    numbers = [1, 2, 3, 4, 5]

    num_is_num = {num:num * 10 for num in numbers}

    print(num_is_num)



if __name__ == '__main__':
    main()