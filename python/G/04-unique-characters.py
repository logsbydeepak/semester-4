text = input("Enter a string: ")
character_frequency = {}

for char in text:
    character_frequency[char] = character_frequency.get(char, 0) + 1

print("Number of unique characters:", len(character_frequency))

"""
Enter a string: Hello, World!
Number of unique characters: 10
"""
