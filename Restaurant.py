def getdetails():
    global age, group, cost
    age = int(input("Enter Age: "))
    group = int(input("Enter Number Of People: "))
    cost = float(input("Enter Cost Of Meal: "))
    
    if age >= 65 or group >= 5:
        cost = cost * 0.5
    else:
        print("No Discount ")
    
def printing():
    print("Age: ", age)
    print("Group: ", group)
    print("Total Cost: ", cost)
    
getdetails()
printing()