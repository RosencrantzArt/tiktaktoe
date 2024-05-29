# Hangman game
![Image of website](documentation/screenshots/hangman_firstpage.JPG)
[Link to live site](https://klaras-hangman-9d12372b114c.herokuapp.com/)

The Hangman game is a Python terminal game deployed to Heroku. The goal of this game is to guess the secret word with one letter at a time. If the player guess it's wrong to many times the man hangs. If the player guess the word the man survives.

## User Experience
### Site purpose
To provide a simple fun game for people that want to challenge themself. 

###

### User Goals
As a user I want:
* First of all to have a simple fun game and be challenged. (The user get's challenged with diffrent levels of difficulty and randomised words at every round.)
* Secondly, to learn how to play and understand the game. (The user get's to understand the game if they read the rules.)
* To play the game without any issues. (If an invalid input occurs the player get's to know what is wrong with an error message.)
* To easily navigate through available options and have clear feedback on my inputs. (The user get's direct feedback when guessing a letter correct or wrong.)
* To know if I won the game or not and what the secret word was. (The user get's feedback if the won or lose when the game is over. They also get's to know what the secret word was.)

### Project Goals
As a programmer of the game, I want the user to meet their goals (above). I also want the game to run smoothly with no bugs.

## Flowchart
* Start the game 
* Player 1 (X) starts
* Shows the gameboard
* Player 1 or 2 makes a move
* Check if the move is valid
* If invalid, go back to Player move if valid update gameboard
* Check for win 
* If Win display win meassage and end the game.If no, proceed to the next step
* Check for draw. If draw end the game. If no, proceed to next step. 
* Switch player. If it was player 1, swith to player 2 and vice versa)
* Repeat. Go back to "Display the game board" 
* End the game
![Design FlowChart](assets/images/flowchart.png)



## Features
### Existing features

## Testing
### Manual testing

### Automated testing

## Technologies Used
* Languages: 
    * Python.
* Libraries:
    
## Bugs
### Fixed bugs

### Remaining bugs


## Deployment
 The app was deployed through Heroku. The steps are as following:

1. Log into Github and locate [Github Repository](https://github.com/KlaraMartinsson/hangman-game).
2. After creating a Heroku account, click "New" to create a new app from the dashboard.
3. Create a unique name for the app and select your region: press "Create app".
4. Go to settings and add the necessary Config_vars and buildpacks. Ensure that the buildpacks are set to `Python` and `NodeJS`.
5. Click `Deploy`.
6. Scroll Down to Deployment Method and select GitHub.
7. Select the name of the repository from Github to be deployed and connect to Heroku.
8. Scroll down to the deploy options: 
Click enable Automatic deploys (Will Update Automatically with every "git push"). This was chosen for this project.

## Credits
### Code
* I learned how to use word art from [Patthoeges](https://github.com/patthoege/hangmangame-pp3-python) gihub. 
* I used wordart from [Fancy text pro](https://www.fancytextpro.com/BigTextGenerator?fbclid=IwAR0TsTKLRY91w8ggGxdgfZp6Cu-R4HP2SjAemqdaCRtT86b_tIwp-WeF3u8).
* I learned about how to clear the terminal window from Stack Overflows [thread](https://stackoverflow.com/questions/2084508/clear-terminal-in-python).

### Acknowledgements

