# scalar_addition
A = [[1,2],[3,4]]
B = [[5,6],[7,8]]
C = A
for i in range(len(A)):
    for j in range(len(A[0])):
        C[i][j] =  A[i][j] + B[i][j]
print(C)

# scalar_substraction
A = [[1,2],[3,4]]
B = [[5,6],[7,8]]
D = A
for i in range(len(A)):
    for j in range(len(A[0])):
        D[i][j] =  A[i][j] - B[i][j]
print(D)

# scalar_multi
A = [[1,2],[3,4]]
B = [[5,6],[7,8]]
E = A
for i in range(len(A)):
    for j in range(len(A[0])):
        E[i][j] =  A[i][j] * B[i][j]
print(E)
