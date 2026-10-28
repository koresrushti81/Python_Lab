n = int(input("Enter a number: "))
temp = abs(n)
rev = 0

while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp //= 10

if n < 0:
    rev = -rev

print("Reverse =", rev)