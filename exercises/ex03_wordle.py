"""EX03 - Structured Wordle."""
__author__ = "730566282"


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def contains_char(searched_str: str, char_str: str) -> bool:
    """Search for a given character in a given string."""
    assert len(char_str) == 1
    i: int = 0
    while i < len(searched_str):
        if char_str[0] == searched_str[i]:  # if character is in word
            return True
        else:  # if character is NOT in word
            i += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Given 2 equal length strings, return emojis corresponding to guess."""
    assert len(guess) == len(secret)
    j: int = 0
    emoji_result: str = ""
    while j < len(secret):
        checker: bool = contains_char(secret, guess[j])
        if checker:  # if character is in word, checks to see if it is green or yellow
            if secret[j] == guess[j]:
                emoji_result += GREEN_BOX
            else:
                emoji_result += YELLOW_BOX
        else:  # runs if letter does not appear in secret word
            emoji_result += WHITE_BOX
        j += 1
    return emoji_result


def input_guess(expected_length: int) -> str:
    """Given a length, prompt user for guess until one is given of correct length."""
    guess: str = input(f"Enter a {str(expected_length)} character word: ")
    while len(guess) != expected_length:
        guess = input(f"That wasn't {str(expected_length)} chars! Try again: ")
    return guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret: str = "codes"
    turn: int = 1
    won: bool = False
    while turn <= 6 and not won:  # while turns are left and user has not won
        print(f"=== Turn {turn}/6 ===")
        guess: str = input_guess(len(secret))
        print(emojified(guess, secret))
        if guess == secret:  # user won
            won = True
            print(f"You won in {turn}/6 turns!")
        else:
            turn += 1
    if turn > len(secret):  # if user runs out of turns
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":  # allows to run as module and import functions and reuse them
    main()