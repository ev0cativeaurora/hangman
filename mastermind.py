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

