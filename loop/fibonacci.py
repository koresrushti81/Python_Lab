n = int(input("Enter number of terms: "))
a = 0
b = 1
i = 1

while i <= n:
    print(a, end=" ")
    a, b = b, a + b
    i += 1