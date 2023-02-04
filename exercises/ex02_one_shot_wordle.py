"""EX02 - One-Shot Wordle - Loops!"""

__author__ = "730564297"

SECRET: str = "python"
guess: str = input(f"What is your {len(SECRET)}-letter guess? ")
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
idx: int = 0
result: str = ""
elsewhere: bool = False 
alt_idx: int = 0

# Check each character of the secret word
while idx < len(SECRET):
    # If the user enters wrong number of characters, prompt them to enter another guess
    if (len(guess) != len(SECRET)):
        guess = input(f"That was not {len(SECRET)} letters! Try again: ")
    else:
        # If the characters match, add a green box to the result
        if guess[idx] == SECRET[idx]:
            result = result + GREEN_BOX
        else: 
            while elsewhere == False and alt_idx < len(SECRET):
                if (guess[idx] == SECRET[alt_idx]):
                    # If the character is found elsewhere, exit the loop
                    elsewhere = True 
                else: # If the character does not appear elsewhere, check the next index
                    alt_idx = alt_idx + 1
            if (elsewhere == True): # If the character appeared elsewhere, add a yellow box to the result
                result = result + YELLOW_BOX
            else: # If the character does not appear elsewhere, add a white box to the result
                result = result + WHITE_BOX
        elsewhere = False
    idx = idx + 1
    alt_idx = 0
if guess == SECRET: # print the result for correct guess
    print(f"{result}\nWoo! You got it!")
else: # print the result for incorrect guess
    print(f"{result}\nNot quite. Play again soon!")
            
