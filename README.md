# Harvard CS50’s Introduction to Artificial Intelligence with Python

In the summer after my sophomore year, in order to gain more knowledge and continue programming, I chose to study Harvard's online artificial intelligence course, [CS50](https://cs50.harvard.edu/ai/2020/), which I found through the online learning platform, [edX](https://www.edx.org/). <br/>

In this repository, I will put my notes and my work on course projects. For each lecture, I will list the objectives of the lecture and two corresponding projects. Detailed notes regarding each lecture can be accessed through the link of each lecture.

## Course Overview

This course explores the concepts and algorithms at the foundation of modern artificial intelligence, diving into the ideas that give rise to technologies like game-playing engines, handwriting recognition, and machine translation. Through hands-on projects, students gain exposure to the theory behind graph search algorithms, classification, optimization, reinforcement learning, and other topics in artificial intelligence and machine learning as they incorporate them into their own Python programs. By course’s end, students emerge with experience in libraries for machine learning as well as knowledge of artificial intelligence principles that enable them to design intelligent systems of their own.

### Artificial Intelligence

Artificial Intelligence (AI) covers a range of techniques that appear as sentient behavior by the computer. For example, AI is used to recognize faces in photographs on your social media, beat the World’s Champion in chess, and process your speech when you speak to Siri or Alexa on your phone. This course will explore some of the ideas that make AI possible.

- [Search](#lecture-0---search)
- [Knowledge](#lecture-1---knowledge)
- Uncertainty
- Optimization
- Learning
- Neural Networks
- Language

## Lecture 0 - Search

Finding a solution to a problem, like a navigator app that finds the best route from your origin to the destination, or like playing a game and figuring out the next move.

### Objectives

- Agent
- State
  - Initial State
- Actions
- Transition Model
- State Space
- Goal Test
- Path Cost
- Algorithms Solving Search Problems
  - Depth-First Search (DFS)
  - Breadth-First Search (BFS)
  - Greedy Best-First Search
  - A\* Search
- Adversarial Search
  - Minimax
  - Alpha-Beta Pruning
  - Depth-Limited Minimax

### Projects

- [Degrees](/0.Search/degrees/)
- [Tic-Tac-Toe](/0.Search/tictactoe/)

## Lecture 1 - Knowledge

Humans reason based on existing knowledge and draw conclusions. The concept of representing knowledge and drawing conclusions from it is also used in AI, and in this lecture we will explore how we can achieve this behavior.

### Objectives

- Knowledge-Based Agents
- Sentence
- Propositional Logic
  - Propositional Symbols
  - Logical Connectives
  - Model
  - Knowledge Base (KB)
  - Entailment (⊨)
- Knowledge Engineering
- Inference
  - Inference Rules
- Resolution
  - Complimentary Literals
  - Clause
  - Disjunction
  - Conjunction
  - Conjunctive Normal Form (CNF)
  - Empty Clause
- First Order Logic
  - Universal Quantification
  - Existential Quantification

### Projects

- [Knights](/1.Knowledge/knights/)
- [Minesweeper](/1.Knowledge/minesweeper/)
