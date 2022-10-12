"""EX06 - Choose your own adventure."""
__author__ = "730566282"


import random  # Imported random to pick a random integar later on


points: int = 0
player: str = ""
SPARKLE: str = "\U00002728"  # Spakles to put around the start of functions
ARROW: str = "\U000025B6"  # Arrow used to list things out


def greet() -> None:
    """Greeting!"""
    global player
    global points
    print(f"{SPARKLE}Welcome to Python Minecraft!{SPARKLE}")
    player = input("What is your name? ")


def mine() -> None:
    """User selected to go mining!"""
    global points
    print(f"{SPARKLE}Time to Mine!{SPARKLE}")
    print("Depending on the ore you find, you will earn more points!")
    print("Select a location from the list below:")
    print(f" {ARROW} cave")
    print(f" {ARROW} ravine")
    location: str = input("Select location: ")
    while not ((location == "cave") or (location == "ravine")):
        print("That is not an option! Try again!")
        location: str = input("Which do you choose?? ")
    if location == "cave":
        print("The cave is dark and scary")
        print("Behind some rocks you found iron ore!")
        print("You earn 1 point!")
        points += 1
    if location == "ravine":
        print("In the deep ravine you see something shiny")
        print("You wander through the ravine, doging the lava")
        print("IT'S DIAMONDS!")
        print("You earn 3 points!")
        points += 3
    cont: str = input("Type 'continue' to pick a new task: ")
    while cont != "continue":
        cont: str = input("Did you forget how to spell? Try again: ")


def monster() -> None:
    """User selected to fight monsters!"""
    global points
    attack: str = ""
    print(f"{SPARKLE}Time to Fight Monsters!{SPARKLE}")
    print("A random monster will spawn, kill it and earn point!")
    ready: str = input("Type 'ready' to begin: ")
    while ready != "ready":
        ready: str = input("Try again! Type 'ready' to begin: ")
    randomizer: int = random.randint(1, 3)
    if randomizer == 1:
        attack = input("A zombie spawned! Quick, type 'punch' to attack! ")
        while attack != "punch":
            attack = input("You missed! Quick, type 'punch' now! ")
        print("You killed it, you earn 1 point!")
        points += 1
    if randomizer == 2:
        attack = input("A skeleton spawned! Quick, type 'punch' to attack! ")
        while attack != "punch":
            attack = input("You missed! Quick, type 'punch' now! ")
        print("You killed it, you earn 1 point!")
        points += 1
    if randomizer == 3:
        attack = input("A creeper spawned! Quick, type 'punch' to attack! ")
        while attack != "punch":
            attack = input("You missed! Quick, type 'punch' now! ")
        print("You killed it, you earn 2 points!")
        points += 2
        cont: str = input("Type 'continue' to pick a new task: ")
        while cont != "continue":
            cont: str = input("Did you forget how to spell? Try again: ")


def main() -> None:
    """Main code in adventure."""
    global player
    global points
    status: bool = True  # Checks if user wants to quit
    greet()
    print(f"It's good to have you here {player}!")
    while status:
        print(f"Current points: {points}")
        print("Pick a task and earn points along the way:")
        print(f" {ARROW} go mining")
        print(f" {ARROW} fight monsters")
        print(f" {ARROW} quit game")
        selection: str = input("Which do you choose?? ")
        while not ((selection == "go mining") or (selection == "fight monsters") or (selection == "quit game")):
            print("That is not an option! Try again!")
            selection: str = input("Which do you choose?? ")
        if selection == "go mining":
            mine()
        elif selection == "fight monsters":
            monster()
        elif selection == "quit game":
            status = False
            print(f"{SPARKLE}Thank you for playing {player}! See you next time!{SPARKLE}")
            print(f"Total points: {points}")


if __name__ == "__main__":
    main()