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
    

#Replacement(Add to one row a multiple of another row)
def replaceRow(matrix, row1, row2, coefficient):
    # for i in range(len(matrix[0])):
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
    print(matrixList)
    scaleRow(matrixList, 0, 1)
    print(matrixList)
    scaleRow(matrixList, 0, 2)
    print(matrixList)
    scaleRow(matrixList, 0, 1/2)
    print(matrixList)

    # now the matrixList is the augmented matrix of the linear equation system
    
main()