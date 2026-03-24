def swap(a,i,j):
    temp=a[i]
    a[i]=a[j]
    a[j]=temp
a=[1,2,3,4]
print(a)
swap(a,0,3)
print(a)





output
[1, 2, 3, 4]
[4, 2, 3, 1]
