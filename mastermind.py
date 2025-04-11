import random

# You might track the number of attempts or store other global info
MAX_ATTEMPTS = 10

def start():
    """
    Placeholder for Mastermind game logic.
    We'll adapt Hangman structure to Mastermind step by step.
    """
    print("Welcome to Mastermind!")
    print(f"You have {MAX_ATTEMPTS} attempts to guess the secret code.")


def generate_secret_code():
    """
    Generate a list of 4 random colors (from a set of 6).
    Example colors: ["red", "blue", "green", "yellow", "black", "white"]
    """
    colors = ["red", "blue", "green", "yellow", "black", "white"]
    code = [random.choice(colors) for _ in range(4)]
    return code



def game():
    """
    Runs one round of Mastermind.
      - Generates a secret code
      - Loops up to MAX_ATTEMPTS
      - Asks player for a combination
      - Gives feedback (to be implemented) 
      - Ends when player guesses the code or runs out of attempts
    """
    secret = generate_secret_code()
    print("Secret code has 4 colors. Available colors: red, blue, green, yellow, black, white.")
    # For debug, you could print the secret code:
    # print(f"[DEBUG] The secret is: {secret}")

    attempts_left = MAX_ATTEMPTS
    while attempts_left > 0:
        guess = get_player_guess()
        # We'll implement a function to compare guess vs secret soon
        # For now, just reduce attempts by 1
        attempts_left -= 1

        # If guess is the secret, break
        # We'll do a real check in next step
        if guess == secret:  # placeholder logic
            print("You guessed exactly (placeholder check)!")
            return True  # or some victory condition

        print(f"Attempts left: {attempts_left}")

    # If we exit the loop, we ran out of attempts
    print("No attempts left. You lose. (placeholder)")
    return False



def get_player_guess():
    """
    Prompts the user to enter 4 colors separated by spaces.
    Returns a list of colors in lowercase.
    """
    while True:
        raw_input = input("Enter your 4 colors (e.g. 'red blue green yellow'): ").strip().lower()
        guess_list = raw_input.split()

        if len(guess_list) != 4:
            print("Please enter exactly 4 colors.")
            continue

        # Optional: validate each color is in the allowed set
        allowed = {"red", "blue", "green", "yellow", "black", "white"}
        invalid = [color for color in guess_list if color not in allowed]
        if invalid:
            print(f"Invalid colors: {invalid}. Allowed: {allowed}")
            continue

        return guess_list


def check_guess(secret, guess):
    """
    Returns (blacks, whites) for the guess compared to the secret.
    - blacks = # of positions that match exactly
    - whites = # of correct colors but in wrong positions
    """
    # Step 1: count blacks
    blacks = 0
    secret_remaining = []
    guess_remaining = []

    for s, g in zip(secret, guess):
        if s == g:
            blacks += 1
        else:
            secret_remaining.append(s)
            guess_remaining.append(g)

    # Step 2: count whites
    whites = 0
    # For each color in guess_remaining, if it's in secret_remaining, count it and remove one occurrence
    for color in guess_remaining:
        if color in secret_remaining:
            whites += 1
            secret_remaining.remove(color)

    return (blacks, whites)



def game():
    secret = generate_secret_code()
    print("Secret code has 4 colors. Available colors: red, blue, green, yellow, black, white.")
    attempts_left = MAX_ATTEMPTS

    while attempts_left > 0:
        guess = get_player_guess()
        attempts_left -= 1

        blacks, whites = check_guess(secret, guess)
        print(f"Result for your guess: {blacks} black(s), {whites} white(s)")

        if blacks == 4:
            print("You guessed the entire code!")
            return True

        print(f"Attempts left: {attempts_left}\n")

    print(f"No attempts left! You lose. The secret was {secret}.")
    return False
