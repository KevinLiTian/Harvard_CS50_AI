# Crossword

An AI that solves crossword puzzles using given structure and words files

## Background

How might you go about solving a crossword puzzle? Given the structure of a crossword puzzle (i.e., which squares of the grid are meant to be filled in with a letter), and a list of words to use, the problem becomes one of choosing which words should go in each vertical or horizontal sequence of squares. We can model this sort of problem as a constraint satisfaction problem. Each sequence of squares is one variable, for which we need to decide on its value (which word in the domain of possible words will fill in that sequence)

## Files

The `data` directory contains the structure and words files for the crossword puzzles, one is welcome to add more data files to this directory to test the functionality or just for fun. The `crossword.py` file has two classes, `variable` and `crossword` to help solving the crossword puzzles. The main solving functions are in the `generate.py` file. In this file, main function takes arguments form command line and decide which structure and words files to use and call the solve function which uses other helper functions in the file

## How to Use

In the `crossword` directory, run the command

`python generate.py data/structure.txt data/words.txt output.png`

Where `structure` and `words` are txt files in the `data` directory, one can use the existing 0-2 files or create their own files. The program will also save a png of the solved crossword puzzle

## Example Output

```shell
$ python generate.py data/structure1.txt data/words1.txt output.png
██████████████
███████M████R█
█INTELLIGENCE█
█N█████N████S█
█F██LOGIC███O█
█E█████M████L█
█R███SEARCH█V█
███████X████E█
██████████████
```

<p align="center">
<img src="https://user-images.githubusercontent.com/99038613/176724983-d23252a0-73cc-41b1-981e-0a2575e66327.jpg" width="60%" height="60%">
</p>
