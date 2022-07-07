""" Helper classes and methods for the search problems """

class Node():
    """ A node that contains information needed for search """
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action

class StackFrontier():
    """ Uses a Stack to store information. DFS """
    def __init__(self):
        self.frontier = []

    def add(self, node):
        """ Add a node into the stack """
        self.frontier.append(node)

    def contains_state(self, state):
        """ Determine if a state is inside the stack """
        return any(node.state == state for node in self.frontier)

    def empty(self):
        """ Determine if a stack is empty """
        return len(self.frontier) == 0

    def remove(self):
        """ Remove the top of the stack and return it """
        if self.empty():
            raise Exception("empty frontier")

        node = self.frontier[-1]
        self.frontier = self.frontier[:-1]
        return node


class QueueFrontier(StackFrontier):
    """ Uses a Queue to store information. BFS """
    def remove(self):
        """ Remove the next item in the queue and return it """
        if self.empty():
            raise Exception("empty frontier")

        node = self.frontier[0]
        self.frontier = self.frontier[1:]
        return node
