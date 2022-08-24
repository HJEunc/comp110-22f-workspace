"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730566282"

#Part 1. Prompting for Inputs – 20 Points
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

#Part 2. Checking Indices for Matches – 20 Points
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

#Part 3. Counting Matching Indices – 30 Points
#counter declared on line 16
if counter>0:
    print(str(counter) + " instances of " + letter + " found in " + word)
else:
    print("No instances of " + letter + " found in " + word)

#Part 4. Exiting Early for Invalid Inputs - 10 points
#on lines 7-9 and 11-13

#Part 5. Style and Documentation Requirements – 10 Points (Manually Graded)

#Part 6. Type Safety and Linting - 9 Points