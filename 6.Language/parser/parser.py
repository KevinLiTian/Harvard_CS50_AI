""" An AI that recognizes sentence structures/syntax/grammar """

import sys

import nltk

# Terminal symbols, where each is to be definitely defined by a word
# Add more words to have better functionality
TERMINALS = """
Adj -> "country" | "dreadful" | "enigmatical" | "little" | "moist" | "red"
Adv -> "down" | "here" | "never"
Conj -> "and" | "until"
Det -> "a" | "an" | "his" | "my" | "the"
N -> "armchair" | "companion" | "day" | "door" | "hand" | "he" | "himself"
N -> "holmes" | "home" | "i" | "mess" | "paint" | "palm" | "pipe" | "she"
N -> "smile" | "thursday" | "walk" | "we" | "word"
P -> "at" | "before" | "in" | "of" | "on" | "to"
V -> "arrived" | "came" | "chuckled" | "had" | "lit" | "said" | "sat"
V -> "smiled" | "tell" | "were"
"""

# Non-Terminal symbols, where each can be expand to more non-terminal or terminal symbols
NONTERMINALS = """
S -> NP VP | VP NP | S Conj S
NP -> N | Det N | NP PP | Det AP N
VP -> V | V NP | V PP | Adv VP | VP Adv
AP -> Adj | Adj AP
PP -> P NP
"""

# Create grammar from pre-defined symbols
grammar = nltk.CFG.fromstring(NONTERMINALS + TERMINALS)
parser = nltk.ChartParser(grammar)


def main():
    """ Main Function
    Takes argument from command line, decide whether to use a pre-defined
    txt file as input or take user input
    Parse the sentence and recognize the structure
    Print out the structure and np_chunks
    """
    # If filename specified, read sentence from file
    if len(sys.argv) == 2:
        with open(sys.argv[1], encoding='utf-8') as file:
            sentence = file.read()

    # Otherwise, get sentence as input
    else:
        sentence = input("Sentence: ")

    # Convert input into list of words
    sentence = preprocess(sentence)

    # Attempt to parse sentence
    try:
        trees = list(parser.parse(sentence))
    except ValueError as error:
        print(error)
        return
    if not trees:
        print("Could not parse sentence.")
        return

    # Print each tree with noun phrase chunks
    for tree in trees:
        tree.pretty_print()

        print("Noun Phrase Chunks")
        for np_c in np_chunk(tree):
            print(" ".join(np_c.flatten()))


def preprocess(sentence):
    """
    Convert `sentence` to a list of its words.
    Pre-process sentence by converting all characters to lowercase
    and removing any word that does not contain at least one alphabetic
    character.
    """
    # Lowercase the sentence
    sentence = sentence.lower()

    # Tokenize each element in the sentence
    word_list = nltk.word_tokenize(sentence)

    # Remove all words that does not contain at least one alphabetic char
    for word in word_list:
        if not any(char.isalpha() for char in word):
            word_list.remove(word)

    return word_list


def np_chunk(tree):
    """
    Return a list of all noun phrase chunks in the sentence tree.
    A noun phrase chunk is defined as any subtree of the sentence
    whose label is "NP" that does not itself contain any other
    noun phrases as subtrees.
    """
    np_chunks = []

    # For each subtree, check if its label is "NP" and no child is np
    for subtree in tree.subtrees():
        if subtree.label() == "NP" and not any(child.label() == "NP" for child in subtree):
            np_chunks.append(subtree)

    return np_chunks


if __name__ == "__main__":
    main()
