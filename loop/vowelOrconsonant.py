ch = input("Enter a character: ").lower()

if len(ch) == 1 and ch.isalpha():
    if ch in "aeiou":
        print("Vowel")
    else:
        print("Consonant")
else:
    print("Enter a single alphabet")