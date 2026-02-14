def calculate_marks():
  
    m1 = float(input("Enter marks for Subject 1: "))
    m2 = float(input("Enter marks for Subject 2: "))
    m3 = float(input("Enter marks for Subject 3: "))
    m4 = float(input("Enter marks for Subject 4: "))
    m5 = float(input("Enter marks for Subject 5: "))
    
    total = m1 + m2 + m3 + m4 + m5
    
    average = total / 5
    
    percentage = (total / 500) * 100
    
    print("Total Marks:", total)
    print("Average Marks:", average)
    print("Percentage:", percentage, "%")

calculate_marks()
