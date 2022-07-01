# Optimization

An AI should not only find the solution, but also find the optimal solution, by either maximizing the objective or minimizing the cost

## Local Search

Local search is a search algorithm that maintains a single node and searches by moving to a neighboring node

#### State Space Landscape

In all the state space, there are better and worse results that are unevenly distributed, as the figure below illustrates

<img src="https://user-images.githubusercontent.com/99038613/176784545-bb4f5683-9d8d-47f5-8258-028fe8f6ab66.jpg" width=60% height=60%>

#### Hill Climbing

Hill climbing is one type of a local search algorithm. In this algorithm, the neighbor states are compared to the current state, and if any of them is better, we change the current node from the current state to that neighbor state

- **Local and Global Minima and Maxima**: A local maximum (plural: maxima) is a state that has a higher value than its neighboring states. As opposed to that, a global maximum is a state that has the highest value of all states in the state-space

    <img src="https://user-images.githubusercontent.com/99038613/176784640-b8d017a2-d617-4b45-b7b4-1b88def9bd8f.jpg">

    <img src="https://user-images.githubusercontent.com/99038613/176784649-37b67396-fbcc-4933-8b4a-be68f27e5b44.jpg">

- **Hill Climbing Variants**
  - **Steepest-ascent**: Choose the highest-valued neighbor
  - **Stochastic**: Choose randomly from higher-valued neighbors
  - **First-choice**: Choose the first higher-valued neighbor
  - **Random-restart**: Conduct hill climbing multiple times
  - **Local Beam Search**: Chooses the k highest-valued neighbors
- **Limitation**: Hill climbing only changes current state if neighboring state is better, but if we reached any local minima/maxmima, the neighboring states are all worse than the current state, then the algorithm will terminate which leaves us at a local, instead of a global maxima/minima

#### [Simulated Annealing](https://en.wikipedia.org/wiki/Simulated_annealing)

Although we have seen variants that can improve hill climbing, they all share the same fault: once the algorithm reaches a local maximum, it stops running. Simulated annealing allows the algorithm to “dislodge” itself if it gets stuck in a local maximum

- [Traveling Salesman Problem (TSP)](https://en.wikipedia.org/wiki/Travelling_salesman_problem): A typical type of problem that can use Simulated Annealing to get good results

## Linear Programming

Linear programming is a family of problems that optimize a linear equation (an equation of the form y = ax₁ + bx₂ + …)

## Constraint Satisfaction Problem

Constraint Satisfaction problems are a class of problems where variables need to be assigned values while satisfying some conditions

#### Unary & Binary Constraints

Unary constraints are the limitations applying to a single variable such as a cannot be equal to 1. Binary constraints are the limitations applying to two variables such as the value of a cannot be equal to the value of b

#### Node Consistency

Node consistency is when all the values in a variable’s domain satisfy the variable’s unary constraints

#### Arc Consistency

Arc consistency is when all the values in a variable’s domain satisfy the variable’s binary constraint, where an arc is a pair of variables

#### Backtracking Search

Backtracking search is a type of a search algorithm that takes into account the structure of a constraint satisfaction search problem. It recursively assigns variables to certain values in their domains, if anything goes wrong it backtracks to the previous point and tries another value

- **Inference**: Although backtracking search is more efficient than simple search, it still takes a lot of computational power. Enforcing arc consistency, on the other hand, is less resource intensive. By interleaving backtracking search with inference (enforcing arc consistency), we can get at a more efficient algorithm

- **Minimum Remaining Values (MRV)**: When choosing the next variable to try, the MRV heuristic says that we should let the variable that has the least number of values in its domain to try first since there's a higher chance to get the correct result
