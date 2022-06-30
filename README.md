# Harvard University's CS50 - Introduction to AI

In the summer after my sophomore year, in order to gain more knowledge and continue programming, I chose to study Harvard's online artificial intelligence course, [CS50](https://cs50.harvard.edu/ai/2020/), which I found through the online learning platform, [edX](https://www.edx.org/)<br/>

In this repository, I will put my notes and my work on course projects. For each lecture, I will list the objectives of the lecture and corresponding projects. Detailed notes and in-class examples regarding each lecture can be accessed through the link of the corresponding lecture below

Please <strong>DO NOT</strong> directly use the source code, they are <strong>ONLY</strong> for reference. Plagiarism is strictly prohibited by both the Harvard University and the edX platform

## Course Overview

This course explores the concepts and algorithms at the foundation of modern artificial intelligence, diving into the ideas that give rise to technologies like game-playing engines, handwriting recognition, and machine translation. Through hands-on projects, students gain exposure to the theory behind graph search algorithms, classification, optimization, reinforcement learning, and other topics in artificial intelligence and machine learning as they incorporate them into their own Python programs. By course’s end, students emerge with experience in libraries for machine learning as well as knowledge of artificial intelligence principles that enable them to design intelligent systems of their own

### Artificial Intelligence

Artificial Intelligence (AI) covers a range of techniques that appear as sentient behavior by the computer. For example, AI is used to recognize faces in photographs on your social media, beat the World’s Champion in chess, and process your speech when you speak to Siri or Alexa on your phone. This course will explore some of the ideas that make AI possible

- [Search](#lecture-0---search): Finding a solution to a problem, like a navigator app that finds the best route from your origin to the destination, or like playing a game and figuring out the next move
- [Knowledge](#lecture-1---knowledge): Representing information and drawing inferences from it
- [Uncertainty](#lecture-2---uncertainty): Dealing with uncertain events using probability
- [Optimization](#lecture-3---optimization): Finding not only a correct way to solve a problem, but a better—or the best—way to solve it
- Learning: Improving performance based on access to data and experience. For example, your email is able to distinguish spam from non-spam mail based on past experience
- Neural Networks: A program structure inspired by the human brain that is able to perform tasks effectively
- Language: Processing natural language, which is produced and understood by humans

## Lecture 0 - [Search](/0.Search/)

Search problems involve an agent that is given an initial state and a goal state, and it returns a solution of how to get from the former to the latter

### Objectives

- Search Problem Terms
- Algorithms
- Adversarial Search

### Projects

- [Degrees](/0.Search/degrees/)
- [Tic-Tac-Toe](/0.Search/tictactoe/)

## Lecture 1 - [Knowledge](/1.Knowledge/)

Humans reason based on existing knowledge and draw conclusions. The concept of representing knowledge and drawing conclusions from it is also used in AI, and this lecture will explore how we can achieve this behavior

### Objectives

- Propositional Logic
- Inference
- First Order Logic

### Projects

- [Knights](/1.Knowledge/knights/)
- [Minesweeper](/1.Knowledge/minesweeper/)

## Lecture 2 - [Uncertainty](2.Uncertainty/)

Last lecture shows how AI can represent knowledge and from that, derive new knowledge. But in reality, usually we don't have that much knowledge for certain. In fact, most of the times AI can only have partial knowledge and leaving some space for uncertainty. Still, we would want the AI to make the best possible decision during these situations. For example, when predicting weather, the AI has the information about the weather conditions right now but the AI cannot be certain for tomorrow. Still, the AI can do better than pure chance. This lecture will demonstrate how an AI can make optimal decisions with limited knowledge

### Objectives

- Probability
- Random Variables
- Sampling

### Projects

- [PageRank](2.Uncertainty/pagerank/)
- [Heredity](2.Uncertainty/heredity/)

## Lecture 3 - [Optimization](3.Optimization/)

Optimization is choosing the best option from a set of possible options. We have already encountered problems where we tried to find the best possible option, such as in the minimax algorithm, and this lecture will learn about tools that we can use to solve an even broader range of problems

### Objectives

- Local Search
- Linear Programming
- Constraint Satisfaction

### Projects

- [Crossword](3.Optimization/crossword/)
