marks = float(input("Enter marks: "))

if marks >= 90 :
    print("Grade: A")
elif 80 <= marks <90 :
    print("Grade: B")
elif 70 <= marks < 80 :
    print("Grade: C")
elif 60 <= marks < 70 :
    print("Grade: D")
elif 50 <= marks < 60 :
    print("Grade: E")
elif 35 <= marks < 50 :
    print("Grade: P")
else :
    print("Grade: F")
