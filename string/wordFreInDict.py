# 28.	Word Frequency Dictionary 
# ●	Count the frequency of every word in a paragraph. 


paragraph = input("enter a paragraph:")
words = paragraph.split()
freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1

print("Word frequencies:")
for word, count in freq.items():
    print(f"{word}: {count}")