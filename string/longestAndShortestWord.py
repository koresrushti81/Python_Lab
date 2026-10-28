string=input("Enter a sentence: ")
words=string.split()
for i in words:
   max= words[0]
   if len(i)>len(max):
         max=i
   min=words[0]
   if len(i)<len(min):
        min=i
   
print("Longest word is:", max)
print("Shortest word is:", min)