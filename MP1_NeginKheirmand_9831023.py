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
    
    



main()