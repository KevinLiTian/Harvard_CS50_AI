# Minesweeper

An AI playing [Minesweeper](<https://en.wikipedia.org/wiki/Minesweeper_(video_game)>) base on some advanced logics

## Background

Minesweeper is a puzzle game that consists of a grid of cells, where some of the cells contain hidden “mines.” Clicking on a cell that contains a mine detonates the mine, and causes the user to lose the game. Clicking on a “safe” cell (i.e., a cell that does not contain a mine) reveals a number that indicates how many neighboring cells – where a neighbor is a cell that is one square to the left, right, up, down, or diagonal from the given cell – contain a mine

## Files

The runner.py is used to initiate an instance of pygame and uses logics provided in the minesweeper.py to play moves. In minesweeper.py, there are three classes, the _Minesweeper_ class which is to represent the game itself and some game rule related functionalities such as randomly place some mines in the board, check how many mines are neighbouring to a certain cell and check whether the player has won or not. The _Sentence_ class provides some logics to the AI, such as which cells are known to be mines or safe cells given some conditions. The _MinesweeperAI_ class is the AI which perceives information about the board, store them into the KB as sentences and use the KB to "algorithm" out which cells are safe to play, which cells are mines for certain and which cells are not certain based on current KB

## How to Play

Make sure _pygame_ is installed on your device. Run runner.py, a pygame window will pop up like the screenshot below

You can either play it yourself or asking the AI to play a move if you are not sure how to play. By clicking the _AI move_ button, the AI will play a move, if there are safe moves available on the board, the AI will play one of them, if no safe moves are available, the AI will randomly choose a cell that is known not to be a mine cell
