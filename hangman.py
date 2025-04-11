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

def game():
    """
    One round of Hangman:
      - Picks a random word
      - Asks the player to guess letters
      - Tracks correct/incorrect guesses
      - Shows ASCII gallows
      - Returns True if player wants to play again, False otherwise
    """
    the_word = word()
    print("The word has {} letters.".format(len(the_word)))

    clue = ["-" for _ in the_word]
    print("")
    print("".join(clue))

    tries = 6
    letters_tried = ""
    letters_wrong = 0

    global player_score, computer_score

    while letters_wrong < tries and "".join(clue) != the_word:
        letter = guess_letter()

        if len(letter) == 1 and letter.isalpha():
            if letters_tried.find(letter) != -1:
                print(f"You've already picked '{letter}'. Please choose another letter.")
                # Continue the loop without penalizing the user
                continue
            else:
                letters_tried += letter
                # Check if the guess is in the word
                if letter in the_word:
                    print(f"Yay! {letter} is correct.")
                    for i in range(len(the_word)):
                        if the_word[i] == letter:
                            clue[i] = letter
                else:
                    letters_wrong += 1
                    print(f"Sorry, there isn't any '{letter}' in the word.")
        else:
            print("Please enter exactly one alphabetic character.")
            # Continue without penalizing
            continue

        # Display ASCII gallows, current clue, and guesses so far
        print(hanged(letters_wrong))
        print("".join(clue))
        print("")
        print("Guesses so far:", letters_tried)

        if letters_wrong == tries:
            print("Game Over!")
            print(f"The word was '{the_word}'")
            computer_score += 1
            break

        if "".join(clue) == the_word:
            print("You Win!")
            print(f"The word was '{the_word}'")
            player_score += 1
            break

    return play_again()


def guess_letter():
    """
    Prompts the user for a guess and returns it in lowercase, stripped of whitespace.
    """
    letter = input("\nGuess a letter: ")
    letter = letter.strip().lower()
    return letter

