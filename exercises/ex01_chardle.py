"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730566282"

word: str = input("Enter a 5-character word: ")
if len(word) != 5:
    print("Error: Word must contain 5 characters")
    exit()
letter: str = input("Enter a single character: ")
if len(letter) != 1:
    print("Error: Character must be a single character.")
    exit()
print("Searching for " + letter + " in " + word)

counter: int = 0

if letter == word[0]:
    print(letter + " found at index 0")
    counter = counter + 1
if letter == word[1]:
    print(letter + " found at index 1")
    counter = counter + 1
if letter == word[2]:
    print(letter + " found at index 2")
    counter = counter + 1
if letter == word[3]:
    print(letter + " found at index 3")
    counter = counter + 1
if letter == word[4]:
    print(letter + " found at index 4")
    counter = counter + 1

if counter > 1:
    print(str(counter) + " instances of " + letter + " found in " + word)
elif counter == 1:
    print(str(counter) + " instance of " + letter + " found in " + word)
else:
    print("No instances of " + letter + " found in " + word)