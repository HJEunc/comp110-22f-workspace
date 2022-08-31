"""EX03 - One Shot Wordle"""

__author__ = "730566282"

secret_word: str = "python"
guess: str = input("What is your 6-letter guess? ")

while len(guess) != 6:
    guess: str = input("That was not 6 letters! Try again: ")

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

i: int = 0
emoji_result: str = ""

while i < len(secret_word):
    if guess[i] == secret_word[i]:
        emoji_result += GREEN_BOX
    else:
        emoji_result += WHITE_BOX
    i += 1

print(emoji_result)

if guess == secret_word:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")