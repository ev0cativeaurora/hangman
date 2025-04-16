import random

# We allow 10 attempts for Mastermind
MAX_ATTEMPTS = 10

# 10-stage Hangman ASCII – one for each “wrong guess” in Mastermind
HANGMAN_PICS = [
    """
        +---+
            |
            |
            |
            |
            ===
    """,
    """
        +---+
        O   |
            |
            |
            |
            ===
    """,
    """
        +---+
        O   |
        |   |
            |
            |
            ===
    """,
    """
        +---+
        O   |
       /|   |
            |
            ===
    """,
    """
        +---+
        O   |
       /|\\  |
            |
            ===
    """,
    """
        +---+
        O   |
       /|\\  |
       /     |
            ===
    """,
    """
        +---+
        O   |
       /|\\  |
       / \\  |
            ===
    """,
    """
        +---+
       \\O   |
       /|\\  |
       / \\  |
            ===
       (Extra face variation)
    """,
    """
        +---+
       \\O/  |
       /|\\  |
       / \\  |
            ===
       (Another variation)
    """,
    """
        +---+
       \\O/  |
       /|\\  |
       / \\  |
       | R.I.P. |
            ===
       (Final stage)
    """
]

def generate_secret_code():
    """
    Generates a list of 4 random colors from a set of 6 possible colors.
    Returns that list as the 'secret code'.
    """
    colors = ["red", "blue", "green", "yellow", "black", "white"]
    code = [random.choice(colors) for _ in range(4)]
    return code

def get_player_guess():
    """
    Prompts the user to enter 4 colors separated by spaces.
    Returns a list of 4 valid colors in lowercase.
    """
    while True:
        raw_input = input("Enter your 4 colors (e.g. 'red blue green yellow'): ").strip().lower()
        guess_list = raw_input.split()

        if len(guess_list) != 4:
            print("Please enter exactly 4 colors.")
            continue

        allowed_colors = {"red", "blue", "green", "yellow", "black", "white"}
        invalid = [color for color in guess_list if color not in allowed_colors]
        if invalid:
            print(f"Invalid colors: {invalid}. Allowed colors: {allowed_colors}")
            continue

        return guess_list

def check_guess(secret, guess):
    """
    Compares the player's guess with the secret code.
    Returns (blacks, whites):
      - blacks: correct color + correct position
      - whites: correct color, wrong position
    """
    blacks = 0
    whites = 0

    secret_remaining = []
    guess_remaining = []

    # 1) Count exact matches (blacks)
    for s, g in zip(secret, guess):
        if s == g:
            blacks += 1
        else:
            secret_remaining.append(s)
            guess_remaining.append(g)

    # 2) Count whites (correct color, wrong position)
    for color in guess_remaining:
        if color in secret_remaining:
            whites += 1
            secret_remaining.remove(color)

    return (blacks, whites)

def show_hangman_stage(stage_index):
    """
    Displays the ASCII stage of 'Hangman' for the given index.
    stage_index goes from 0 to 9 (for 10 attempts).
    """
    # If stage_index >= len(HANGMAN_PICS), we can show the final stage or just clamp it
    if stage_index >= len(HANGMAN_PICS):
        stage_index = len(HANGMAN_PICS) - 1
    print(HANGMAN_PICS[stage_index])

def game():
    """
    Runs one round of Mastermind with hangman visuals:
      - Generates a secret code
      - Prompts the user (up to MAX_ATTEMPTS times)
      - Shows black/white feedback
      - Each 'wrong' guess => next hangman stage
      - Return True if player guesses code, else False
    """
    secret_code = generate_secret_code()
    print("Secret code has 4 colors. Available colors: red, blue, green, yellow, black, white.")
    
    attempts_used = 0

    while attempts_used < MAX_ATTEMPTS:
        guess = get_player_guess()
        blacks, whites = check_guess(secret_code, guess)
        
        if blacks == 4:
            # The code is entirely correct
            print("You guessed the entire code!")
            return True
        else:
            # Wrong guess => increment attempts_used
            attempts_used += 1
            print(f"Result for your guess: {blacks} black(s), {whites} white(s)")
            show_hangman_stage(attempts_used - 1)  # stage index is attempts_used-1
            attempts_left = MAX_ATTEMPTS - attempts_used
            print(f"Attempts left: {attempts_left}\n")
    
    # If we exit the loop, the user used all attempts without 4 blacks
    print(f"No attempts left! You lose. The secret was {secret_code}.")
    return False

def play_again():
    """
    Asks if the user wants to play again.
    Returns True for "yes", False otherwise.
    """
    answer = input("Would you like to play again? (y/n): ").lower().strip()
    return answer in ("y", "yes")

def start():
    """
    Starts the Mastermind game with Hangman visuals, repeating until the user quits.
    """
    print("\nWelcome to Mastermind!")
    print("Instructions:")
    print(f"- You have {MAX_ATTEMPTS} attempts to guess the code.")
    print("- Each guess, you enter 4 colors (e.g., red blue green yellow).")
    print("- We respond with how many are correct in color+position (blacks),")
    print("  and how many are correct in color but not position (whites).")
    print("- If you fail a guess, we draw the next stage of 'Hangman'!")
    print("")

    while True:
        won = game()
        if won:
            print("Congrats on cracking the code!")
        else:
            print("Better luck next time!")
        
        if not play_again():
            break

    print("Thanks for playing Mastermind with Hangman visuals! Goodbye.")

if __name__ == "__main__":
    start()
