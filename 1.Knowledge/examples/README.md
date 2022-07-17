# Knowledge Examples

The `logic.py` file contains helpful propositional logic representations using Python such as logic symbols (assertion of reality), logical connectives (and, or, not...), and functions to check the logical representation and entailments (`formula`, `model_check`). And the remaining four files contain the utilization of propositional logics

## Harry

`harry.py contains a simple logic stating that

- If it's not raining, then Harry visited Hagrid
- Harry either visited Hagrid or visited Dumbledore
- Harry cannot visit both Hagrid and Dumbledore
- Harry visited Dumbledore

And by these statements, or assertions of reality, we query that is it raining or not? It should be obvious for us that it is raining, but check out how we can use Python implmentation of propositional logic to let our AI deduce that it is raining

In `examples` directory, run `python harry.py`

## Clue

[Clue](https://en.wikipedia.org/wiki/Cluedo) is a murder mystery game that players should use logic to reason who's the murderer out of three characters, what's the weapon out of three weapons is used for the murder, and in which room out of three rooms did the murder take place? Each round a clue will be given to rule out a possibility and the players should deduce based on the clues given

Now check in `clue.py` to see how we implemented this logic in Python. Notice that there are several sections of the code, one is the `symbols`, one is the rule of the game, one is `initial clues` and the other two are `first clues` and `second clues` which are commented out to represent that we have not yet get those clues at the beginning of the game

In `examples` directory, run `python clue.py`

The initial output should be all MAYBE, because from the initial clues given, we cannot be certain of the result. Then uncomment the first clues and run the program again, this time we should be able make some certain inferences, but some are still MAYBE. Finally uncomment the second clues, run the program yet again, and everything should be clear right now

## Mastermind

[Mastermind](https://www.wikihow.com/Play-Mastermind) is a game based on logic where the player will have four color to place on four grids, and the feedback will be in the form of "How many colors are placed in the wrong grid". And the player should adjust the placing of the colors based on the feedback and some logic reasoning to finally place every color in the correct grid

Now take a look at `mastermind.py` where we encoded the rule of the mastermind game with Python. The correct position is specified in the `colors` list variable, then we encode the rules of the game and also some incorrect circumstances for the AI to deduce upon

In `examples` directory, run `python mastermind.py`

## Puzzle

Check out `puzzle.py`, where the puzzle is to assign each of the four person to a different house. Four persons are defined in `people` list variable and the four houses are defined in `houses` list variable. We encode in Python that each person must have a house and a house can only be assigned to one person. Then we provide some information for our AI to deduce upon

In `examples` directory, run `python puzzles.py`
