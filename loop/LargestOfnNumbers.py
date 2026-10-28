n = int(input("How many numbers? "))
i = 1
largest = int(input("Enter number 1: "))

while i < n:
    num = int(input("Enter next number: "))
    if num > largest:
        largest = num
    i += 1

print("Largest =", largest)