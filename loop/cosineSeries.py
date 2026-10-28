import math

x = float(input("Enter x in radians: "))
n = int(input("Enter number of terms: "))
s = 0

for i in range(n):
    s += ((-1) ** i) * (x ** (2 * i)) / math.factorial(2 * i)

print("Cosine series sum =", s)