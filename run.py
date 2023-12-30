

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

def main():
    show_title()
    show_rules()
    
    
    

if __name__ == "__main__":
    main()