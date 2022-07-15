## Specification

Add knowledge to knowledge bases `knowledge0`, `knowledge1`, `knowledge2`, and `knowledge3` to solve the following puzzles.

- Puzzle 0 is the puzzle from the Background. It contains a single character, A.
  - A says “I am both a knight and a knave.”
- Puzzle 1 has two characters: A and B.
  - A says “We are both knaves.”
  - B says nothing.
- Puzzle 2 has two characters: A and B.
  - A says “We are the same kind.”
  - B says “We are of different kinds.”
- Puzzle 3 has three characters: A, B, and C.
  - A says either “I am a knight.” or “I am a knave.”, but you don’t know which.
  - B says “A said ‘I am a knave.’”
  - B then says “C is a knave.”
  - C says “A is a knight.”

In each of the above puzzles, each character is either a knight or a knave. Every sentence spoken by a knight is true, and every sentence spoken by a knave is false

You should only tell the AI what the characters said with propositional logics defined in `logic.py`, without telling the AI what you think. You can use the `model_check` function in `logic.py` to check what the entailments are

Once you’ve completed the knowledge base for a problem, you should be able to run `python puzzle.py` to see the solution to the puzzle

## Hints

- For each knowledge base, you’ll likely want to encode two different types of information: (1) information about the structure of the problem itself (i.e., information given in the definition of a Knight and Knave puzzle), and (2) information about what the characters actually said
- Consider what it means if a sentence is spoken by a character. Under what conditions is that sentence true? Under what conditions is that sentence false? How can you express that as a logical sentence?
- There are multiple possible knowledge bases for each puzzle that will compute the correct result. You should attempt to choose a knowledge base that offers the most direct translation of the information in the puzzle, rather than performing logical reasoning on your own. You should also consider what the most concise representation of the information in the puzzle would be
  - For instance, for Puzzle 0, setting `knowledge0 = AKnave` would result in correct output, since through our own reasoning we know A must be a knave. But doing so would be against the spirit of this problem: the goal is to have your AI do the reasoning for you
- You should not need to (nor should you) modify `logic.py` at all to complete this problem
