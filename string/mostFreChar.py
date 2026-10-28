string=input("enter a string:")
max_char = max(string, key=string.count)
print("Most frequent character:", max_char)