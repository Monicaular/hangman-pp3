import words
import random
from style import Color, style_colors


def show_title():
    """
    Shows the the name of the game in a more graphical style
    """
    lilac_color = style_colors['lilac']
    
    game_title = """
  _    _            _   _    _____   ___  ___            _   _
 | |  | |    /\\    | \\ | |  / ____| |   \\/   |    /\\    | \\ | |
 | |__| |   /  \\   |  \\| | | |  __  |  \\  /  |   /  \\   |  \\| |
 |  __  |  / /\\ \\  | . ` | | | |_ | |  |\\/|  |  / /\\ \\  | . ` |
 | |  | | / ____ \\ | |\\  | | |__| | |  |  |  | / ____ \\ | |\\  |
 |_|  |_|/_/   \\__\\|_| \\_|  \\___| | |__|  |__|/_/   \\__\\|_| \\_|
                                                         
Welcome to Hangman Game!
    """
    coloured_game_title = lilac_color.format(game_title)
    print(coloured_game_title)


def show_rules():
    """
    Displays the game's rules - if the users wishes to
    """
    pink_color = style_colors['pink']
    display_rules = input("Would you like to see the game rules? (Y/N)\n ")
    while display_rules.upper() not in ["Y", "N"]:
        display_rules = input('Please only insert Y or N\n').upper()
    
    if display_rules.upper() == "Y":
        rules = [
            "Insert your username so we know who are we playing with",
            "Choose a difficulty level between easy, medium, and hard",
            "Choose a letter or a word to guess",
            "A correct letter will show you its position(s) in the word",
            "A wrong letter would add to the hangman",
            "You have six tries to guess, otherwise the man will be hanged",
            "Let's begin the fun"
        ]
        print("\nPlaying Rules:\n ")
        # displays the rules in multiple lines
        for rule in rules:
            formatted_rule = pink_color.format(rule)
            print(f"  - {formatted_rule}")
            
    else:
        print("You chose to skip the rules. Let's start the game")

def add_username():
    """
    Asks the player to insert a username and validates the input
    """   
    while True:
        try:
            print()
            username = input("Please enter a username:\n")
            # Check if the input contains spaces
            if " " in username:
                raise ValueError("Username cannot contain spaces.")
            # Check if the input contains only numbers and letters
            if not username.isalnum():
                raise ValueError("Please enter letters and numbers.")
            # Check if the input contains only spaces
            if not username.strip():
                raise ValueError("Please enter letters and numbers.")
            # Check if the input exceeds 8 characters
            if len(username) > 8:
                raise ValueError("Username must not exceed 8 characters.")
        # Catch any ValueError exception and print the error message
        except ValueError as e:
            print(f"{e}")
        # If no exception is raised, print a message and return the name
        else:
            print(f"\n{username.capitalize()}, get ready to unravel the mystery!")
            return username


def choose_difficulty():
    """
    Gets the user to choose the difficulty of the game that they prefer
    """
    while True:
        try:
            print("\nChoose the difficulty level:")
            print("1 - Easy")
            print("2 - Medium")
            print("3 - Hard")

            choice = input("Choose between 1, 2 and 3: ")
            choice = int(choice)
            # Validate user input
            if choice not in [1, 2, 3]:
                raise ValueError("\nInvalid choice. Please enter 1, 2, or 3.\n")
            return choice  # Return the selected choice
        except ValueError as e:
            print(e)


def extract_word(word_list):
    """
    Returns a randomly selected word from the given word list.
    """
    word = random.choice(word_list)
    return word.upper()


def game_play(word, username):
    """
    Checks if inserted letters and words are correct and validates them
    """
    red_color = style_colors['pale_red']
    green_color = style_colors['bright_green']
    word_completed = "_" * len(word)
    guessed_letters = set()
    guessed_words = set()
    tries = 6

    while tries > 0:
        game_state(word, guessed_letters, tries)
        guess = input("Please guess a letter or a word:\n ").upper()

        if tries == 1:
            print(red_color.format("This is your last chance, choose carefully"))

        # Checks if the input is a single letter
        if guess.isalpha() and len(guess) == 1:
            # Checks if the input is in the previously input list
            if guess in guessed_letters:
                print(f"You already guessed the letter {guess}. Try again.")
            # Checks that the word does not contain the input letter
            elif guess not in word:
                error_message = f"{guess} is not in the word."
                print(red_color.format(error_message))
                tries -= 1
                guessed_letters.add(guess)
            # Checks that the word contains the input letter
            else:
                guess_message = f"Terrific, {guess} is in the word."
                print(green_color.format(guess_message))
                guessed_letters.add(guess)
                # Converts the string into a list of charcters
                word_as_list = list(word_completed)
                # Shows where the guessed letters are situatued in the word
                indices = [
                    i for i, letter in enumerate(word)
                    if letter == guess
                ]

                for index in indices:
                    word_as_list[index] = guess

                # Joins the elements of the list into a string
                word_completed = "".join(word_as_list)

                # Checks if there are more space in the word
                if "_" not in word_completed:
                    print(f'Well Done! You guessed the word: {word}')
                    return
            
        # Checks if the input is multiple letters
        elif guess.isalpha() and len(guess) > 1:
            # Checks if the input word matches the word
            if guess == word:
                congrats_message = f"Nicely done, you are a Hangman pro {username.capitalize()}"
                print(green_color.format(congrats_message))
                print(f'You guessed the word: {word}')
                return
            else:
                print("Incorrect word guess. Try again.")
                tries -= 1
                guessed_words.add(guess)
        else:
            print("Invalid input. Please enter letters.")
    print(f"Nice try, perhaps you need more practice, {username.capitalize()}.")
    print(f"The word was: {word}")

def game_state(word, guessed_letters, tries):
    """
    It provides the Hangman Game implementation and
    makes a more user friendly display
    """
    # Displays the hangman graphic
    print(words.hangman_graphic[6 - tries])
    display_word = " ".join([letter if letter \
                            in guessed_letters else "_" for letter \
                            in word])
    print(f"Word: {display_word}")
    print(f"You have {tries} tries left")
    print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")

def play_hangman_again():
    """
    It asks the player if they want to play again
    """
    while True:
        play_again = input("Would you like to play again? (y/n):\n ").lower()

        if play_again == 'y':
            main()
        elif play_again == 'n':
            print("Thanks for playing Hangman! Goodbye!")
            break
        else:
            print("Invalid input. Please enter 'y' to play again or\
                  'n' to exit.")

def main():
    """
    This function is the primary driver of the game program,
    It first displays the title of the game,
    Then it displays the rules and adds a username, 
    It prompts the user to choose the difficulty and assigns it,
    Selects a random word from the chosen word list, 
    Initiates the game play and
    lastly it prompts the user to decide whether to play the game again. 
    """
    show_title()
    show_rules()
    username = add_username()
    level = choose_difficulty()

    if level == 1:
        word_list = words.easy_level_words
    elif level == 2:
        word_list = words.medium_level_words
    else:
        word_list = words.hard_level_words

    word = extract_word(word_list)

    print(f"Chosen difficulty level: {level}")

    game_play(word, username)

    play_hangman_again()

if __name__ == "__main__":
    main()
