String=input("Enter a string: ")
seen=""
printed=""
for i in String:
    if i in seen:
        if i not in printed:
            print("Duplicate character:",i)
            printed+=i
    seen+=i