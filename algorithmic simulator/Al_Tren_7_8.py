import random


END = 100

def main():
    n_list = []
    for i in range(END):
        n_list.append(random.randint(1,100))

    nums_list = [i ** 2 for i in n_list]

    print(n_list)
    print(nums_list)


if __name__ == '__main__':
    main()