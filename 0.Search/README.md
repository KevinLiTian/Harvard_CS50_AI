# Notes for Lecture 0 - Search

- Agent: An entity that perceives its environment and acts upon that environment
- State: A configuration of an agent in its environment
  - Initial State: The state from which the search algorithm starts
- Actions: Choices that can be made in a state
- Transition Model: A description of what state results from performing any applicable action in any state
- State Space: The set of all states reachable from the initial state by any sequence of actions
- Goal Test: The condition that determines whether a given state is a goal state
- Path Cost: A numerical cost associated with a given path
- Algorithms Solving Search Problems
  - [Depth-First Search (DFS)](https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/): Exhausts each one direction before trying another direction
  - [Breadth-First Search (BFS)](https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/): Follow multiple directions at the same time, taking one step in each possible direction before taking the second step in each direction
  - [Greedy Best-First Search](https://www.javatpoint.com/ai-informed-search-algorithms#:~:text=Greedy%20best%2Dfirst%20search%20algorithm,the%20advantages%20of%20both%20algorithms.): At any time, choose the state that is closest to the goal as the next state (only consider the estimated cost to the goal)
  - [A\* Search](https://www.geeksforgeeks.org/a-search-algorithm/): Consider both the cost of path until now and the estimated cost to the goal
- Adversarial Search
  - [Minimax Algorithm](https://www.javatpoint.com/mini-max-algorithm-in-ai): A recursive or backtracking algorithm which is used in decision-making and game theory. It provides an optimal move for the player assuming that opponent is also playing optimally
  - [Alpha-Beta Pruning](https://www.javatpoint.com/ai-alpha-beta-pruning): An optimization technique for the Minimax Algorithm
  - Depth-Limited Minimax: A type of Minimax Algorithm that only search to a certain depth, arrive at a decision more quickly
