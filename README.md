# 🔴 Connect Four 🟡

This is a fully functioning console running connect four implementation written in Python.

## Rules
  - The game contains the standard connect four rules, with a 6 row by 7 column game board.
  - Players take turns inserting their pieces into columns.
  - The game ends on two accounts:
    1. Either player gets 4-in-a-row in any direction\
       a) Vertical\
       b) Horizontal\
       c) Positively Sloped Diagonal\
       d) Negatively Sloped Diagonal
    3. The board completely fills up with pieces

## Game Modes
### Randomized Mode:
  - Moves for each player are made at random.
### User Inputted Mode: 
  - User's manually input the column in which they would like to play.

## Game Play
  - The user is first prompted to select a game mode (Randomized or User Inputted)
  - The game then begins, the board is printed to the console and the user is prompted for their move selection.
    - If the game is in **Randomized Mode**, any button click by the user after the prompt will trigger a randomly generated column number selection.
    - If the game is in **User Inputted Mode**, after the prompt, the column selection will be a user inputted valid column number.
  - Validation checks are in place for both the randomly generated column number and the user inputted column number.
    - If the input is not valid, the user will be prompted until a valid selection is made. 
  - After a valid selection is made, the board is printed with the latest move inserted.
  - After each move, a check is made to see if there is a winner or if the board is full.
    - If either case arises, the game will terminate and a message will be printed to the screen to describe why the game ended. 
  - The game will keep switching between Player 1 and Player 2 move prompts and board prints until the game is over.
