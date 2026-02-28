a = int(input("Enter a number to calculate it's Factors: "))
print("Factors of",a,"are: ")
for i in range (1,a+1):
    if (a%i==0):
        print(i, end=" ")
