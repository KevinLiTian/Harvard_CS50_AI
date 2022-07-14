# Knights

An AI solving [Knights and Knaves](https://en.wikipedia.org/wiki/Knights_and_Knaves) logic puzzles using propositional logics

## Background

In 1978, logician Raymond Smullyan published “What is the name of this book?”, a book of logical puzzles. Among the puzzles in the book were a class of puzzles that Smullyan called “Knights and Knaves” puzzles

In a Knights and Knaves puzzle, the following information is given: Each character is either a knight or a knave. A knight will always tell the truth: if knight states a sentence, then that sentence is true. Conversely, a knave will always lie: if a knave states a sentence, then that sentence is false

The objective of the puzzle is, given a set of sentences spoken by each of the characters, determine, for each character, whether that character is a knight or a knave

For example, consider a simple puzzle with just a single character named A. A says “I am both a knight and a knave”

Logically, we might reason that if A were a knight, then that sentence would have to be true. But we know that the sentence cannot possibly be true, because A cannot be both a knight and a knave – we know that each character is either a knight or a knave, but not both. So, we could conclude, A must be a knave

That puzzle was on the simpler side. With more characters and more sentences, the puzzles can get trickier! Your task in this problem is to determine how to represent these puzzles using propositional logic, such that an AI running a model-checking algorithm could solve these puzzles for us

## Files

There are two files, `logic.py` and `puzzle.py`. `Logic.py` has all the helper functions for us to translate human logic into AI knowledge, such as AND, OR, NOT, etc. Furthermore there are also functions to give entailments based on existing knowledge base such as the model check function. `Puzzle.py` is the actual use of all the helper functions in `logic.py`. There are four scenarios, each have its own KB. We have to determine whether each character in each scenario is a knight or a knave based on the corresponding KB. Some are easy for human to "logic" it out and some are a bit tricky, that's why AI will be better at these kinds of job since they will never make mistakes, they "algorithm" it out (otherwise blame on the programmer LOL)

## How to Use

Go into the `puzzle.py` and check the four scenarios, try to reason it out which character is a knight or a knave. Then in the `knights` directory, run the command below to see if you got it right!

`python puzzle.py`

## Example Output

```shell
Puzzle 0
    A is a Knave
Puzzle 1
    A is a Knave
    B is a Knight
Puzzle 2
    A is a Knave
    B is a Knight
Puzzle 3
    A is a Knight
    B is a Knave
    C is a Knight
```
