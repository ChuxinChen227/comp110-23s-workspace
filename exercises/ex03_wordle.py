"""EX03 - Structured Wordle"""

__author__ = "730564297"

def contains_char(secret: str, character: str) -> bool:
    """see if character is contained in the secret word"""
    assert len(character) == 1
    idx: int = 0
    found: bool = False
    while found is False and idx < len(secret):
        if (character == secret[idx]):
            # If the character is found in the secret word, exit the loop
            found = True 
        else:   # If the character does not appear in the secret word, check the next index
            idx = idx + 1
    return found

def emojified (guess: str, secret: str) -> str:
    """use colored emojis to indicate guess results"""
    assert len(guess) == len(secret)
    result: str = ""
    idx: int = 0
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    while idx < len(secret):
        # If the characters match, add a green box to the result
        if guess[idx] == secret[idx]:
            result = result + GREEN_BOX
        else: 
            contain: bool = contains_char(secret, guess[idx])
            if (contain is True):   # If the character appeared elsewhere, add a yellow box to the result
                result = result + YELLOW_BOX
            else:   # If the character does not appear elsewhere, add a white box to the result
                result = result + WHITE_BOX
        idx = idx + 1
    return result

def input_guess(length: int) -> str:
    """prompt the user to input a guess of the same length as the parameter"""
    guess: str = input(f"Enter a {str(length)} character word: ")
        # If the user enters wrong number of characters, prompt them to enter another guess
    while (len(guess) != length):
        guess = input(f"That wasn't {str(length)} chars! Try again: ")
    
    return guess

def main() -> None:
    """The entrypoint of the program and main game loop."""
    turn: int = 1
    secret: str = "python"
    while turn <= 6:
        print (f"=== Turn {turn}/6 ===")  # indicate the current turn number
        guess: str = input_guess(len(secret))  # prompt the user for a guess of the correct length
        result: str = emojified(guess, secret)  # codify the emoji result
        print (result)
        if guess == secret:  # print the result for correct guess and exit the program
            print (f"You won in {turn}/6 turns!")
            exit()
        else:  # if the guess is wrong move on to the next turn
            turn = turn + 1
    print (f"X/6 - Sorry, try again tomorrow!")  # exit the program when the turns are used up and print the result
        
if __name__ == "__main__":
    main()