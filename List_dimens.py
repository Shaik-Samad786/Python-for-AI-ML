a = [[1,2],[2,3]]
print(type(a))
print(a)
b =[1,2,3,4,5,6,7,8,9]
print(type(b))
print(b)
print(a[0])
print(a[0][0])
print(a[0][1])
print(type(a[0][0]))



# output

<class 'list'>
[[1, 2], [2, 3]]
<class 'list'>
[1, 2, 3, 4, 5, 6, 7, 8, 9]
[1, 2]
1
2
<class 'int'>


a = [1,2,3,4,5]
ar = [[1,2],[2,3]]
print(ar)
print(type(ar))
print(type(ar[0]))
print(type(ar[0][0]))
print(type(ar[0][1]))


# output

[[1, 2], [2, 3]]
<class 'list'>
<class 'list'>
<class 'int'>
<class 'int'>


A = [[2,4],[1,0]]
for i in range(len(A)):
    for j in range(len(A[i])):
        A[i][j] = A[i][j]*3
        
for a in A:
    print(a)


# output

[6, 12]
[3, 0]
