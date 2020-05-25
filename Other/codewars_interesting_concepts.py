def iq_test(numbers):
    e = [int(i) % 2 == 0 for i in numbers.split()]

    return e.index(True) + 1 if e.count(True) == 1 else e.index(False) + 1

def main():
    #print(iq_test("1 42 18 20 8 42 8"))
    a = list()
    print(a)


if __name__ == '__main__':
    main()