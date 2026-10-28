# 25.	Second Most Frequent Character 
# ●	Find the second most frequently occurring character. 


string = input("enter a string:")
freq = {}
for char in string:
    freq[char] = freq.get(char, 0) + 1

if len(freq) < 2:
    print("Not enough unique characters.")
else:
    max_char = max(freq, key=freq.get)
    del freq[max_char]
    sec_max_char = max(freq, key=freq.get)
    print("Second most frequent character:", sec_max_char)