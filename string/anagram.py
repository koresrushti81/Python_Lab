# Check whether two strings are anagrams. 
string1 = input("Enter a string: ")
string2 = input("Enter another string: ")
if (len(string1) != len(string2)):
    print("The strings are not anagrams.")
else:
    sorted_string1 = sorted(string1)
    sorted_string2 = sorted(string2)
    if (sorted_string1 == sorted_string2):
        print("The strings are anagrams.")
    else:
        print("The strings are not anagrams.")