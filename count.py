s=input("Enter a string")
count_vowel=0
count_con=0
count_space=0
count_digit=0
count_special=0
d=[1,2,3,4,5,6,7,8,9,0]
s=['!' ,'@' ,'#','$', '%','^','&','*','~','`']
for i in s:
 if i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U' :
  count_vowel+=1

 elif i in d :
   count_digit
 elif i in s:
  count_space+=1
 elif i ==" " :
  count_space+=1
 else: 
  count_con+=1
print(count_vowel)
print(count_con)
print(count_space)
print(count_digit)
print(count_special)