## Specification

Complete the implementation of `preprocess` and `np_chunk`, and complete the context-free grammar rules defined in `NONTERMINALS`.

- The `preprocess` function should accept a `sentence` as input and return a lowercased list of its words.
  - You may assume that `sentence` will be a string.
  - You should use `nltk`’s `word_tokenize` function to perform tokenization.
  - Your function should return a list of words, where each word is a lowercased string.
  - Any word that doesn’t contain at least one alphabetic character (e.g. `.` or `28`) should be excluded from the returned list.
- The `NONTERMINALS` global variable should be replaced with a set of context-free grammar rules that, when combined with the rules in `TERMINALS`, allow the parsing of all sentences in the `sentences/` directory.
  - Each rules must be on its own line. Each rule must include the `->` characters to denote which symbol is being replaced, and may optionally include `|` symbols if there are multiple ways to rewrite a symbol.
  - You do not need to keep the existing rule `S -> N V` in your solution, but your first rule must begin with `S ->` since `S` (representing a sentence) is the starting symbol.
  - You may add as many nonterminal symbols as you would like.
  - Use the nonterminal symbol `NP` to represent a “noun phrase”, such as the subject of a sentence.
- The `np_chunk` function should accept a `tree` representing the syntax of a sentence, and return a list of all of the noun phrase chunks in that sentence.
  - For this problem, a “noun phrase chunk” is defined as a noun phrase that doesn’t contain other noun phrases within it. Put more formally, a noun phrase chunk is a subtree of the original tree whose label is `NP` and that does not itself contain other noun phrases as subtrees.
    - For example, if `"the home"` is a noun phrase chunk, then `"the armchair in the home"` is not a noun phrase chunk, because the latter contains the former as a subtree.
  - You may assume that the input will be a `nltk.tree` object whose label is `S` (that is to say, the input will be a tree representing a sentence).
  - Your function should return a list of `nltk.tree` objects, where each element has the label `NP`.
  - You will likely find the documentation for `nltk.tree` helpful for identifying how to manipulate a `nltk.tree` object.

You should not modify anything else in `parser.py` other than the functions the specification calls for you to implement, though you may write additional functions and/or import other Python standard library modules. You will need to modify the definition of `NONTERMINALS`, but you should not modify the definition of `TERMINALS`.
