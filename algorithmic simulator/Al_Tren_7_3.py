import random


END = 100

def main():
    num_list = []
    for i in range(END):
        num_list.append(random.randint(1,100))

    print(num_list)
    print(id(num_list))

    c_list = num_list.copy()
    print(c_list)
    print(id(c_list))

    s_list = num_list[:]
    print(s_list)
    print(id(s_list))

    l_list = list(num_list)
    print(l_list)
    print(id(l_list))

    f_list = [i for i in num_list]
    print(f_list)
    print(id(f_list))





if __name__ == '__main__':
    main()