word1 = input("Enter first string: ").lower().replace(" ", "")
word2 = input("Enter second string: ").lower().replace(" ", "")

count1 = {}
count2 = {}

for char in word1:
    count1[char] = count1.get(char, 0) + 1

for char in word2:
    count2[char] = count2.get(char, 0) + 1

if count1 == count2:
    print("Strings are anagrams")
else:
    print("Strings are not anagrams")

"""
Enter first string: evil
Enter second string: live
Strings are anagrams
"""
