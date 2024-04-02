import random

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

print(get_random_word_from_word_list())
