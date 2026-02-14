def convert_days():
   
    days = int(input("Enter number of days: "))
    
    
    years = days // 365
    remaining_days = days % 365
    
    months = remaining_days // 30
    remaining_days = remaining_days % 30
    
    weeks = remaining_days // 7
    remaining_days = remaining_days % 7

    print("Years:", years)
    print("Months:", months)
    print("Weeks:", weeks)
    print("Remaining Days:", remaining_days)


convert_days()
