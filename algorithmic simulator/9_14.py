import pickle

def main():
    test_averages_file = open('../programming exercises/mydata.dat', 'rb')

    test_averages_row = test_averages_file.read()

    test_averages = pickle.loads(test_averages_row)

    test_averages_file.close()

    print(test_averages)

if __name__ == '__main__':
    main()
