string=input("Enter a string: ")
seen=""
 
for i in string:
     
        if i not in seen:
              seen+=i
print(seen)