""" An AI that solves crossword puzzles given structure and words """

import sys

from PIL import Image, ImageDraw, ImageFont

from crossword import Variable, Crossword


class CrosswordCreator():
    """ Crossword puzzle AI that takes in a crossword problem """
    def __init__(self, crossword):
        """
        Create new CSP crossword generate.
        """
        self.crossword = crossword
        self.domains = {
            var: self.crossword.words.copy()
            for var in self.crossword.variables
        }

    def letter_grid(self, assignment):
        """
        Return 2D array representing a given assignment.
        """
        letters = [
            [None for _ in range(self.crossword.width)]
            for _ in range(self.crossword.height)
        ]
        for variable, word in assignment.items():
            direction = variable.direction
            for k in range(len(word)):
                i = variable.i + (k if direction == Variable.DOWN else 0)
                j = variable.j + (k if direction == Variable.ACROSS else 0)
                letters[i][j] = word[k]
        return letters

    def print(self, assignment):
        """
        Print crossword assignment to the terminal.
        """
        letters = self.letter_grid(assignment)
        for i in range(self.crossword.height):
            for j in range(self.crossword.width):
                if self.crossword.structure[i][j]:
                    print(letters[i][j] or " ", end="")
                else:
                    print("█", end="")
            print()

    def save(self, assignment, filename):
        """
        Save crossword assignment to an image file.
        """
        cell_size = 100
        cell_border = 2
        interior_size = cell_size - 2 * cell_border
        letters = self.letter_grid(assignment)

        # Create a blank canvas
        img = Image.new(
            "RGBA",
            (self.crossword.width * cell_size,
             self.crossword.height * cell_size),
            "black"
        )
        font = ImageFont.truetype("assets/fonts/OpenSans-Regular.ttf", 80)
        draw = ImageDraw.Draw(img)

        for i in range(self.crossword.height):
            for j in range(self.crossword.width):

                rect = [
                    (j * cell_size + cell_border,
                     i * cell_size + cell_border),
                    ((j + 1) * cell_size - cell_border,
                     (i + 1) * cell_size - cell_border)
                ]
                if self.crossword.structure[i][j]:
                    draw.rectangle(rect, fill="white")
                    if letters[i][j]:
                        width, height = draw.textsize(letters[i][j], font=font)
                        draw.text(
                            (rect[0][0] + ((interior_size - width) / 2),
                             rect[0][1] + ((interior_size - height) / 2) - 10),
                            letters[i][j], fill="black", font=font
                        )

        img.save(filename)

    def solve(self):
        """
        Enforce node and arc consistency, and then solve the CSP.
        """
        self.enforce_node_consistency()
        self.ac3()
        return self.backtrack(dict())

    def enforce_node_consistency(self):
        """
        Update `self.domains` such that each variable is node-consistent.
        (Remove any values that are inconsistent with a variable's unary
         constraints; in this case, the length of the word.)
        """
        # Since set cannot be modified while iterating, store the word
        # that should be removed in corresponding var
        remove_words = {}

        # Iterate to check which words do not satisfy node consistency
        for var, word_list in self.domains.items():
            for word in word_list:
                # If not store in remove_words dict
                if len(word) != var.length:
                    if var not in remove_words:
                        remove_words[var] = []
                    remove_words[var].append(word)

        # Remove words from domain
        for var, word_list in remove_words.items():
            for word in word_list:
                self.domains[var].remove(word)

    def revise(self, var1, var2):
        """
        Make variable `x` arc consistent with variable `y`.
        To do so, remove values from `self.domains[x]` for which there is no
        possible corresponding value for `y` in `self.domains[y]`.

        Return True if a revision was made to the domain of `x`; return
        False if no revision was made.
        """
        # Check overlap
        overlap = self.crossword.overlaps[var1, var2]

        # If no overlap, nothing needs to be changed
        if overlap is None:
            return False

        # Store indices of overlap
        index_x = overlap[0]
        index_y = overlap[1]

        # Otherwise for each word in x domain, check if any word in y domain is possible
        # Same reason, we cannot modify set during iterating, so store first
        remove_words = []
        for word in self.domains[var1]:
            possible = False
            # If any word in y is possible, then the word in x is OK
            for possible_word in self.domains[var2]:
                if word[index_x] == possible_word[index_y]:
                    possible = True

            # If no word in y satisfies the word in x, remove word in x
            if not possible:
                remove_words.append(word)

        # If no words in x needs to be removed, return false since we won't modify anything
        if len(remove_words) == 0:
            return False

        # If there is, remove them from domain of x
        for word in remove_words:
            self.domains[var1].remove(word)

        return True

    def ac3(self, arcs=None):
        """
        Update `self.domains` such that each variable is arc consistent.
        If `arcs` is None, begin with initial list of all arcs in the problem.
        Otherwise, use `arcs` as the initial list of arcs to make consistent.

        Return True if arc consistency is enforced and no domains are empty;
        return False if one or more domains end up empty.
        """
        # If arcs is None, we begin by using all the arcs in this CSP
        if arcs is None:
            arcs = []
            for var1 in self.domains:
                for var2 in self.crossword.neighbors(var1):
                    arcs.append((var1, var2))

        # Dequeue until empty
        while len(arcs) != 0:
            (var1, var2) = arcs.pop(0)
            # If revised, then check if there's something left in var1's domain
            # if nothing is left, then this csp is impossible, return false
            if self.revise(var1, var2):
                if len(self.domains[var1]) == 0:
                    return False

                # If this csp is possible, add var1 neighbors into queue (except var2)
                var1_neighbor = self.crossword.neighbors(var1)
                var1_neighbor.remove(var2)
                for var in var1_neighbor:
                    arcs.append((var, var1))

        return True

    def assignment_complete(self, assignment):
        """
        Return True if `assignment` is complete (i.e., assigns a value to each
        crossword variable); return False otherwise.
        """
        # Complete if all variables are assigned to a value
        # Assignment dictionary has all variables
        return len(self.domains) == len(assignment)

    def consistent(self, assignment):
        """
        Return True if `assignment` is consistent (i.e., words fit in crossword
        puzzle without conflicting characters); return False otherwise.
        """
        value_set = set()
        for var, value in assignment.items():
            # 1. All values are distinct
            if value not in value_set:
                value_set.add(value)
            else:
                return False

            # 2. Every value is of correct length
            if var.length != len(value):
                return False

            # 3. No conflict between neighbors
            for neighbor in self.crossword.neighbors(var):
                if neighbor in assignment:
                    (index_var, index_neighbor) = self.crossword.overlaps[var, neighbor]
                    if value[index_var] != assignment[neighbor][index_neighbor]:
                        return False

        return True

    def order_domain_values(self, var, assignment):
        """
        Return a list of values in the domain of `var`, in order by
        the number of values they rule out for neighboring variables.
        The first value in the list, for example, should be the one
        that rules out the fewest values among the neighbors of `var`.
        """
        rule_out = {}
        neighbors = self.crossword.neighbors(var)
        for value in self.domains[var]:
            rule_out[value] = 0

            # Same value in other variables' domain
            for other_var in self.domains:
                if other_var == var or other_var in assignment:
                    continue
                if value in self.domains[other_var]:
                    rule_out[value] += 1

            # Violate arc-consistency
            for neighbor in neighbors:
                if neighbor in assignment:
                    continue
                (index_var, index_neighbor) = self.crossword.overlaps[var, neighbor]
                for word in self.domains[neighbor]:
                    if value[index_var] != word[index_neighbor]:
                        rule_out[value] += 1

        return sorted(rule_out, key=rule_out.get)

    def select_unassigned_variable(self, assignment):
        """
        Return an unassigned variable not already part of `assignment`.
        Choose the variable with the minimum number of remaining values
        in its domain. If there is a tie, choose the variable with the highest
        degree. If there is a tie, any of the tied variables are acceptable
        return values.
        """
        candidate = None
        for var in self.domains:
            if var in assignment:
                continue

            # If there's less choice in var's domain than candidate's, choose var instead
            if candidate is None or len(self.domains[var]) < len(self.domains[candidate]):
                candidate = var

            # Or if they have same domain length, choose by their degree (with more neighbors)
            elif len(self.domains[var]) == len(self.domains[candidate]) and \
                len(self.crossword.neighbors(var)) > len(self.crossword.neighbors(candidate)):
                candidate = var

        return candidate

    def backtrack(self, assignment):
        """
        Using Backtracking Search, take as input a partial assignment for the
        crossword and return a complete assignment if possible to do so.

        `assignment` is a mapping from variables (keys) to words (values).

        If no assignment is possible, return None.
        """
        # Terminate condition (assignment complete)
        if self.assignment_complete(assignment):
            return assignment

        # Select an unassigned variable using:
        # 1. Minimum remaining range of domain heuristics
        # 2. Highest number of degrees heuristics
        var = self.select_unassigned_variable(assignment)

        for value in self.order_domain_values(var, assignment):
            assignment[var] = value
            if self.consistent(assignment):
                self.ac3() # Enforce arc-consistency everytime
                result = self.backtrack(assignment) # Recursively tracks all assignments
                # If there is a possible result, return it
                if result is not None:
                    return result

            # Not consistent or no possible result, the variable cannot take on this value
            assignment.pop(var)

        # No value is possible for a result, backtrack
        return None

def main():
    """ Main Function
    Takes arguments from command line, decide which structure and words files to use
    Use the CrosswordCreator AI to solve the puzzle
    Outputs the result in terminal and also as a png
    """
    # Check usage
    if len(sys.argv) not in [3, 4]:
        sys.exit("Usage: python generate.py structure words [output]")

    # Parse command-line arguments
    structure = sys.argv[1]
    words = sys.argv[2]
    output = sys.argv[3] if len(sys.argv) == 4 else None

    # Generate crossword
    crossword = Crossword(structure, words)
    creator = CrosswordCreator(crossword)
    assignment = creator.solve()

    # Print result
    if assignment is None:
        print("No solution.")
    else:
        creator.print(assignment)
        if output:
            creator.save(assignment, output)


if __name__ == "__main__":
    main()
