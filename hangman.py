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

