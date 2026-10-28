string=input("Enter a string: ")
uppercount=0
lowercount=0
for i in string:
    if (i==i.upper() and i.isalpha()):
        uppercount+=1
    elif (i==i.lower() and i.isalpha()):
        lowercount+=1
    else:
        print("Invalid input. Please enter a valid string.")
print("Uppercase letters:", uppercount)
print("Lowercase letters:", lowercount)