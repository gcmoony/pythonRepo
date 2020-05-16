import matplotlib.pyplot as plt
import numpy as np

def generateLinearValues(xValues = [1, 2, 3, 4], yIntercept = 0, slopeVal = 1):
    yOutputs = []
    for value in xValues:
        yOutputs.append(value * slopeVal + yIntercept)
    return yOutputs


def example01():
    # Creating Two subplots
    fig, ax = plt.subplots(2)

    # Adding points into first subplot
    ax[0].plot([1,2,5], [2,3,5])

    # Adding points into the second subplot
    ax[1].plot([1,4], [1, 3])

    # Display two plots
    plt.show()

def example02():
    # Generate some plotting values
    xVals = [0, 2, 3, 4]
    yVals = generateLinearValues(xValues= xVals, yIntercept= 0, slopeVal=2)

    # Generate a plot with the new values
    fig, ax = plt.subplots()
    ax.plot(xVals, yVals, label='Generated Plot', color = 'green', marker = 'X')
    

    # Plot formatting
    ax.legend()
    ax.set_ylabel('Output values')
    ax.set_xlabel('Input values')


    # Displaying the graphs
    plt.show()

def example03():
    # Creating two graphs on 1 figure
    aFigure, ax = plt.subplots()
    
    # Creating two tables
    table01 = [[-1, 0, 1], [5, -5, 5]]
    table02 = [[1, 3, 5, 7], generateLinearValues(xValues= [1,3,5,7])]

    # plotting both tables
    ax.plot(table01[0], table01[1], label = 'Table 01')
    ax.plot(table02[0], table02[1], label = 'Table 02')
    plt.legend()
    plt.show()


def main():
    #example01()
    example02()
    example03()

if __name__ == '__main__':
    main()