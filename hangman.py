import random

# Keep track of scores
player_score = 0
computer_score = 0


# Select random word from file
def word():
    """
    Picks a random word from 'words.txt'.
    """
    word_list = open("words.txt", "r").readlines()
    # Use randint(0, len(word_list) - 1) or randrange for safety
    random_number = random.randint(0, len(word_list) - 1)
    chosen_word = word_list[random_number].rstrip()
    # Convert to lowercase to match user guesses
    chosen_word = chosen_word.lower()
    return chosen_word


# Game graphics
def hanged(man):
    """
    Returns the ASCII hangman stage for the given number of wrong guesses.
    """
    graphic = [
    '''
       +------+
       |
       |
       |
       |
       |
    ==============
    ''',
    '''
       +------+
       |      |
       |      O
       |
       |
       |
    ==============
    ''',
    '''
       +------+
       |      |
       |      O
       |      |
       |
       |
    ==============
    ''',
    '''
       +------+
       |      |
       |      O
       |     -|
       |
       |
    ==============
    ''',
    '''
       +------+
       |      |
       |      O
       |     -|-
       |
       |
    ==============
    ''',
    '''
       +------+
       |      |
       |      O
       |     -|-
       |     /
       |
    ==============
    ''',
    '''
       +------+
       |      |
       |      O
       |     -|-
       |     / \\
       |
    ==============
    '''
    ]
    return graphic[man]


# Game Menu 
def start():
    """
    Starts the Hangman game session, shows welcome message and instructions,
    and loops over new games until the player chooses to stop.
    """
    print("\nWelcome to Hangman!")
    print("Instructions:")
    print("1. You have 6 attempts to guess the word.")
    print("2. One wrong guess removes one attempt.")
    print("3. If you guess the same letter again, you'll be asked to pick another letter.")
    print("4. Enjoy the game!\n")

    # Start the main loop of the game
    while game():
        pass

    # After exiting the loop, show final scores
    print("")
    scores()
