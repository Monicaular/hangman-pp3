# Hangman

## Introduction <a name="introduction"></a>

Hangman is a classic that has been played by people of all ages on paper for many years, prior to the emergence of technology. </br>
It's a popular choice for those who enjoy intellectual challenges and want to spend quality time with their friends. </br>

This digital version of Hangman is designed to enhance the traditional paper game, but with the added feature that it can be played solo against the computer.

## Description <a name="description"></a>
 
As soon as the user starts the game, they will be prompted to enter a letter or a word. </br>
If the input is correct, a message will be displayed indicating the correct letter replacement. The gallows and the previously guessed letters will also be displayed. </br>
If the correct word is guessed, the whole word will be revealed, and a message indicating the success will be displayed. </br>
However, if the input is wrong, the user will be informed about their number of attempts, and the gallows with the penalty will be displayed.

Overall, Hangman is an enjoyable and demanding game that involves a combination of guessing abilities and vocabulary knowledge. It is a fantastic way to assess your skills and have a good time simultaneously.

![Screenshot of the start page of the hangman game](/readme-screenshots/initialising-game-screenshot.png)

**View the Hangman live game** [HERE](https://hangman-monica-pp3-cfdaaa86683d.herokuapp.com/)

# Table of contents
1. [Introduction](#introduction)
2. [Description](#description)
3. [How to Play](#how-to-play)
4. [Flowchart](#flowchart)
5. [User Experience (UX)](#user-experience)
    - [User Stories](#user-stories)
6. [Features](#features)
    - [Existing Features](#existing-features)
7. [Features to Implement](#features-to-implement)
8. [Designs](#designs)
9. [Technologies](#technologies)
10. [Frameworks, Libraries & Programs Used](#frameworks-used)
11. [Testing](#testing)
12. [Manual Testing](#manual-testing)
13. [Input Validation Testing](#input-validation-testing)
14. [Fixed Bugs](#fixed-bugs)
15. [Deployment](#deployment)
16. [Forking the GitHub Repository](#forking-the-github-repository)
17. [Local Clone](#local-clone)
18. [Credits](#credits)


## How to play <a name="how to play"></a>
The game will begin by asking the user to review the rules of the game. After that, the user will create a username and select the difficulty level. They will then proceed to play against the computer and will be prompted to guess either a word or a letter. The game will continue until the user has guessed all the letters or the entire word, or until they have run out of attempts.



## Flowchart <a name="flowchart"></a>


![Image with the Hangman game flowchart ](/readme-screenshots/hangman-game-flowchart.png)

## User Experience (UX) <a name="user experince"></a>

Hangman is a classic game that offers simple but entertaining gameplay. The game challenges players to guess a letter or the whole word in 6 tries. At the beginning of the game, a series of blank underscores is displayed, one for each letter of the word. This helps the player to determine the length of the word and to start guessing letters that could make it easier to win the game. 

If the user inputs a single letter, it is revealed only if it is correct, and its position is displayed on the screen. If the letter is incorrect, the user receives a message highlighted in red, and a graphic with the parts of the body that represent the remaining tries is displayed. The user is also allowed to write the whole word in one go, without being restricted to guessing a single letter.

Players can continue guessing letters until they reach the 6th try, at which point the game displays the hanged man's full body, indicating that the game has been lost.

The game is simple to grasp and offers a well-balanced mix of challenge and reward. It's also an enjoyable way to boost one's vocabulary and spelling abilities.

### User Stories <a name="user stories"></a>

* First Time visitor goals
    * To be able to understand easily what is the game about.
    * To understand how the game works by having instructions included.
    * To enjoy playing the game and want to replay it.
    * To recommend it to their friends.

* Returning visitor goals
    * To find themselves continuosly entertained.
    * To learn new words and add them to their vocabulary.
    * To explore a more dificult level. 

* Frequent user goals
    * To improve their speed and accuracy in guessing the words.
    * To up their level difficulty and feel challenged.
    * Recommending the game to their friends and relatives.
    
## Features <a name="features"></a>

* **Word selection** - the game starts with a pre-selected word that the player needs to guess.
* **Display of hidden words** - the word is initially displayed with blank underscores representing each letter.
* **Incorrect guess counter** - there is a counter that keeps track of the letters that have been entered already and number of tries left.
* **Feedback for correct and incorrect guess** - after each gueess, the game provides feedbsck by revealing the positions for the guessed letters and displaying a message letting them know if they guessed or not.
* **Graphics for hangman** - a visual representation of a hangman is gradually drawn for each incorrect guess. 
* **Difficulty setting** - the user can choose the difficulty level. 
* **Play again** - the user can choose to play again or to exit.

### Existing Features <a name="existing features"></a>
* **Start Screen**
    * Shows the graphic title and the welcome message

![Screenshot of the game title](/readme-screenshots/intro-screen.png)

* **Playing Rules**
    * User has the choice to view the play rules or to skip them

![Screenshot of the playing rules](/readme-screenshots/game-rules.png)

* **Creating a username and introduction message**
    * User can create a username

![Screenshot of creating username and introduction message](/readme-screenshots/create-username.png)

* **Difficulty Setting**
    * User can choose between easy, medium and hard

![Screenshot of choosing difficulty level](/readme-screenshots/difficulty-choice.png)

* **Guessing prompt**
    * Prompting the user for guessing letter or word

![Screenshot of the hidden word display](/readme-screenshots/make-a-guess.png)

* **Correct letter**
    * If letter is guessed, a message saying that letter is in the word will show

![Screenshot of the correct guess message](/readme-screenshots/guessed-letter.png)

* **Incorrect letter**

    * If the user inserts a wrong letter, a red message will be shown that the letetr is not in the hidden word

![Screenshot of the incorrect guess message](/readme-screenshots/incorrect-guess.png)

* **Guess of the word**
    * The user will get a congrats message if he guesses the word

![Screenshot of guessed word message](/readme-screenshots/guessed-word.png)

* **Out of tries**
    * User is shown a message that they are out of tries

![Screenshot of out of tries message](/readme-screenshots/out-of-tries-1.png)

* **Play Again**
    * User has the choice to play again or exit the game

![Screenshot of play again choice message](/readme-screenshots/play-again.png)

## Features to Implement <a name="features to implement"></a>

* Multiple player option
* Different word categories
* Wider range of words
* Score tracking system
* More advanced graphics

## Design <a name="design"></a>

* Colours
    * Pink
    * Lilac
    * Red
    * Green

* Flowchart
    * [Lucidchart](https://www.lucidchart.com/pages/)

## Technologies used <a name="technologies used"></a>

* [Phyton 3.12](https://www.python.org/)

## Frameworks, Libraries & Programs Used <a name="frameworks used"></a>

* [Codeanywhere](https://app.codeanywhere.com/)
    * To write the code for the game.
* [Git](https://git-scm.com/)
    * For version control.
* [Github](https://github.com/)
    * Deployment of the website and storing the files online.
* [Lucidchart](https://www.lucidchart.com/pages/)
    * To create the flowchart for the game
* [Heroku](https://dashboard.heroku.com/apps)
    * To deploy the project.
* [CI Python Linter](https://pep8ci.herokuapp.com/)
    * To check the code for errors.

## Testing <a name="testing"></a>

<details><summary>run.py - CI Python Linter Check</summary>

![Screenshot of the errors for the run.py file](/readme-screenshots/run-py-linter-check.png)

</details>

<details><summary>words.py - CI Python Linter Check</summary>

![Screenshot of the errors for the words.py file](/readme-screenshots/words-py-linter-check.png)

</details>

<details><summary>style.py - CI Python Linter Check</summary>

![Screenshot of the errors for the style.py file](/readme-screenshots/style-py-linter-check.png)

</details>

## Manual Testing <a name="manual testing"></a>

The game has been manually tested multiple times during the coding phase. Additionally, it was checked after being deployed to Heroku to ensure that all features are displaying as intended. Furthermore, friends and relatives have also tested the game. 
Testing was performed on various aspects, such as rules display, username input validation, select difficulty input validation, gallows ASCII image display, correct and incorrect answers, and win or lose display. Finally, the play again feature was also tested.

| Feature | Expected Result | Steps Taken | Actual Result | Screenshot |
| ------- | ----------------| ------------ | ------------ | ----------|
| Start Screen | To show the graphic and the welcome message| None | As intended | ![Screenshot with the logo and welcome message](/readme-screenshots/intro-screen.png) |
| Display Rules | To display rules or to skip them by using letters "y" and "n" | Insert "y" to view and "n" to skip | As intented | ![Screenshot of the displayed rules](/readme-screenshots/game-rules.png) |
| Create Username | To get username and use it in the game's messages | Insert alphanunumeric username | As intented | ![Screenshot os the entered username](/readme-screenshots/create-username.png) |
| Personalised Message With The Username | To display username in messages | None | As intented | ![Screenshot with the personalised messages](/readme-screenshots/personalised-message-lost.png) ![Another screenshot](/readme-screenshots/personalised-messsage-won.png) |
| Choose Difficulty Level | To retrieve the number from the options | Insert 1, 2 or 3 | As intented | ![Screenshot with the difficulty level options](/readme-screenshots/difficulty-choice.png) |
| Guess a letter or a word | Prompts the user to guess a letter or go for the whole word | Input a letter or a word to guess | As intented | ![Screenshot of the prompt to enter a letter or a word](/readme-screenshots/make-a-guess.png) |
| Correct Guess | To display the position of the letter, the gallows with no lost tries, a list of the letters that already been inserted | Guessed a correct letter | As intented | ![Screenshot of a correct guessed letter](/readme-screenshots/guessed-letter.png)
| Incorrect Guess | To display incorrect message, the gallows with the left tries, the list with the already insterted letted and updated word | Guessed wrong letter | As intented | ![Screenshot with the incorrect guess message](/readme-screenshots/incorrect-guess.png) |
| Repeated Guess | To display a message saying guessed already, no penalty applied | Input a letter previously inserted | As intented | ![Screenshot of a message for a second input of a letter](/readme-screenshots/previous-guess.png) |
| Hangman Gallows | To show the updated hangman gallows | Input several letters | As intented | ![Screenshots with the gallows updating whilist inserting right or wrong letters](/readme-screenshots/updating-gallows-incorrect.png) ![A second screenshot](/readme-screenshots/updating-gallows-correct.png) |
| Win The Game | To show congrats message and show the word | Guess the word in less than 6 tries | As intented | ![Screenshot with the win message](/readme-screenshots/guessed-word.png) |
| Lose The Game | To show a message confirming the lose | Fail to guess in 6 tries | As intended | ![Screenshot with the losing game message](/readme-screenshots/out-of-tries-1.png) |
| Play Again | To display the play again choice message | Choose between "y" and "n" | As intended | ![Screenshot with the play again message](/readme-screenshots/play-again.png) |

## Input validation testing <a name="input validation"></a>

* Display rules
    * Cannot conitue if the input is empty
    * It must be either a "y" or an "n"

![Screenshot with the validation for displaying the rules](/readme-screenshots/rules-input-validation.png)

* Enter username
    * Username cannot be empty
    * Username must be formed of letters and numbers
    * Username cannot contain special charcters
    * Username has a maximum 8 characters rule

![Screenshot for username input validation](/readme-screenshots/username-input-validation.png)

* Select difficulty level

    * Can only contain numbers
    * Can only have the values 1, 2 or 3

![Screenshot for difficulty level input validation](/readme-screenshots/difficulty-level-validation.png)

* Guess a letter or a word
    * Can only input letters

![Screenshot with inputing a special character](/readme-screenshots/guess-letters-words-validation.png)
![Screenshot with inputing a number](/readme-screenshots/guess-letters-words-validation-1.png)

* Play Again
    * Can only contain letters "y" and "n"
    * cannot contain spaces or special character

![Screenshot with the play again input validation](/readme-screenshots/play-again-validation.png)

## Fixed Bugs <a name="fixed bugs"></a>

* The hangman's final gallows stage did not appear when the game was lost. This have been resolved.
* When a space was inserted at the play again stage, the error message would not show up. However, the system would repeatedly ask if the user would like to play again if a space was mistakenly inputted. This has been resolved as shown above.
* The game would end even though the user would have guessed the letter at the last try. This has been resolved.
* All the above bugs were noticed by playing the game repeatedly whilist writing the code but also by friends that have tested it.

## Deployment <a name="deployment"></a>

In order to deploy this project to Heroku, Code Institute Python Essentials Template has been used so the python code can be viewed in a terminal browser.

**Steps**:
1. Log in to Heroku or create a new account.
2. On the home page click "New" and then select "Create new app".
3. Choose a unique app name and select the region.
4. Click "Create app".
5. On the next page look for "settings" and locate "Config Vars".
6. Click "Reveal Config Vars" and add "PORT" as a key and the value "8000", then click "Add".
7. Scroll down, locate "Buildpack" and click "Add", select "Python".
8. Repeat step 7. only this time add "Node.js", make sure "Python" is first.
9. Scroll to the top and select "Deploy" tab.
10. Select GitHub as deployment method and search for your repository and link them together.
11. Scroll down and select either "Enable Automatic Deploys" or "Manual Deploy".
12. Deployed site [Hangman](https://hangman-monica-pp3-cfdaaa86683d.herokuapp.com/).

## Forking the GitHub Repository <a name="forking depository"></a>

By forking the repository, we make a copy of the original repository on our GitHub account to view and change without affecting the original repository by using these steps:

1. Log in to GitHub and locate GitHub Repository [hangman-pp3](https://github.com/Monicaular/hangman-pp3). 
2. At the top of the Repository (under the main navigation) locate "Fork" button.
3. Now you should have a copy of the original repository in your GitHub account.


## Local Clone <a name="local-clone"></a>

To make a local clone in gihub, please follow the below steps:

1. Log in to GitHub and locate GitHub Repository [hangman-pp3](https://github.com/Monicaular/hangman-pp3).
2. Under the repository name click "Clone or download"
3. Click on the code button, select clone with HTTPS, SSH or GitHub CLI and copy the link shown.
4. Open Git Bash.
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone` and then paste The URL copied in the step 3.
7. Press Enter and your local clone will be created.

## Credits <a name="credits"></a>

### Content

* Hangam Game.
* All content has been written by the developer.

### Code
* Helped me understand how a hangman game works [Practice Python](https://www.practicepython.org/).
* How to add colors to text in Python [GeeksforGeeks](https://www.geeksforgeeks.org/how-to-add-colour-to-text-python/).
* Understanding the whole Python concept [Code Institute](https://learn.codeinstitute.net/dashboard).

## Acknowledgements

* My mentor Mitko Bacharov for continous helpful feedback.
* Code Insitute tutors for support.
* Slack Community for encouragement.
* Online communities like Stack Overflow for offering answers. 






