import matplotlib.pyplot as plt


def costFunctionCalc(aDictOfPoints, thetaParam):
    """
    Takes a dictionary of points x:y and a thetaParameters
    and returns a single floating point value costVal
    """
    totalPoints = len(aDictOfPoints)
    sumOfSquareDiffs = 0

    # Get the sum of squared differences
    for x, y in aDictOfPoints.items():
        # Get height difference squared
        squareDiff = (x * thetaParam - y) ** 2 # ((x * theta1) - y)
        sumOfSquareDiffs += squareDiff

    costVal = sumOfSquareDiffs / (2 * totalPoints)
    return costVal


def generateCostValueList(dictOfPoints):
    """
    Creates cost values given a dictionary of points x:y and returns a list of cost values
    """
    listOfCostVals = []
    theta = -0.5
    while(theta <= 1):
        listOfCostVals.append(costFunctionCalc(dictOfPoints, theta))
        theta += 0.5
    return listOfCostVals


def dictToList(aDictionaryOfPoints, getKeys = False):
    """
    Uses a dictionary to generate a list of data points.
    getKeys == True will provide a list of data using the keys of the dictionary
    getKeys == False will provide a list of data using the values of the dictionary
    """
    values = []
    for x, y in aDictionaryOfPoints.items():
        if(getKeys):
            values.append(x)
        else:
            values.append(y)
    return values


def get_gradient_at_b(x, y, m, b):
  '''
  x == set of inputs
  y == set of real outputs
  m == gradient guess
  b == intercept guess
  '''
  b_gradient = -1
  if len(x) == len(y):
    diff = 0
    for index in enumerate(x):
      # Sum of all differences, yi - (mxi + b)
      diff += (y[index] - (m * x[index] + b))
    b_gradient = (-2/len(x)) * diff

  return b_gradient


def main():
    # Creating a set of points
    pointDict = {1:2,
                 2:6,
                 3:15}
    thetaVal = 0.5

    # List format
    x = dictToList(pointDict, getKeys=True)
    y = dictToList(pointDict)
    print(f"X Values: {x}\nY Values: {y}\n")

    plt.plot(x, y, "o")
    plt.show()

    # Using the cost function calculator
    costVal = costFunctionCalc(pointDict, thetaVal)
    

    print(f"Cost value of {thetaVal}: {costVal}")

    

if __name__=='__main__':
    main()