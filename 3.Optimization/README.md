# Optimization

- Local Search: A search algorithm that maintains a single node and searches by moving to a neighboring node
- Hill Climbing: Hill climbing is one type of a local search algorithm. In this algorithm, the neighbor states are compared to the current state, and if any of them is better, we change the current node from the current state to that neighbor state
  - Local and Global Minima and Maxima: A local maximum (plural: maxima) is a state that has a higher value than its neighboring states. As opposed to that, a global maximum is a state that has the highest value of all states in the state-space
  - Hill Climbing Variants
    - Steepest-ascent: Choose the highest-valued neighbor
    - Stochastic: Choose randomly from higher-valued neighbors
    - First-choice: Choose the first higher-valued neighbor
    - Random-restart: Conduct hill climbing multiple times
    - Local Beam Search: Chooses the k highest-valued neighbors
- [Simulated Annealing](https://en.wikipedia.org/wiki/Simulated_annealing): Although we have seen variants that can improve hill climbing, they all share the same fault: once the algorithm reaches a local maximum, it stops running. Simulated annealing allows the algorithm to “dislodge” itself if it gets stuck in a local maximum
  - [Traveling Salesman Problem (TSP)](https://en.wikipedia.org/wiki/Travelling_salesman_problem): A typical type of problem that can use Simulated Annealing to get good results
- Linear Programming: inear programming is a family of problems that optimize a linear equation (an equation of the form y = ax₁ + bx₂ + …)
- Constraint Satisfaction: Constraint Satisfaction problems are a class of problems where variables need to be assigned values while satisfying some conditions
- Node Consistency: Node consistency is when all the values in a variable’s domain satisfy the variable’s unary constraints
- Arc Consistency: Arc consistency is when all the values in a variable’s domain satisfy the variable’s binary constraints (note that we are now using “arc” to refer to what we previously referred to as “edge”)
- Backtracking Search: Backtracking search is a type of a search algorithm that takes into account the structure of a constraint satisfaction search problem
  - Inference: Although backtracking search is more efficient than simple search, it still takes a lot of computational power. Enforcing arc consistency, on the other hand, is less resource intensive. By interleaving backtracking search with inference (enforcing arc consistency), we can get at a more efficient algorithm. This algorithm is called the Maintaining [Arc-Consistency algorithm](https://www.sciencedirect.com/topics/computer-science/arc-consistency-algorithm)
  - Minimum Remaining Values (MRV): The idea here is that if a variable’s domain was constricted by inference, and now it has only one value left (or even if it’s two values), then by making this assignment we will reduce the number of backtracks we might need to do later
