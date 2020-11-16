#scalar multiplication
def scalarMatrixMult(mat, scalar, lengthOfMat):
    lengthOfMat = lengthOfMat
    for index in range(lengthOfMat):
        for j in range(lengthOfMat):
            mat[index][j] = mat[index][j] * scalar

#driver code
if __name__ == "__main__":
    #first list
    A = [[1,0,0],[0,1,0],[0,0,1]]
    scalar = 3
    lengthOfMat = len(A)
    scalarMatrixMult(A, scalar, lengthOfMat)
    for index in range(lengthOfMat):
        for j in range(lengthOfMat):
            print(A[index][j], end = " ")
        print()

    #second list
    D = []
    scalar = 3
    lengthOfMat = len(D)
    scalarMatrixMult(D, scalar, lengthOfMat)
    for index in range(lengthOfMat):
        for j in range(lengthOfMat):
            print(A[index][j], end = " ")
        print()
print(D)
