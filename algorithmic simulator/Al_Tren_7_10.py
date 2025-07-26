import random


END = 100

def main():
    n_list = []
    for i in range(END):
        n_list.append(random.randint(1,200))

    nums_list = [i for i in n_list if i % 2 == 0]
    print(nums_list)




if __name__ == '__main__':
    main()