import pickle

def main():
    test_file = open('../programming exercises/mydata.dat', 'wb')

    test_averages = {
        'Alex': 98,
        'Mira': 87,
        'Lola': 92,
        'Ted': 74,
        'Sally': 89,
        'Zeb': 84
    }

    pickle.dump(test_averages, test_file)

    test_file.close()

if __name__ == '__main__':
    main()