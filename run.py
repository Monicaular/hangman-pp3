

def show_title():
    """
    Shows the the name of the game in a more graphical style
    """
    
    game_title = """
  _    _            _   _   _____  __  __            _   _ 
 | |  | |    /\    | \ | | / ____||  \/  |    /\    | \ | |
 | |__| |   /  \   |  \| || |  __ | \  / |   /  \   |  \| |
 |  __  |  / /\ \  | . ` || | |_ || |\/| |  / /\ \  | . ` |
 | |  | | / ____ \ | |\  || |__| || |  | | / ____ \ | |\  |
 |_|  |_|/_/    \_\|_| \_| \_____||_|  |_|/_/    \_\|_| \_|
                                                         
Welcome to Hangman Game!
    """
    print(game_title)

def show_rules():
    """
    Displays the game's rules - if the users wishes to
    """
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
            print(rule)
    else:
        print("You choose to skip the rules. Let's start the game")

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

def main():
    show_title()
    show_rules()
    add_username()
    
    
    

if __name__ == "__main__":
    main()