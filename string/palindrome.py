string =input("Enter a string: ")
rev=string[::-1]
if(rev==string):
    print("The string is a palindrome.",string)

else:
    print("The string is not a palindrome.",string)