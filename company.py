isMarried=input("Are you married? (yes/no): ")
if (isMarried=="yes" or isMarried=="YES" or isMarried=="Yes" or isMarried=="y" or isMarried=="Y"):
    print("Driver is insured")

else:
    gender=input("Enter your gender (male/female): ")
    age=int(input("Enter your age: "))
    if(isMarried=="No" or isMarried=="no" or isMarried=="n" or isMarried=="N") and (gender=='Male' or gender=='m'or gender=='M' or gender=="MALE")and age>30: 
       print("Driver is insured")
    elif(isMarried=="No" or isMarried=="no" or isMarried=="n" or isMarried=="N") and (gender=='Female' or gender=='F'or gender=='f' or gender=="female")and age>25: 
       print("Driver is insured")
    else:
       print("Driver is not insured")
     