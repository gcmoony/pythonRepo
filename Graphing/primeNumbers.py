import matplotlib.pyplot as plt
import random as rand

def plotList(coordList):
    pass

def createList(inclusiveA, exclusiveB, totalValues = 5, workingList = None):
    if workingList != None:
        if len(workingList) < totalValues:
            workingList.append(rand.randint(inclusiveA, exclusiveB))    
            createList(inclusiveA, exclusiveB, totalValues, workingList)
    else:
        workingList = []
        workingList.append(rand.randint(inclusiveA, exclusiveB))
        createList(inclusiveA, exclusiveB, totalValues, workingList)
    return workingList

def main():
    myList = createList(4, 20, 15)
    print(myList)
    #plotList()

if __name__ == "__main__":
    main()