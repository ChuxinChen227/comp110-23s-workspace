"""EX06 - Choose Your Own Adventure."""

__author__ = "730564297"

from random import randint

points: int = 0
player: str = ""
chance: int = 0
EMOJI_TREE = "\U0001F333"


def main() -> None:
    """The main function of the game."""
    greet()
    play_game()


def greet() -> None:
    """Greets the player and gets their name."""
    global player
    player = input("What is your name? ")
    print(f"Hello, {player}! Have fun taking care of your virtual tree! {EMOJI_TREE}")


def play_game() -> None:
    """The game loop where the player can choose what to do next."""
    while chance < 5:
        print(f"{player}, you have a total points of {points} now.")
        choice = input("What do you want to do next? (water/sunlight/quit): ")
        if choice == "water":
            print(f"\n{player}, the tree is looking thirsty. How much water do you want to give it?")
            water = int(input("Enter a number of cups of water (1-5): "))
            water_tree(water)
        if choice == "sunlight":
            give_sunlight()
        if choice == "quit":
            print(f"\nGoodbye {player}! You earned {points} adventure points.")
            return
    print(f"\nCome back tomorrow {player}! You earned {points} adventure points.")


def water_tree(water: int) -> int:
    """Asks the player how much water to give the tree and updates the points accordingly."""
    global points, chance
    chance += 1
    if water < 1:
        print(f"{player}, the tree needs at least 1 cup of water to survive!")
    if water > 5:
        print(f"{player}, the tree can't handle that much water!")
    else:
        points += water
        print(f"\nYou gave the tree {water} cups of water. Your tree looks happier and healthier now!")
    return points


def give_sunlight() -> None:
    """Asks the player how long to give the tree sunlight and updates the points accordingly."""
    global points, chance
    chance += 1
    print(f"\n{player}, it's a beautiful day outside. How long would you like to give your tree sunlight?")
    length = int(input("Enter a number of hours (1-8): "))
    if length < 1:
        print(f"{player}, the tree needs at least 1 hour of sunlight to survive!")
    if length > 8:
        print(f"{player}, the tree can't handle that much sunlight!")
    else:
        bonus = randint(1, 3)
        points += length + bonus
        print(f"\nYou gave the tree {length} hours of sunlight, and it also got a {bonus} point bonus for some extra sunshine. Your tree looks happy and healthy now!")


if __name__ == "__main__":
    main()
