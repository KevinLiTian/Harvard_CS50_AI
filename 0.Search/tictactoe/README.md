# Tic-Tac-Toe

An AI that uses the Minimax Algorithm to play the Tic-Tac-Toe game optimally

## Files

The `runner.py` is used to initiate the pygame instance and it uses functions written in `tictactoe.py` as the logic for the AI. In `tictactoe.py`, the AI determines board state, possible actions, win conditions and using the Minimax Algorithm to make the optimal move at the current state of the game

## How to Play

Make sure `pygame` is installed on your device, if not, use the command

`pip install pygame`

In the `tictactoe` directory, run the command

`python runner.py`

A pygame window will pop up like the screenshot below

<p align="center">
<img src="https://user-images.githubusercontent.com/99038613/174504591-79a6821a-98ab-4195-b9a5-cd654ef16fed.png" width="60%" height="60%">
</p>

Choose either to play as "X" or "O" role, the AI will take the remaining role. You should never be able to beat the AI since it's playing optimally! (Or maybe I'm a bad programmer)
