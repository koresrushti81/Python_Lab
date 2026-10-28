import math

n = int(input("Enter a number: "))
root = math.isqrt(n) if n >= 0 else 0
print("Square root =", math.sqrt(n) if n >= 0 else "Not defined")

if root < 2:
    print("Square root is not prime")
else:
    prime = True
    for i in range(2, math.isqrt(root) + 1):
        if root % i == 0:
            prime = False
            break

    if prime:
        print("Square root is prime")
    else:
        print("Square root is not prime")