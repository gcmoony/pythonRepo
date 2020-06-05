def iq_test(numbers = "1 42 18 20 8 42 8"):
    e = [int(i) % 2 == 0 for i in numbers.split()]

    return e.index(True) + 1 if e.count(True) == 1 else e.index(False) + 1


def list_finding(someList = [1, 14, 24, 18, 2], longList = "9 19 9 45 37 11 23 43 31 50 11 31 29 17 37 25 29 13 51 43 47 39 51 45 11 17 21 39 33 35 25 51 5 25"):
    longList = [int(i) for i in longList.split()]
    print(longList)
    a = [item % 2 == 0 for item in someList]
    print(a)
    print(a.count(True))
    print(a.index(True))
    return someList.index(True)

def compareLists(list1 = [], list2 = [1, 14, 5, 2]):
    '''
    Replacing the old way of using if else statements

    if len(list1) >= len(list2):
        return True
    else:
        return False
    '''

    print(f"\nList 1: {list1}\nList 2: {list2}")
    return True if len(list1) >= len(list2) else False
    

def list_creation(someList = [1, 14, 24, 18, 2]):
    """
    Easy way to break a string (numbers.split()) and loop through the now list of strings
    and assign them into a new list

    numbers = "12 1 23 11 17"
    e = [i for i in numbers.split()]
    """
    # f will be the same list as someList
    f = [j for j in someList]
    return f




def main():
    #print(iq_test())
    #print(compareLists())
    #print(list_creation())
    #print(list_finding())
    list_finding()

if __name__ == '__main__':
    main()