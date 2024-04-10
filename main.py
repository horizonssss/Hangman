import random
import string

# Set max chances available in game
MAX_CHANCES = 7

def select_difficulty():
    """
    Lets the player select a difficulty level which adjusts the MAX_CHANCES
    """
    global MAX_CHANCES
    print("\nSelect difficulty:")
    print("1. Easy (10 chances)")
    print("2. Medium (7 chances)")
    print("3. Hard (5 chances)")
    difficulty = input("Enter your choice (1/2/3): ")

    if difficulty == "1":
        MAX_CHANCES = 10
    elif difficulty == "2":
        MAX_CHANCES = 7
    elif difficulty == "3":
        MAX_CHANCES = 5
    else:
        print("Invalid selection. Defaulting to Medium.")
        MAX_CHANCES = 7


def get_random_word_from_word_list(subject_file):


    try:
        with open(subject_file, 'r') as file:
            # Strip whitespace and newlines
            wordlist = [line.strip().lower() for line in file.readlines()]
        # Return random word from list
        return random.choice(wordlist)
    except FileNotFoundError:
        print()
        print(f"Error: '{subject_file}' file not found.")

        return None
    except Exception as e:
        print()
        print(f"An error has occurred: {e}")
        return None
    
def provide_hint(word, guessed_letters):
    """
    Provides a hint by revealing an unguessed letter in the word
    Reduces the player's chances by one as a cost for using the hint

    Parameters:
        word (str): The word to be guessed.
        guessed_letters (str): Letters guessed so far

    Returns:
        str: A letter from the word not yet guessed
    """
    unguessed_letters = [letter for letter in word if letter not in guessed_letters]
    if unguessed_letters:
        return random.choice(unguessed_letters)
    return ''

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
    Prints out the hangman picture, depending on remaining chances

    Parameters:
        integer (int): Remaining incorrect guesses, dictates the hangman's drawing stage
    """
    stages = [
        "________ \n| | \n| 0 \n| /|\\ \n| / \\ \n| ",
        "________ \n| | \n| 0 \n| /|\\ \n| / \n| ",
        "________ \n| | \n| 0 \n| /|\\ \n| \n| ",
        "________ \n| | \n| 0 \n| /| \n| \n| ",
        "________ \n| | \n| 0 \n| / \n| \n| ",
        "________ \n| | \n| 0 \n| \n| \n| ",
        "________ \n| | \n| \n| \n| \n| "
    ]
    # Adjust to show correct stage
    print()
    print(stages [0 + chances])

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
    # Game start message
    print()
    print("Welcome to Hangman")
    print("------------------")

    # Select and update the difficulty by changing number of chances
    select_difficulty()

    # Offer choice for word subjects with loop to validate input
    subject_chosen = False
    while subject_chosen == False:
        print()
        print("What subject would you like the word to be based on?")
        print("\nEither:\n-------\nOcean (o)\nForest(f)\nCities(c)\nSkies (s)\n")
        subject = input("Please enter your selection: ").lower()

        if subject not in ["o", "f", "c", "s"]:
            print()
            print("Please enter a valid choice")
        else:
            subject_chosen = True
    # Create a dictionary for the files
    word_sources = {
    'o': 'ocean_words.txt',
    'f': 'forest_words.txt',
    'c': 'cities_words.txt',
    's': 'skies_words.txt',
    }
    # Choose random word from correct file depending on subject selection
    word = get_random_word_from_word_list(word_sources[subject])

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
            print()
            print(f"Sorry, you lost! The word was '{word}'")
            break

        # Create variable to display the used letters so far
        used_letters = ""
        # Loop through guessed letters to append the new variable with better spacing
        for letter in guessed_letters:
            used_letters += letter + " "

        # Display game information to player
        print("\n\n")
        print("--- Guess the word! ---")
        print()
        print(f"Your word: " + word_display)
        print()
        print(f"Chances left: {chances}")
        if loop_count > 0:
            print()
            print(f"So far, you have used the following letters: {used_letters}")
        
        # Give user an option for a hint (insert random letter)
        print("\nDo you want a hint? This will cost you one chance. (y/n): ")
        # Input the option
        hint_choice = input().lower()
        if hint_choice == 'y':
            # Make sure player has at least one chance to use a hint
            if chances > 1:
                hint = provide_hint(word, guessed_letters)
                guessed_letters += hint  # Add the hinted letter to guessed letters
                chances -= 1  # Reduce chances by one as a cost for the hint
                print(f"Here's your hint: {hint} is in the word.")
            else:
                print("Not enough chances left to use a hint!")
        # Take the input for a character guess
        print()
        character = input("Enter a letter that could be in the word: ").lower()
        # Check length of input is not over 1 and is a letter
        if len(character) > 1 or not character.isalpha():
            print()
            print("Please enter one character at a time")
            continue
        elif character in guessed_letters:
            print()
            print("You have already used this letter, pick again!")
        # Append the guessed character to the guessed letters string
        else:
            guessed_letters += character
            if character in word:
                print()
                print("You guessed a letter correct!")
                # A variable to check if the letters guessed equal the word
                guessed_letters_without_whitespace = define_length_of_word(word, guessed_letters).replace(" ", "")
                # Check word has been guessed correctly or letter guessed correctly
                if guessed_letters_without_whitespace == word:
                    print()
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
        print()
        yes_or_no_to_play = input("Would you like to play again? (y/n): ").lower()
        if yes_or_no_to_play == "y":
            print()
            print("Great, let's play again!")
            return True
        elif yes_or_no_to_play == "n":
            print()
            print("Goodbye!")
            return False
        else:
            print()
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