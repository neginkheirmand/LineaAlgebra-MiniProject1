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
    

def isInEchelonForm(matrix):
    #all nonzero rows are above any rows of zeros
    for i in range(0, len(matrix[0])):
        rowStarted = False
        for j in range(0, len(matrix)):
            if rowStarted:
                if matrix[i][j]!=0:
                    return False
            else: 
                if matrix[i][j]!=0:
                    rowStarted = True

    
    
pivotColumn = 0
pivotRow = 0

#Replacement(Add to one row a multiple of another row)
def replaceRow(matrix, row1, row2, coefficient):
    for i in range(len(matrix[0])):
        matrix[row1][i]=matrix[row2][i]+(coefficient*matrix[row1][i])
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

def findPivot(matrix, row, column):
    global pivotColumn, pivotRow
    # if pivotColumn>=len(matrix[0]):
    #     return
    for i in range(column, len(matrix[0])):
        for j in range(row, len(matrix)):
            if matrix[j][i]!=0 :
                pivotColumn = i
                pivotRow = j
                return

def convertToZeroEntry(matrix, pivot_Row, pivot_Column, thisRow, thisColumn):
    coefThsEntr = (-1*matrix[pivot_Row][pivotColumn])/matrix[thisRow][thisColumn]
    replaceRow(matrix, thisRow, pivot_Row, coefThsEntr)    

def forwardPhase(matrix, row, column):
    print(matrix)
    #this function takes in the matrix, selects the next pivot and make the bellow entries zero
    global pivotColumn, pivotRow
    findPivot(matrix, row, column)
    #now we have the new pivot column and pivot row settled 
    changeRow(matrix, pivotRow, row)
    row +=1
    column = pivotColumn 
    for i in range(row, len(matrix)):
        if matrix[i][column]!=0:
            #make it zero  
            convertToZeroEntry(matrix, row-1, column, i, column)
    if pivotColumn>=len(matrix[0])-1 or row>=len(matrix):
        return
    forwardPhase(matrix, row, pivotColumn+1)
    

    
    
    

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

    row = 0
    column = 0 
    forwardPhase(matrixList, row, column)
    
    #convert leading entry ->1
    j=0
    for i in range(0, len(matrixList[0])):
        if i==len(matrixList[0])-1:
            #end of row
            break
        if matrixList[j][i]!=0 and matrixList[j][i]!=1:
            scaleRow(matrixList, j, 1/matrixList[j][i])
            j+=1
    print(matrixList)



main()