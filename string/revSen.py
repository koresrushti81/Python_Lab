# 29.	Sentence Reversal 
# ●	Reverse the order of words in a sentence without changing the words themselves. 
# ●	Example:
# ●	Input: Python is easy
# Output: easy is Python

string=input("enter a string:")
words = string.split()
for i in range(len(words)-1, -1, -1):
    print(words[i], end=" ")