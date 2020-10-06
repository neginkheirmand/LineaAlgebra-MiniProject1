def getRowAndColumnInfo():
    print("Coefficient matrix\nEnter number of rows and columns respectively:")
    listOfInput =input().split()
    boolean = True
    if len(listOfInput) != 2:
        boolean = False
    else:
        try:
            listOfInput[0] = int(listOfInput[0])
            listOfInput[1] = int(listOfInput[1])
        except ValueError:
            boolean = False

    while not(boolean) :
        #user must enter only two numbers
        print("Enter number of rows and columns respectively:")
        boolean = False
        listOfInput =input().split()
        if len(listOfInput) != 2:
            boolean = False
            continue
        else:
            try:
                listOfInput[0] = int(listOfInput[0])
                listOfInput[1] = int(listOfInput[1])
                boolean = True
            except ValueError:
                boolean = False
    
    return listOfInput[0], listOfInput[1]
    

    
pivotColumn = 0
pivotRow = 0

#Replacement(Add to one row a multiple of another row)
def replaceRow(matrix, row1, row2, coefficient):
    for i in range(len(matrix[0])):
        matrix[row1][i]=matrix[row1][i]+(coefficient*matrix[row2][i])
    return


#Scaling(Multiply all entries in a row by a nonzero constant)
def  scaleRow(matrix, rowNum, constant):
    if constant!=0:
        for i in range(len(matrix[rowNum])):
            matrix[rowNum][i] = constant*matrix[rowNum][i]
    return

#Interchange (change position two rows)
def changeRow(matrix, row1, row2):
    rowContainer = matrix[row1]
    matrix[row1] = matrix[row2]
    matrix[row2] = rowContainer
    return

def findPivot(matrix):
    global pivotColumn, pivotRow
    if pivotColumn>=len(matrix[0]):
        return
    for i in range(pivotColumn, len(matrix[0])):
        for j in range(pivotRow, len(matrix)):
            if matrix[j][i]!=0 :
                pivotColumn = i
                pivotRow = j
                return

def forwardPhase(matrix):
    #this function takes in the matrix, selects the next pivot and make the bellow entries zero
    global pivotColumn, pivotRow
    pivotColumnNow = pivotColumn
    pivotRowNow = pivotRow
    findPivot(matrix)
    #now we have the new pivot column and pivot row settled 
    if pivotColumn>=len(matrix[0])-1:
        return
    changeRow(matrix, pivotRowNow, pivotRow)
    
    
    

def main():
    row, column = getRowAndColumnInfo()
    matrixList = []
    for i in range(row):
        print("Enter row {}".format(i))
        newRow = input().split()
        for j in range(column):
            newRow[j]= int(newRow[j])
        matrixList.append(newRow)
    print(matrixList)

    #now we have the coefficient matrix

    print("Enter constant values:")
    constantValues = input().split()
    if len(constantValues)== row:
        for i in range(row):
            try:
                constantValues[i] = int(constantValues[i])
            except ValueError:
                constantValues = []
    while len(constantValues)!= row:
        print("Please enter correct number of constants:")
        constantValues = input().split()
        for i in range(row):
            try:
                constantValues[i] = int(constantValues[i])
            except ValueError:
                constantValues = []
                break

    #now we have the constant values
    # next step is to create the augmented matrix

    for i in range(row):
        matrixList[i].append(constantValues[i])
    print("Given augmented matrix:")
    print(matrixList)
    # now the matrixList is the augmented matrix of the linear equation system

    forwardPhase(matrixList)
    print(matrixList)

    print("pivot column={} pivot row ={}".format(pivotColumn, pivotRow))


    

main()