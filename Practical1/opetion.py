a = int(input("Enter a number: "))
b = int(input("Enter a number: "))

choose = input("Enter your choice (1 for addition, 2 for subtraction, 3 for multiplication, 4 for division): ")

if choose == '1':
    result = a + b
    print("The result of addition is:", result)
elif choose == '2':
    result = a - b
    print("The result of subtraction is:", result)
elif choose == '3':
    result = a * b
    print("The result of multiplication is:", result)
elif choose == '4':
    if b != 0:
        result = a / b
        print("The result of division is:", result)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid choice. Please select a valid operation.")                    


