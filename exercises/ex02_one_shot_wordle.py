"""EX02 - One Shot Wordle."""

__author__ = "730566282"

secret_word: str = "python"
guess: str = input(f"What is your {len(secret_word)}-letter guess? ")

while len(guess) != len(secret_word):
    guess = input(f"That was not {len(secret_word)} letters! Try again: ")

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

i: int = 0
emoji_result: str = ""

while i < len(secret_word):  # tests if indexes match
    if guess[i] == secret_word[i]:
        emoji_result += GREEN_BOX
    else:  # runs if indexes do not math
        j: int = 0
        checker: bool = False
        while not checker and j < len(secret_word):  # tests if letters appear at other indexes
            if guess[i] == secret_word[j]:
                checker = True
            else:
                j += 1
        if checker:  # runs if letter appears at other index
            emoji_result += YELLOW_BOX
        else:  # runs if letter does not appear in secret word
            emoji_result += WHITE_BOX
    i += 1

print(emoji_result)

if guess == secret_word:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")