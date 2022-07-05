# Parser

An AI that recognizes sentence structures/syntax/grammar

## Background

A common task in natural language processing is parsing, the process of determining the structure of a sentence. This is useful for a number of reasons: knowing the structure of a sentence can help a computer to better understand the meaning of the sentence, and it can also help the computer extract information out of a sentence. In particular, it’s often useful to extract noun phrases out of a sentence to get an understanding for what the sentence is about

## Files

In _sentences_ directory, there are 10 different pre-defined sentences as txt files, each with a different syntax. One is welcome to add more sentences as txt files to test the functionality of the AI. In the _parser.py_ file, the AI use the [nltk (natural language tool kit)](https://www.nltk.org/) and some customized context free grammars to recognize the sentence structures. Feel free to add more words to the non-terminal variable to expand the functionality of the AI

## How to Use

Make sure nltk is installed, if not, use the following command

`pip install nltk`

In the parser directory, run the command

`python parser.py sentences/.txt`

Where the _sentences/.txt_ is an optional argument, if not provided, the AI will take user input

## Example Output

```python
        S
   _____|___
  NP        VP
  |         |
  N         V
  |         |
holmes     sat
```
