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



