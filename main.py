import random
import string

# Set max chances available in game
MAX_CHANCES = 7

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
    chances = MAX_CHANCES
    # Control logic for game loop
    won = False
    # The string of letters guessed so far
    guessed_letters = ""
    # Count the loops, for displaying correct comments at right time
    loop_count = 0

    # Loop to keep game running
    while True:
        # The underscores representing letters to guess or guessed already
        word_display = define_length_of_word(word, guessed_letters)
        
        # Chances have been used, end the game
        if chances == 0:
            print(f"Sorry, you lost! The word was '{word}'")
            break

        # Create variable to display the used letters so far
        used_letters = ""
        # Loop through guessed letters to append the new variable with better spacing
        for letter in guessed_letters:
            used_letters += letter + " "

        # Display game information to player
        print("--- Guess the word! ---")
        print(f"Your word: " + word_display)
        print(f"Chances left: {chances}")
        if loop_count > 0:
            print(f"So far, you have used the following letters: {used_letters}")

        # Take the input for a character guess
        character = input("Enter a letter that could be in the word: ").lower()
        # Check length of input is not over 1 and is a letter
        if len(character) > 1 or not character.isalpha():
            print("Please enter one character at a time")
            continue
        elif character in guessed_letters:
            print("You have already used this letter, pick again!")
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
                loop_count += 1
        loop_count += 1



def ask_to_play_again():
    """
    Asks the user whether they want to play again.
    Keeps asking until a valid response ('y' or 'n') is received
    
    Returns:
        bool: True if the user wants to play again, False otherwise
    """
    # This loop will keep running until a valid input is received
    while True:
        # Convert to lowercase for consistency
        yes_or_no_to_play = input("Would you like to play again? (y/n): ").lower()
        if yes_or_no_to_play == "y":
            print("Great, let's play again!")
            return True
        elif yes_or_no_to_play == "n":
            print("Goodbye!")
            return False
        else:
            print("Please enter only 'y' or 'n'")

def main():
    """
    Main function to start the hangman game and handle replay logic.
    """
    continue_game = True
    while continue_game:
        # Start a new game
        start_hangman_game()
        # Ask if the user wants to play again and get a boolean response
        continue_game = ask_to_play_again()

if __name__ == "__main__":
    main()