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

#Replacement(Add to one row a multiple of its own and other row)
def replaceRow(matrix, row1, row2, coefficient):
    for i in range(len(matrix[0])):
        matrix[row1][i]=matrix[row2][i]+(coefficient*matrix[row1][i])
    return

#Replacement(Add to one row a multiple of another row)
def replaceThisRow(matrix, row1, row2, coefficient):
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

def zeroRows(matrix):
    numZeroRows= 0
    i=0
    while i<len(matrix):
        zeroEntries=0
        for j in range(0, len(matrix[0])):
            if matrix[i][j]==0:
                zeroEntries+=1
        if zeroEntries== len(matrix[0]):
            matrix.pop(i)
            numZeroRows+=1
            i-=1
        i+=1
    for k in range(0, numZeroRows):
        matrix.append([0] * len(matrix[0]))


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
    
def printMatrix(matrix):
    print("[", end=" ")
    for i in range(0, len(matrix)):
        if i==0:
            print("[", end=" ")
        else:    
            print("  [", end=" ")
        for j in range(0, len(matrix[0])):
            print(matrix[i][j], end=" ")
        if i==len(matrix)-1:
            print("]", end="")
        else:
            print("]")
    print(" ]")
    
def upperEntriesToZero(matrix, pivot_Column, pivot_Row):
    if pivot_Row==0 :
        return
    i = pivot_Row-1
    while i>=0:
        if matrix[i][pivot_Column]!=0:
            replaceThisRow(matrix, i, pivot_Row, (-1*matrix[i][pivot_Column])/matrix[pivot_Row][pivot_Column])

        i-=1
    

def backwardPhase(matrix):
    i = len(matrix[0]) -2 #leftmost column
    j = len(matrix) -1 #downmost row
    while j>=0:
        for i in range(0, len(matrix[0])):
            if matrix[j][i]!=0:
                #leading entry
                # print("its a leading entry row={}  column={}".format(j, i))
                upperEntriesToZero(matrix, i, j)
                break
        j-=1
    return

def leadingEntriesOne(matrix):
    i=0
    j=0
    while i<len(matrix):
        while j<len(matrix[0]):
            if matrix[i][j]!=0:
                scaleRow(matrix, i, 1/matrix[i][j])
                break
            j+=1
        i+=1


def printVariable(vlist, numbVariable):
    if vlist == None:
        print("X{} is free".format(numbVariable+1), end="\n")
        return
    else:
        noSign = False
        if vlist[len(vlist)-1]!=0:
            noSign = False
            print("X{}: {}".format(numbVariable+1, vlist[len(vlist)-1]), end=" ")
        else:
            noSign = True
            print("X{}:".format(numbVariable+1), end=" ")
        
        for i in range(0, len(vlist)-1):
            if vlist[i]==0 or i == numbVariable:
                continue
            elif vlist[i]>0:
                print("{}\033[91mX{}\033[0m".format(-1*vlist[i], i+1), end=" ")
            elif noSign:
                print("{}\033[91mX{}\033[0m".format(-1*vlist[i], i+1), end=" ")
                noSign = False
            else:
                print("+{}\033[91mX{}\033[0m".format(-1*vlist[i], i+1), end=" ")
        print()
        return





def printOutput(matrix):
    variables = [-1]*(len(matrix[0])-1)
    for i in range(0, len(matrix)):
        for j in range(0, len (matrix[0])):
            if matrix[i][j]!=0:
                #leading entry
                variables[j] = i
                break
    #where variables[i] is -1 the variable Xi is a free variable 
    #if a variables[i] is not -1 (the number of the row in which they are the leading entry/pivot) then the variable Xi is a base variable
    for i in range(0, len(matrix[0])-1):
        if(variables[i]!=-1):
            printVariable(matrix[variables[i]] ,i)
        else:
            printVariable(None, i)

def consistency(matrix):

    i = len(matrix) -1
    while i>=0:
        j = len(matrix[0]) -1
        if matrix[i][j] == 0:
            i-=1
            continue
        numVariableInRow = 0
        j-=1
        while j>=0:
            if matrix[i][j]!=0:
                numVariableInRow+=1
                break
            j-=1
        if numVariableInRow==0:
            return False
        i-=1
    return True

def roundoffErrorFixer(matrix):
    for i in range(0,len(matrix)):
        for j in range(0, len(matrix[0])):
            if -0.00000001<matrix[i][j]<0.00000001:
                matrix[i][j]=0

def main():
    row, column = getRowAndColumnInfo()
    if row == 0 or column==0:
        print("\033[91mXinexistent matrix\033[0m")
        return
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
    # print(matrixList)
    printMatrix(matrixList)
    # now the matrixList is the augmented matrix of the linear equation system

    row = 0
    column = 0 
    forwardPhase(matrixList, row, column)
    roundoffErrorFixer(matrixList)
    # printMatrix(matrixList)
    print("\n\n\n")
    # zero rows 
    zeroRows(matrixList)
    #the matrix is in echelon form
    if not(consistency(matrixList)):
        print("\033[91mthis system is inconsistent\033[0m")
        return
    #next step -> change it to reduced echelon form
    backwardPhase(matrixList)
    #convert leading entry ->1
    leadingEntriesOne(matrixList)
    printMatrix(matrixList)
    printOutput(matrixList)     



main()