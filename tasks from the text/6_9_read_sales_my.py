# Эта программа читает все значения из
# файла sales.txt.
def main():
    sales = []
    sales_fail = open('sales.txt', 'r')
    line = sales_fail.readline()

    while line:
        print(f'{float(line):,.2f}')
        sales.append(float(line))
        line = sales_fail.readline()


    sales_fail.close()

    print(sales)

if __name__ == '__main__':
    main()