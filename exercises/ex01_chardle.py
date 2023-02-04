"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730564297"

word: str = input("Enter a 5-character word: ")
if (len(word) != 5):
    print("Error: Word must contain 5 characters")
    exit()

character: str = input("Enter a single character: ")
if (len(character) != 1):
    print("Error: Character must be a single character.")
    exit()
print("Searching for " + character + " in " + word)

count: int = 0

if (character == word[0]):
    count = count + 1
    print(character + " found at index 0")
if (character == word[1]):
    count = count + 1
    print(character + " found at index 1")
if (character == word[2]):
    count = count + 1
    print(character + " found at index 2")
if (character == word[3]):
    count = count + 1
    print(character + " found at index 3")
if (character == word[4]):
    count = count + 1
    print(character + " found at index 4")

if (count == 0):
    print("No instances of " + character + " found in " + word)
if (count == 1):
    print("1 instance of " + character + " found in " + word)
if (count > 1):
    print(str(count) + " instances of " + character + " found in " + word)
