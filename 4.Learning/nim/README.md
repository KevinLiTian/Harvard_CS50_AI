# Nim

An AI that uses reinforcement learning to learn from experience playing Nim with itself

## Background

The game of [Nim](https://en.wikipedia.org/wiki/Nim) is a mathematical game of strategy. Players take turns removing objects from piles, there are several piles of objects at the beginning of the game. Each move made by the player should only take objects from one pile, the amount of objects can vary between 1 and all of the objects in that pile. The win condition to to let the opponent player take the last objects

Reinforcement learning is quite useful in these kinds of mathematical strategy games or game theories because the AI is able to learn by experience of which state of the game is favored and what action is the best under certain states

## Files

The `nim.py` file contains the definition of the Nim game itself and a NimAI that trains itself by playing the game over and over again. The `play.py` file starts the training process and the game by calling functions in `nim.py`

## How to Use

Check in the `play.py` file, the train function takes in an integer input as how many games will the NimAI train by playing with itself. Use input of 0 to play against an untrained AI and use input of 10000 to play against a well trained one. After configuring the number of training games, run this command in the `nim` directory:

`python play.py`

As a human player, one should input which pile and what amount to remove according to the prompts

## Example Output

```shell
$ python play.py
Playing training game 1
Playing training game 2
Playing training game 3
...
Playing training game 9999
Playing training game 10000
Done training

Piles:
Pile 0: 1
Pile 1: 3
Pile 2: 5
Pile 3: 7

AI's Turn
AI chose to take 1 from pile 2.
```
