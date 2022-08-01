# Optimization

An AI should not only find the solution, but also find the optimal solution, by either maximizing the objective or minimizing the cost

## Local Search

Local search is a search algorithm that maintains a single node and searches by moving to a neighboring node, and determines whether to move to neighboring node based on if the neighbor node is better or worse

### State Space Landscape

In all the state space, there are better and worse results that are unevenly distributed, as the figure below illustrates. Optimization techniques allows agent to find the global optimum or global minimum based on the need of the problem

<img src="https://user-images.githubusercontent.com/99038613/176784545-bb4f5683-9d8d-47f5-8258-028fe8f6ab66.jpg" width=60% height=60%>

### Hill Climbing

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
- **Limitation**: Hill climbing only changes current state if neighboring state is better, but if we reached any local minima/maxmima, the neighboring states are all worse than the current state, thus stuck at that local point, then the algorithm will terminate which leaves us at a local, instead of a global optimum

### Random Start

One way to get around this limitation is by choosing the start points randomly, and re-run the hill climbing algorithm multiple times, then record the result of each rum. Maybe some iterations of hill climb will result better than other hill climbs because the start point of those iterations are randomly choosed and are lucky enough to fall into the local region of the global optimum

### [Simulated Annealing](https://en.wikipedia.org/wiki/Simulated_annealing)

Although we have seen variants that can improve hill climbing, they all share the same fault: once the algorithm reaches a local maximum, it stops running. Simulated annealing allows the algorithm to “dislodge” itself if it gets stuck in a local maximum

- [Traveling Salesman Problem (TSP)](https://en.wikipedia.org/wiki/Travelling_salesman_problem): A typical type of problem that can use Simulated Annealing to get good results

```
Notations :
  T : temperature. Decreases to 0.
  s : a system state
  E(s) : Energy at s. The function we want to minimize
  ∆E : variation of E, from state s to state s_next
  P(∆E , T) : Probability to move from s to s_next.
  	if  ( ∆E < 0 ) P = 1
  	      else P = exp ( - ∆E / T) . Decreases as T →  0

Pseudo-code:
    Let s = s0  -- initial state
    For k = 0 through kmax (exclusive):
        T ← temperature(k , kmax)
        Pick a random neighbour state , s_next ← neighbour(s)
        ∆E ← E(s) - E(s_next)
        If P(∆E , T) ≥ random(0, 1), move to the new state:
            s ← s_next
    Output: the final state s
```

## Linear Programming

Linear programming is a family of problems that optimize a linear equation (an equation of the form y = ax₁ + bx₂ + …)

## Constraint Satisfaction Problem

Constraint Satisfaction problems are a class of problems where variables need to be assigned values while satisfying some conditions. For example, the game of Sudoku, where each empty space is a variable that needs to be assigned value from 1 to 9

### Unary & Binary Constraints

Unary constraints are the limitations applying to a single variable such as a cannot be equal to 1. Binary constraints are the limitations applying to two variables such as the value of a cannot be equal to the value of b. In the game of Sudoku, the unary constraint is for each space, the value must be within 1 to 9. The binary constraint is that two variable/empty space, in the same row or column or each 3x3 block, cannot take on the same value

### Node Consistency

Node consistency is when all the values in a variable’s domain satisfy the variable’s unary constraints

### Arc Consistency

Arc consistency is when all the values in a variable’s domain satisfy the variable’s binary constraint, where an arc is a pair of variables

### Backtracking Search

Backtracking search is a type of a search algorithm that takes into account the structure of a constraint satisfaction search problem. It recursively assigns variables to certain values in their domains, if anything goes wrong it backtracks to the previous point and tries another value

- **Inference**: Although backtracking search is more efficient than simple search, it still takes a lot of computational power. Enforcing arc consistency, on the other hand, is less resource intensive. By interleaving backtracking search with inference (enforcing arc consistency), we can get at a more efficient algorithm

- **Minimum Remaining Values (MRV)**: When choosing the next variable to try, the MRV heuristic says that we should let the variable that has the least number of values in its domain to try first since there's a higher chance to get the correct result

```
csp - Constraint Satisfaction Problem
assignment - Assign variables to a value
assignment complete - All variables are assigned to a value
domain -  Set of all values a variable can take on
consistent - Ensure that so far, all constraints are satisfied

function BackTrack(assignment, csp)
  if assignment complete:
    return assignment

  var = select from unassigned variables(assignment, csp)
  for value in domain(var, assignment, csp):
      add {var, value} to assignment

      if value is consistent with assignment:
        Ensure Arc-Consistency

        result = BackTrack(assignement, csp)

        if result not failed:
          return result

      remove {var, value} from assignment

    return fail if the variable cannot take on any value
```

## Examples

Check out some [examples](examples/) that practice these theories
