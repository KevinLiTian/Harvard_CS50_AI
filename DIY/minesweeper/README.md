## Specification

Complete the implementations of the `Sentence` class and the `MinesweeperAI` class in `minesweeper.py`.

In the `Sentence` class, complete the implementations of `known_mines`, `known_safes`, `mark_mine`, and `mark_safe`.

- The `known_mines` function should return a set of all of the cells in `self.cells` that are known to be mines.
- The `known_safes` function should return a set of all the cells in `self.cells` that are known to be safe.
- The `mark_mine` function should first check to see if `cell` is one of the cells included in the sentence.
  - If `cell` is in the sentence, the function should update the sentence so that `cell` is no longer in the sentence, but still represents a logically correct sentence given that `cell` is known to be a mine.
  - If `cell` is not in the sentence, then no action is necessary.
- The `mark_safe` function should first check to see if `cell` is one of the cells included in the sentence.
  - If `cell` is in the sentence, the function should update the sentence so that `cell` is no longer in the sentence, but still represents a logically correct sentence given that `cell` is known to be safe.
  - If `cell` is not in the sentence, then no action is necessary.

In the `MinesweeperAI` class, complete the implementations of `add_knowledge`, `make_safe_move`, and `make_random_move`.

- `add_knowledge` should accept a `cell` (represented as a tuple `(i, j)`) and its corresponding `count`, and update `self.mines`, `self.safes`, `self.moves_made`, and `self.knowledge` with any new information that the AI can infer, given that `cell` is known to be a safe cell with `count` mines neighboring it.
  - The function should mark the `cell` as one of the moves made in the game.
  - The function should mark the `cell` as a safe cell, updating any sentences that contain the `cell` as well.
  - The function should add a new sentence to the AI’s knowledge base, based on the value of `cell` and `count`, to indicate that `count` of the `cell`’s neighbors are mines. Be sure to only include cells whose state is still undetermined in the sentence.
  - If, based on any of the sentences in `self.knowledge`, new cells can be marked as safe or as mines, then the function should do so.
  - If, based on any of the sentences in `self.knowledge`, new sentences can be inferred (using the subset method described in the Background), then those sentences should be added to the knowledge base as well.
- `make_safe_move` should return a move `(i, j)` that is known to be safe.
  - The move returned must be known to be safe, and not a move already made.
  - If no safe move can be guaranteed, the function should return `None`.
  - The function should not modify `self.moves_made`, `self.mines`, `self.safes`, or `self.knowledge`.
- `make_random_move` should return a random move `(i, j)`.
  - This function will be called if a safe move is not possible: if the AI doesn’t know where to move, it will choose to move randomly instead.
  - The move must not be a move that has already been made.
  - The move must not be a move that is known to be a mine.
  - If no such moves are possible, the function should return `None`.

## Hints

- Be sure you’ve thoroughly read the Background section to understand how knowledge is represented in this AI and how the AI can make inferences
- If feeling less comfortable with object-oriented programming, you may find [Python’s documentation on classes](https://docs.python.org/3/tutorial/classes.html) helpful
- You can find some common `set` operations in [Python’s documentation on sets](https://docs.python.org/3/library/stdtypes.html#set)
- When implementing `known_mines` and `known_safes` in the `Sentence` class, consider: under what circumstances do you know for sure that a sentence’s cells are safe? Under what circumstances do you know for sure that a sentence’s cells are mines?
- `add_knowledge` does quite a lot of work, and will likely be the longest function you write for this project by far. It will likely be helpful to implement this function’s behavior one step at a time
- You’re welcome to add new methods to any of the classes if you would like, but you should not modify any of the existing functions’ definitions or arguments
- When you run your AI (as by clicking “AI Move”), note that it will not always win! There will be some cases where the AI must guess, because it lacks sufficient information to make a safe move. This is to be expected. `runner.py` will print whether the AI is making a move it believes to be safe or whether it is making a random move
- Be careful not to modify a set while iterating over it. Doing so may result in errors!

There is a specific type of inference regarding minesweeper game. Take a look at the following example

<img src="https://user-images.githubusercontent.com/99038613/179137274-3878c0fd-7fba-4551-a617-f1f5679a2972.jpg" width=60%>

We know from the top-middle cell that mine in `{A, B, C} = 1`, and from the bottom-middle cell that mine in `{A, B, C, D, E} = 2`; from these two sentences, we are able to infer that `{D, E} = 1`. How to represent the infer process? We can infer by `{A, B, C, D, E} - {A, B, C} = 2 - 1`, which can be generalized to `{Set 2} - {Set 1} = Mine 2 - Mine 1`

Every type of problem has its own inference method, and we as programmers are to find these patterns and engineer them with programming languages. This is knowledge engineering
