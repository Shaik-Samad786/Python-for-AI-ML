def check_triangle ():
    a = float(input("Enter one angle of Triangle: "))
    b = float(input("Enter another angle of Triangle: "))
    
    c = 180 - (a+b)
    print("The Thrid angle of Triangle = ", c)
    if (a==90 or b==90 or c==90) :
        print("The triangle formed is Right-Angled Triangle")
    elif (a==b or b==c or c==a):
        print("The triangle formed is Isosceles Triangle")
    else:
        print("Neither")

check_triangle()
