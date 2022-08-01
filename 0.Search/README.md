# Search

Given two inputs, the intial state and the goal state, the AI will navigate to find the optimal solution of a series of actions

## Search Problem Terms

### Agent

Agent is an entity that perceives its environment and acts upon that environment. For instance, this entity could be an AI program, the environment could be the state of a chess game, and the AI will determine the action under that state, in another word, how to take the next move

### State

A configuration of an agent in its environment, also can be understood as the state of the game in a chess game

### Initial State

The state from which the search algorithm starts, the environment when the agent first kick in

### Actions

All possible choices that can be made by an agent in a state

### Transition Model

A description of what state results from performing any applicable action in any state </br>
i.e. result(s, a) return the state in s by performing the action a

<img width="676" alt="Screen Shot 2022-06-19 at 8 46 33 PM" src="https://user-images.githubusercontent.com/98674104/174507131-39f1116b-7bdb-4fb6-ba3d-dfb2d163800e.png">

### State Space

The set of all states reachable from the initial state by any sequence of actions

<img width="679" alt="Screen Shot 2022-06-19 at 8 46 55 PM" src="https://user-images.githubusercontent.com/98674104/174507153-ec890424-f4ef-41d7-9c00-c6e2708c1f9f.png">

### Goal Test

The condition that determines whether a given state is a goal state, if certain state passes the goal test, which means the algorithm should be terminated since we have found the solution

### Path Cost

A numerical cost associated with a given path </br>
The cost of each edge (between two vertices) could be 1 or more than 1 </br>
i.e. when navigating a path on the map, we do not only consider the distance but also trying to minimize the path cost, which in real life is the traffic condition on certain roads. If there's a bad traffic on a certain road, then the cost of that road is high

<img width="675" alt="Screen Shot 2022-06-19 at 8 47 16 PM" src="https://user-images.githubusercontent.com/98674104/174507169-e74f9eaa-3533-4d9b-a549-d0765f475a5b.png">

## Algorithms

### [Depth-First Search (DFS)](https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/)

Exhausts each one direction before trying another direction. If there are several possible ways, the agent will choose randomly. So, DFS might not be efficient to find the path due to this randomness, and it does not guarantee to find the shortest path

For example:

<img width="675" alt="Screen Shot 2022-06-19 at 8 48 56 PM" src="https://user-images.githubusercontent.com/98674104/174507280-633a5e6a-9d41-4111-9634-0b12d5963dcb.png">

OR </br>

<img width="678" alt="Screen Shot 2022-06-19 at 8 50 04 PM" src="https://user-images.githubusercontent.com/98674104/174507348-2df8c20c-6e2e-4df2-912a-ee3f2dc6dafd.png">

DFS typically uses a [stack](https://www.programiz.com/dsa/stack) data structure to store all of the possible actions. Below is the pseudo code for the DFS implementation

```
DFS(G,v)   ( v is the vertex where the search starts )
    Stack S := {};   ( start with an empty stack )
    for each vertex u, set visited[u] := false;
    push S, v;
    while (S is not empty) do
        u = pop S;

        if u is destination then
            return path from v to u

        if (not visited[u]) then
            visited[u] = true;
            for each unvisited neighbour w of u
                push S, w;
```

### [Breadth-First Search (BFS)](https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/)

Follow multiple directions at the same time, taking one step in each possible direction before taking the second step in each direction </br>
Guarantee the shortest path, but takes relatively a long time as it seeks each directions setp by step. Also, BFS only considers unweighted path and ignore the path cost, so it's more efficient to use A\* when doing map navigation rather than BFS

<img width="677" alt="Screen Shot 2022-06-19 at 8 48 21 PM" src="https://user-images.githubusercontent.com/98674104/174507239-b6c05071-3100-4143-81d1-95581c24f33e.png">

BFS typically uses a [queue](https://www.programiz.com/dsa/queue) data structure to store all of the possible actions. Below is the pseudo code for the BFS implementation, the only difference between DFS and BFS is one uses stack and one uses queue

```
BFS (G, s)  (G is the graph and s is the source node)
    let Q be queue
    Q.enqueue( s )
    mark s as visited

    while ( Q is not empty)
        v  =  Q.dequeue( )

        if v is destination then
            return path from s to v

        for all neighbours w of v in Graph G
            if w is not visited
                Q.enqueue( w )
```

### Example

Check out `examples` directory for Python implementation of DFS and BFS that solves mazes

### [Greedy Best-First Search](https://www.javatpoint.com/ai-informed-search-algorithms#:~:text=Greedy%20best%2Dfirst%20search%20algorithm,the%20advantages%20of%20both%20algorithms.)

At any time, choose the state that is closest to the goal as the next state (only consider the estimated cost to the goal), as estimated by a
heuristic function h(n). However, it only consider the distance between the current node to the destination but not the cost to reach this node from the source. The greedy algorithm does not guarantee the shortest path

<img width="678" alt="Screen Shot 2022-06-19 at 8 55 53 PM" src="https://user-images.githubusercontent.com/98674104/174507683-67090988-940d-4a4e-b045-0ac985f4fb4c.png">

Manhattan distance vs Euclidean distance. We use either of these to estimate the cost from current state to the goal, then choose the action that minimizes the cost

<img src="https://user-images.githubusercontent.com/98674104/174507758-c1a8a28d-3a2a-4a3b-bfe8-be28384a6a95.jpeg" width="680" height="350">

### [A\* Search](https://www.geeksforgeeks.org/a-search-algorithm/)

Consider both the cost of path until now and the estimated cost to the goal, g(n) + h(n)

- g(n) = cumalative cost reaching the current node
- h(n) = estimated cost to the destination node

Thus, A\* is the best path search algorithm as it considers the distance, weight, cost, etc. and it guarantees to find the shortest path

<img width="679" alt="Screen Shot 2022-06-19 at 8 53 16 PM" src="https://user-images.githubusercontent.com/98674104/174507529-69b6908c-f37f-41ed-a94a-0d9323aab6e8.png">

```
A* (G, s)  (G is the graph and s is the source node)

    # Order the queue by ascending order of g(n) + h(n)
    let Q be priority_queue
    Q.enqueue( s )
    mark s as visited

    while ( Q is not empty)
        v  =  Q.dequeue( )

        if v is destination then
            return path from s to v

        for all neighbours w of v in Graph G
            if w is not visited
                Q.enqueue( w )
```

## Adversarial Search

### [Minimax Algorithm](https://www.javatpoint.com/mini-max-algorithm-in-ai)

A recursive or backtracking algorithm which is used in decision-making and game theory. It provides an optimal move for the player assuming that opponent is also playing optimally. For instance, in the figure below, the green player is trying to maximize the score and the red player is to minimize to score, which is exactly the same in any game

<img width="674" alt="Screen Shot 2022-06-19 at 8 53 37 PM" src="https://user-images.githubusercontent.com/98674104/174507542-ed38bf8f-7f65-41f2-8af2-b3a3b30b9e2d.png">

### [Alpha-Beta Pruning](https://www.javatpoint.com/ai-alpha-beta-pruning)

An optimization technique for the Minimax Algorithm </br>
For example, if we want to find the max of three nodes and we know the current node will be definitely less than the previous node, then we do not need to explore every other subnodes of it

<img width="679" alt="Screen Shot 2022-06-19 at 8 53 53 PM" src="https://user-images.githubusercontent.com/98674104/174507566-df02b8e6-a489-4d58-9a8a-ab0e98ec0bc3.png">

### Depth-Limited Minimax

A type of Minimax Algorithm that only search to a certain depth, arrive at a decision more quickly

```
function minimax(node, depth, maximizingPlayer) is
    if depth == 0 or node is a terminal node then
        return static evaluation of node

    if MaximizingPlayer then    // for Maximizer Player
        maxEva= -infinity
        for each child of node do
        eva= minimax(child, depth-1, false)
        maxEva= max(maxEva,eva) //gives Maximum of the values
        return maxEva

    else    // for Minimizer player
        minEva= +infinity
        for each child of node do
        eva= minimax(child, depth-1, true)
        minEva= min(minEva, eva)    //gives minimum of the values
        return minEva
```

## Examples

Check out some [examples](examples/) that practice these theories
