import random as rand
import copy


def generateList(listSize = 20):
    listOfValues = []
    while(len(listOfValues) != listSize):
        listOfValues.append(rand.randint(0, 30))
    return listOfValues


def bubbleSort(unsortedList):
    for sortingItemIndex in range(len(unsortedList)):
        for itemIndex in range(len(unsortedList)):
            if unsortedList[sortingItemIndex] > unsortedList[itemIndex]:
                temp = unsortedList[sortingItemIndex]
                unsortedList[sortingItemIndex] = unsortedList[itemIndex]
                unsortedList[itemIndex] = temp
    print("Bubble Sort:\n", unsortedList)
             


def main():
    # Generate a new list of values
    myList = generateList()
    print("Original list:\n", myList)
    # Run bubble sort
    bubbleSort(copy.copy(myList))
    # Run merge sort

    # Run quick sort


if __name__ == '__main__':
    main()