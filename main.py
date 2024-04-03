import random
import string

def get_random_word_from_word_list():
    """
    Reads a list of words from a text file named 'word_list.txt', 
    selects a random word from the list, and returns it. If the file
    cannot be opened, prints an error message and returns None.
    
    Returns:
        str: A random word from the list, or None if the file can't be read.
    """
    try:
        with open("word_list.txt", 'r') as file:
            # Strip whitespace and newlines
            wordlist = [line.strip() for line in file.readlines()]
        # Return random word from list
        return random.choice(wordlist)
    except FileNotFoundError:
        print("Error: 'word_list.txt' file not found.")
        return None
    except Exception as e:
        print(f"An error has occurred: {e}")
        return None

def define_length_of_word(word, guessed_letters):
    """
    Returns a string representing the word with underscores for unguessed letters and the actual letter for guessed ones

    Parameters:
        word (str): The word to be guessed
        guessed_letters (str): Letters guessed so far

    Returns:
        str: A string with guessed letters revealed and underscores for the rest
    """
    # Check word is not None
    if word is None:
        return "No word provided, please provide a word."
    
    # Initialise display variable
    display = ""
    
    # Check each letter against the guessed letters
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "  # Add the letter and a space
        else:
            display += "_ "  # Add an underscore and a space for unguessed letters

    return display


def draw_hangman(chances):
    """
    Prints out the hangman picture, depending on remaining chances.

    Parameters:
        integer (int or None): The number to be processed or None.
    """
    if chances == 6:
        print("________ ")
        print("| | ")
        print("| ")
        print("| ")
        print("| ")
        print("| ")
    elif chances == 5:
        print("________ ")
        print("| | ")
        print("| 0 ")
        print("| ")
        print("| ")
        print("| ")
    elif chances == 4:
        print("________ ")
        print("| | ")
        print("| 0 ")
        print("| / ")
        print("| ")
        print("| ")
    elif chances == 3:
        print("________ ")
        print("| | ")
        print("| 0 ")
        print("| /| ")
        print("| ")
        print("| ")
    elif chances == 2:
        print("________ ")
        print("| | ")
        print("| 0 ")
        print("| /|\ ")
        print("| ")
        print("| ")
    elif chances == 1:
        print("________ ")
        print("| | ")
        print("| 0 ")
        print("| /|\ ")
        print("| / ")
        print("| ")
    elif chances == 0:
        print("________ ")
        print("| | ")
        print("| 0 ")
        print("| /|\ ")
        print("| / \ ")
        print("| ")

def remaining_letters(guessed_letters = ''):
    """
    Returns a string of the alphabet with letters that have been guessed crossed out

    Parameters:
        Guessed_letters (str): A string of letters that have been guessed so far. Defaults to an empty string

    Returns:
        str: A string of the alphabet with guessed letters crossed out

    Raises:
        ValueError: If guessed_letters is not a string
    """
    # Validate input type
    if not isinstance(guessed_letters, str):
        raise ValueError("guessed_letters must be a string")
    
    # Convert guessed_letters to lowercase for ascii_lowercase comparison
    guessed_letters = guessed_letters.lower()

    # Initialise the display string
    display_letters = ""

    # Build the string with guessed letters crossed out
    for letter in string.ascii_lowercase:
        if letter in guessed_letters:
            display_letters += (letter + '\u0336' + " ") # Cross out guessed letter
        else:
            display_letters += (letter + " ") # Include other letters
    return display_letters

def start_hangman_game():
    """
    Initialises the game, acts as main running loop
    """
    # Create a random word to be guessed
    word = get_random_word_from_word_list()
    # Amount of chances given to player
    chances = 7
    # Control logic for game loop
    won = False
    # The string of letters guessed so far
    guessed_letters = ""

    # Loop to keep game running
    while True:
        # The underscores representing letters to guess or guessed already
        word_display = define_length_of_word(word, guessed_letters)
        
        # Chances have been used, end the game
        if chances == 0:
            print(f"Sorry, you lost! The word was '{word}'")
            print("Goodbye!")
            break
        # Display the information to player
        print("--- Guess the word! ---")
        print(f"Your word: " + word_display)
        print(f"Chances left: {chances}")

        # Take the input for a character guess
        character = input("Enter a letter that could be in the word: ")
        # Check length of input is not over 1 and is a letter
        if len(character) > 1 or not character.isalpha():
            print("Please enter one character at a time")
            continue
        # Append the guessed character to the guessed letters string
        else:
            guessed_letters += character
        if character in word:
            print("You guessed a letter correct!")
            # A variable to check if the letters guessed equal the word
            guessed_letters_without_whitespace = define_length_of_word(word, guessed_letters).replace(" ", "")
            # Check word has been guessed correctly or letter guessed correctly
            if guessed_letters_without_whitespace == word:
                print(f"You won! The word was '{word}'")
                won = True
                break
        else:
            chances -= 1
            draw_hangman(chances)



# Testing

start_hangman_game()

# Notes, to do:
# 1. Create loop for play again function
# 2. Create logic for recognising letters already tried
# 3. Create function for displaying letters already tried