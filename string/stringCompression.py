# ●	Compress a string by counting consecutive repeated characters. 
# ●	Example:
# 	Input: aaabbccccd
# 	Output: a3b2c4d1

string = input("enter a string:")
s=""
count = 1
for i in range(len(string)-1):
    if string[i] == string[i+1]:
        count += 1
    else:
        s += string[i] + str(count)
        count = 1
s += string[-1] + str(count)
print(s)