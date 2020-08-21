import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random as rand

def plotList(coordList):
    plt.plot(coordList, animated = True)
    ani = animation.FuncAnimation(plt, )
    plt.show()

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
    myList = createList(inclusiveA= 4, exclusiveB = 20, totalValues= 6)
    print(myList)
    plotList(myList)

if __name__ == "__main__":
    main()
