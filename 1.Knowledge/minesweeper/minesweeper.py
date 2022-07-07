""" The Minesweeper AI that plays the game using advanced logics """

import itertools
import random


class Minesweeper():
    """
    Minesweeper game representation
    """

    def __init__(self, height=8, width=8, mines=8):

        # Set initial width, height, and number of mines
        self.height = height
        self.width = width
        self.mines = set()

        # Initialize an empty field with no mines
        self.board = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                row.append(False)
            self.board.append(row)

        # Add mines randomly
        while len(self.mines) != mines:
            i = random.randrange(height)
            j = random.randrange(width)
            if not self.board[i][j]:
                self.mines.add((i, j))
                self.board[i][j] = True

        # At first, player has found no mines
        self.mines_found = set()

    def print(self):
        """
        Prints a text-based representation
        of where mines are located.
        """
        for i in range(self.height):
            print("--" * self.width + "-")
            for j in range(self.width):
                if self.board[i][j]:
                    print("|X", end="")
                else:
                    print("| ", end="")
            print("|")
        print("--" * self.width + "-")

    def is_mine(self, cell):
        """ Determine if a cell is mine """
        i, j = cell
        return self.board[i][j]

    def nearby_mines(self, cell):
        """
        Returns the number of mines that are
        within one row and column of a given cell,
        not including the cell itself.
        """

        # Keep count of nearby mines
        count = 0

        # Loop over all cells within one row and column
        for i in range(cell[0] - 1, cell[0] + 2):
            for j in range(cell[1] - 1, cell[1] + 2):

                # Ignore the cell itself
                if (i, j) == cell:
                    continue

                # Update count if cell in bounds and is mine
                if 0 <= i < self.height and 0 <= j < self.width:
                    if self.board[i][j]:
                        count += 1

        return count

    def won(self):
        """
        Checks if all mines have been flagged.
        """
        return self.mines_found == self.mines


class Sentence():
    """
    Logical statement about a Minesweeper game
    A sentence consists of a set of board cells,
    and a count of the number of those cells which are mines.
    """

    def __init__(self, cells, count):
        self.cells = set(cells)
        self.count = count

    def __eq__(self, other):
        return self.cells == other.cells and self.count == other.count

    def __str__(self):
        return f"{self.cells} = {self.count}"

    def known_mines(self):
        """
        Returns the set of all cells in self.cells known to be mines.
        """
        # When the number of mines is the same as the number of cells,
        # then all the cells are mines
        if len(self.cells) == self.count:
            return self.cells

        return set()

    def known_safes(self):
        """
        Returns the set of all cells in self.cells known to be safe.
        """
        # When there is no mines, then all cells are safe
        if self.count == 0:
            return self.cells

        return set()

    def mark_mine(self, cell):
        """
        Updates internal knowledge representation given the fact that
        a cell is known to be a mine.
        """
        # If cell is not in cells, then nothing needs to be done
        if cell in self.cells:
            # Remove the cell from cells and decrease the number of mines by 1
            self.cells.remove(cell)
            self.count = self.count - 1

    def mark_safe(self, cell):
        """
        Updates internal knowledge representation given the fact that
        a cell is known to be safe.
        """
        # If cell is not in cells, then nothing needs to be done
        if cell in self.cells:
            # Remove the cell from cells
            self.cells.remove(cell)

    def inference(self, other):
        """
        Using the method of subset to inference a new sentence from
        the two existing sentences
        """
        # If this sentence is a subset of other sentence
        if self.cells.issubset(other.cells):
            return Sentence(other.cells - self.cells, other.count - self.count)
        # Or if other sentence is a subset of this sentence
        elif other.cells.issubset(self.cells):
            return Sentence(self.cells - other.cells, self.count - other.count)
        # If no inference can be made, then None
        else:
            return None

class MinesweeperAI():
    """
    Minesweeper game player
    """

    def __init__(self, height=8, width=8):

        # Set initial height and width
        self.height = height
        self.width = width

        # Keep track of which cells have been clicked on
        self.moves_made = set()

        # Keep track of cells known to be safe or mines
        self.mines = set()
        self.safes = set()

        # List of sentences about the game known to be true
        self.knowledge = []

    def mark_mine(self, cell):
        """
        Marks a cell as a mine, and updates all knowledge
        to mark that cell as a mine as well.
        """
        self.mines.add(cell)
        for sentence in self.knowledge:
            sentence.mark_mine(cell)

    def mark_safe(self, cell):
        """,
        Marks a cell as safe, and updates all knowledge
        to mark that cell as safe as well.
        """
        self.safes.add(cell)
        for sentence in self.knowledge:
            sentence.mark_safe(cell)

    def add_knowledge(self, cell, count):
        """
        Called when the Minesweeper board tells us, for a given
        safe cell, how many neighboring cells have mines in them.

        This function should:
            1) mark the cell as a move that has been made
            2) mark the cell as safe
            3) add a new sentence to the AI's knowledge base
               based on the value of `cell` and `count`
            4) mark any additional cells as safe or as mines
               if it can be concluded based on the AI's knowledge base
            5) add any new sentences to the AI's knowledge base
               if they can be inferred from existing knowledge
        """
        # 1) mark the cell as a move that has been made
        self.moves_made.add(cell)

        # 2) mark the cell as safe
        self.mark_safe(cell)

        # 3) add a new sentence to the AI's knowledge base based on the value of `cell` and `count`
        cells = set()
        # Adding neighbor cells into cells set
        for row in range(cell[0] - 1, cell[0] + 2):
            for col in range(cell[1] - 1, cell[1] + 2):

                # Ignore the cell itself
                if (row, col) == cell:
                    continue

                # Add cell into cells set if it is valid (within the board)
                if (0 <= row < self.height) and (0 <= col < self.width):
                    cells.add((row, col))

        # Create new sentence
        new_sentence = Sentence(cells, count)

        # Clean up new_sentence using known mines and safes
        for safe_cell in self.safes:
            new_sentence.mark_safe(safe_cell)

        for mine_cell in self.mines:
            new_sentence.mark_mine(mine_cell)

        # Add result into KB
        self.knowledge.append(new_sentence)

        # 4) mark any additional cells as safe or as mines
        # if it can be concluded based on the AI's knowledge base
        add_safes = set()
        add_mines = set()

        for sentence in self.knowledge:
            # Remove sentences that are canceled out
            if len(sentence.cells) == 0:
                self.knowledge.remove(sentence)
                continue

            # Get known safes and known mines from a sentence
            safe_cells = sentence.known_safes()
            mine_cells = sentence.known_mines()

            # Get new safes
            for cell in safe_cells:
                add_safes.add(cell)

            # Get new mines
            for cell in mine_cells:
                add_mines.add(cell)

        # Mark new cells and mines to KB if any
        for cell in add_safes:
            self.mark_safe(cell)

        for cell in add_mines:
            self.mark_mine(cell)

        # 5) add any new sentences to the AI's knowledge base
        # if they can be inferred from existing knowledge
        new_sentences = []
        # Check each two sentences in the KB whether we can use inference
        for sentence1, sentence2 in itertools.combinations(self.knowledge, 2):
            inf_sentence = sentence1.inference(sentence2)
            if inf_sentence is not None and inf_sentence not in self.knowledge:
                new_sentences.append(inf_sentence)

        self.knowledge = self.knowledge + new_sentences

    def make_safe_move(self):
        """
        Returns a safe cell to choose on the Minesweeper board.
        The move must be known to be safe, and not already a move
        that has been made.

        This function may use the knowledge in self.mines, self.safes
        and self.moves_made, but should not modify any of those values.
        """
        # Available moves are those safes but not moves that are already made
        available_moves = self.safes.difference(self.moves_made)

        # If there are available moves, randomly choose one.
        # Otherwise return None
        if len(available_moves) != 0:
            return random.choice(tuple(available_moves))

        return None


    def make_random_move(self):
        """
        Returns a move to make on the Minesweeper board.
        Should choose randomly among cells that:
            1) have not already been chosen, and
            2) are not known to be mines
        """
        available_moves = set()
        # Available moves are those not mines and not moves that are already made
        for row in range(self.height):
            for col in range(self.width):
                cell = (row, col)
                if (cell not in self.mines) and (cell not in self.moves_made):
                    available_moves.add(cell)

        # If there are available moves, randomly choose one.
        # Otherwise return None
        if len(available_moves) != 0:
            return random.choice(tuple(available_moves))

        return None
