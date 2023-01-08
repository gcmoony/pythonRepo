'''
The objective here is to rotate a matrix of size M * M 90 degrees clockwise.
'''

def rotateMatrix(originalMatrix):
    newMatrix = templateMatrix(len(originalMatrix))
    size = len(originalMatrix)

    # Start from the last row, first column in originalMatrix
    rowIter, colIter = size - 1, 0
    
    # Start with the first row in newMatrix
    newMatrixRowIter = 0

    # From the bottom row to the top row in originalMatrix
    while rowIter >= 0:
        # From left to right in originalMatrix
        while colIter < size:
            # Add the item from originalMatrix to the current row of newMatrix
            newMatrix[newMatrixRowIter].append(originalMatrix[rowIter][colIter])
            # Move to next column in originalMatrix[rowIter]
            colIter += 1
            # Move to the next row of newMatrix
            newMatrixRowIter += 1
            

        # Start from the left at the new row in the originalMatrix
        colIter = 0
        # Move up 1 row in the originalMatrix
        rowIter -= 1

        # Start adding to the top row in the newMatrix
        newMatrixRowIter = 0
    return newMatrix
    
def displayMatrix(matrix):
    '''
    Prints each row of a matrix for output readability
    '''
    for row in matrix:
        print(row)
    print()


def templateMatrix(matrixSize):
    '''
    Create an empty matrix of size M
    '''
    newMatrix = []
    counter = 0
    while counter < matrixSize:
        newMatrix.append([])
        counter += 1
    return newMatrix



def main():
    # Create a matrix
    matrix = [
    [1, 2, 4, 1],
    [4, 5, 6, 12],
    [42, 2, 61, 2],
    [91, 83, 24, 7]
    ]

    # Rotate the matrix 90 degrees CW
    newMatrix = rotateMatrix(matrix)

    # Rotate the matrix 180 degrees CW
    newerMatrix = rotateMatrix(newMatrix)

    # Display the matricies
    displayMatrix(matrix)
    displayMatrix(newMatrix)
    displayMatrix(newerMatrix)

if __name__ == '__main__':
    main()
