import random


END = 100

def get_sun_list(nums_list):
    total = 0
    for i in nums_list:
        total += i

    return total

def main():
    n_list = []
    for i in range(END):
        n_list.append(random.randint(1,100))

    print(n_list)
    total_sum = get_sun_list(n_list)
    print(total_sum)





if __name__ == '__main__':
    main()