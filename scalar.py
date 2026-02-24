A = [[1,2],[3,4]]
B = [[5,6],[7,8]]
C = A
for i in range(len(A)):
    for j in range(len(A[0])):
        C[i][j] =  A[i][j] + B[i][j]
print(C)
