# 30.	String Rotation 
# ●	Check whether one string is a rotation of another. 
# ●	Example:
# ●	ABCD
# ●	CDAB
# Output: Yes
str=input("enter a string:")
rot=input("enter a string to check rotation:")

if len(str) == len(rot) and rot in str + str:
    print("Yes")
else:
    print("No")
