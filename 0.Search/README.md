# Notes for Lecture 0 - Search

#### Agent

An entity that perceives its environment and acts upon that environment

#### State

A configuration of an agent in its environment

<img width="675" alt="Screen Shot 2022-06-19 at 8 45 52 PM" src="https://user-images.githubusercontent.com/98674104/174507105-dbd932c9-fbfa-4a4f-b5df-f79bb3d6e298.png">

#### Initial State

The state from which the search algorithm starts

#### Actions

Choices that can be made in a state </br>
i.e. Up, Down, Left, Right in the 15 Puzzle Game

<img width="676" alt="Screen Shot 2022-06-19 at 8 46 13 PM" src="https://user-images.githubusercontent.com/98674104/174507117-71e97a91-08ca-416c-b32a-af7dc5516e55.png">

#### Transition Model

A description of what state results from performing any applicable action in any state </br>
i.e. result(s, a) return the state in s by performing the action a

<img width="676" alt="Screen Shot 2022-06-19 at 8 46 33 PM" src="https://user-images.githubusercontent.com/98674104/174507131-39f1116b-7bdb-4fb6-ba3d-dfb2d163800e.png">

#### State Space

The set of all states reachable from the initial state by any sequence of actions

<img width="679" alt="Screen Shot 2022-06-19 at 8 46 55 PM" src="https://user-images.githubusercontent.com/98674104/174507153-ec890424-f4ef-41d7-9c00-c6e2708c1f9f.png">

#### Goal Test

The condition that determines whether a given state is a goal state

#### Path Cost

A numerical cost associated with a given path </br>
The cost of each edge (between two vertices) could be 1 or more than 1 </br>
i.e. when navigating a path on the map, we do not only consider the distance but also trying to minimize the path cost

<img width="675" alt="Screen Shot 2022-06-19 at 8 47 16 PM" src="https://user-images.githubusercontent.com/98674104/174507169-e74f9eaa-3533-4d9b-a549-d0765f475a5b.png">

## Algorithms

#### [Depth-First Search (DFS)](https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/)

Exhausts each one direction before trying another direction </br>
There are different possible ways, which will be chosen randomly. So, DFS might not be efficient to find the shortiest path due to this randomness </br>

For example: </br>

<img width="675" alt="Screen Shot 2022-06-19 at 8 48 56 PM" src="https://user-images.githubusercontent.com/98674104/174507280-633a5e6a-9d41-4111-9634-0b12d5963dcb.png">

OR </br>

<img width="678" alt="Screen Shot 2022-06-19 at 8 50 04 PM" src="https://user-images.githubusercontent.com/98674104/174507348-2df8c20c-6e2e-4df2-912a-ee3f2dc6dafd.png">

#### [Breadth-First Search (BFS)](https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/)

Follow multiple directions at the same time, taking one step in each possible direction before taking the second step in each direction </br>
Guarantee the shortest path, but take long time as it seeks each directions setp by step. Also, BFS only considers unweighted path and ignore the path cost, so it's more efficient to use A\* when doing map navigation rather than BFS

<img width="677" alt="Screen Shot 2022-06-19 at 8 48 21 PM" src="https://user-images.githubusercontent.com/98674104/174507239-b6c05071-3100-4143-81d1-95581c24f33e.png">

#### [Greedy Best-First Search](https://www.javatpoint.com/ai-informed-search-algorithms#:~:text=Greedy%20best%2Dfirst%20search%20algorithm,the%20advantages%20of%20both%20algorithms.)

At any time, choose the state that is closest to the goal as the next state (only consider the estimated cost to the goal), as estimated by a
heuristic function h(n). However, it only consider the distance between the current node to the destination but not consider the cost to reach this node (g(n))

<img width="678" alt="Screen Shot 2022-06-19 at 8 55 53 PM" src="https://user-images.githubusercontent.com/98674104/174507683-67090988-940d-4a4e-b045-0ac985f4fb4c.png">

Manhattan distance vs Euclidean distance, we uses Manhattan distance in the Greedy BFS

<img src="https://user-images.githubusercontent.com/98674104/174507758-c1a8a28d-3a2a-4a3b-bfe8-be28384a6a95.jpeg" width="680" height="350">


#### [A\* Search](https://www.geeksforgeeks.org/a-search-algorithm/)

Consider both the cost of path until now and the estimated cost to the goal, g(n) + h(n) </br>

g(n) = cost to reach node </br>
h(n) = estimated cost to goal </br>

Thus, A\* is the best path search algorithm as it considers the distance, weight, cost, etc.

<img width="679" alt="Screen Shot 2022-06-19 at 8 53 16 PM" src="https://user-images.githubusercontent.com/98674104/174507529-69b6908c-f37f-41ed-a94a-0d9323aab6e8.png">

## Adversarial Search

#### [Minimax Algorithm](https://www.javatpoint.com/mini-max-algorithm-in-ai)

A recursive or backtracking algorithm which is used in decision-making and game theory. It provides an optimal move for the player assuming that opponent is also playing optimally

<img width="674" alt="Screen Shot 2022-06-19 at 8 53 37 PM" src="https://user-images.githubusercontent.com/98674104/174507542-ed38bf8f-7f65-41f2-8af2-b3a3b30b9e2d.png">

#### [Alpha-Beta Pruning](https://www.javatpoint.com/ai-alpha-beta-pruning)

An optimization technique for the Minimax Algorithm </br>
For example, if we want to find the max of three nodes and we know the current node will be definitely less than the previous node, then we do not need to explore every other subnodes of it

<img width="679" alt="Screen Shot 2022-06-19 at 8 53 53 PM" src="https://user-images.githubusercontent.com/98674104/174507566-df02b8e6-a489-4d58-9a8a-ab0e98ec0bc3.png">

#### Depth-Limited Minimax

A type of Minimax Algorithm that only search to a certain depth, arrive at a decision more quickly
