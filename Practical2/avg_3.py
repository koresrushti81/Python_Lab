a = int(input("Enter a number a: "))
b = int(input("Enter a number b: "))
c = int(input("Enter a number c: "))

if a < b and a < c:
    print("The smallest number is:", a)
elif b < a and b < c:
    print("The smallest number is:", b)
else:
    print("The smallest number is:", c)        