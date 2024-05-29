# Tic Tac Toe

How to Play
The game board is a 3x3 grid.
Players take turns to place their markers (X and O) on the grid.
The first player to get three of their markers in a row (horizontally, vertically, or diagonally) wins.
If the board is full and no player has won, the game ends in a draw.


## User Stories 
*User 1: As a new player I want to be able to start the game and receive a brief instruction on how to play, so that I can quickly understand the rules and get started.

*User 2: As an active player I want to see the current game board after each move, so I can keep track of the game's progress and plan my next moves.

*User 3: As a player I want to be notified when someone wins the game or if it ends in a draw, so I know when the game is over and who the winner is.


*User 4: As an erroneous user I want to receive clear error messages if I make an invalid move, so I can understand what went wrong and try again.


User 5: As a serious player I want to be able to play multiple rounds without having to manually restart the program, so I can continue playing without interruption.


### Site purpose


### Project Goals


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

