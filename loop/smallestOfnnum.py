n = int(input("How many numbers? "))
i = 1
smallest = int(input("Enter number 1: "))

while i < n:
    num = int(input("Enter next number: "))
    if num < smallest:
        smallest = num
    i += 1

print("Smallest =", smallest)