"""
This is a program based on the Collatz Sequence. The 
Collatz Sequence takes any positive integer value
and eventually returns the value 1.
"""


def collatz(aNumber):
    if aNumber % 2 == 0:
        aNumber = aNumber // 2
        print(aNumber)
        return aNumber

    else:
        aNumber = aNumber * 3 + 1
        print(aNumber)
        return aNumber



def main():
    recalls = 0
    try:
        firstVal = int(input("Enter an integer value: "))
        while(firstVal != 1):
            firstVal = collatz(firstVal)
            recalls += 1
        print(f"The function 'collatz' ran a total of {recalls} time(s).\n")
    
    except ValueError:
        print("Please use integer values only.\n")
        main()

if __name__ == '__main__':
    main()