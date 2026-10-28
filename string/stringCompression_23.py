# 23.	String Compression 
# ●	Compress repeated characters and return the original string if compression does not reduce the length. 
 
string = input("enter a string:")
compressed = ""
count = 1
for i in range(len(string)-1):
    if string[i] == string[i+1]:
        count += 1
    else:
        compressed += string[i] + str(count)
        count = 1
compressed += string[-1] + str(count)

if len(compressed) < len(string):
    print("Compressed string:", compressed)
else:
    print("Original string:", string)