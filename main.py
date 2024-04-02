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

def define_length_of_word(word):
    """
    Defines the length of a given input word, returning underscores
    for the length of a word with spaces in between.

    Parameters:
        word (str or None): The word to be processed or None.

    Returns:
        str: Underscore and space per letter input.
    """
    # Check word is not None
    if word is None:
        return "No word provided, please provide a word."
    # Initialise the underscores variable
    underscores = ""
    # Add an underscore & space for each letter in the word
    underscores = len(word) * "_ "

    return underscores

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

def remaining_letters(guessed_letters):
    """
    Prints the alphabet with letters that have been guessed crossed out.

    Parameters:
    guessed_letters (set or list): The letters that have been guessed so far.
    """
    if guessed_letters is None:
        return None
    
    guessed_letters_before_strike = ""
    for letter in guessed_letters:
        if letter in string.ascii_lowercase:
            guessed_letters_before_strike += letter + '\u0336'
    print(guessed_letters_before_strike)





# Testing
print(define_length_of_word(get_random_word_from_word_list()))
remaining_letters("abcx")