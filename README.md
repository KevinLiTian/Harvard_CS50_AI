# Harvard University's CS50AI - Introduction to Artificial Intelligence

In the summer after my sophomore year, in order to gain more knowledge and continue programming, I chose to study Harvard's online artificial intelligence course, [CS50AI](https://cs50.harvard.edu/ai/2020/), which I found through the online learning platform, [edX](https://www.edx.org/). Here's my [certificate](https://certificates.cs50.io/f5a81eaf-2bf6-4c43-8a3c-c866f94c1052) after completing the course

In this repository, I am putting my notes and my work on course projects. For each lecture, I will list the objectives of the lecture and corresponding projects. Detailed notes and in-class examples regarding each lecture can be accessed through the link of the corresponding lecture below. The release material and specification of each project are also included in the `DIY` directory in case one wants to practice doing them

Please <strong>DO NOT</strong> directly use the source code, they are <strong>ONLY</strong> for reference. Plagiarism is strictly prohibited by both the Harvard University and the edX platform. See [academic honesty](https://cs50.harvard.edu/college/2021/fall/syllabus/#academic-honesty) and [license](https://cs50.harvard.edu/ai/2020/license/) for details

## Course Overview

This course explores the concepts and algorithms at the foundation of modern artificial intelligence, diving into the ideas that give rise to technologies like game-playing engines, handwriting recognition, and machine translation. Through hands-on projects, students gain exposure to the theory behind graph search algorithms, classification, optimization, reinforcement learning, and other topics in artificial intelligence and machine learning as they incorporate them into their own Python programs. By course’s end, students emerge with experience in libraries for machine learning as well as knowledge of artificial intelligence principles that enable them to design intelligent systems of their own

### Artificial Intelligence

Artificial Intelligence (AI) covers a range of techniques that appear as sentient behavior by the computer. For example, AI is used to recognize faces in photographs on your social media, beat the World’s Champion in chess, and process your speech when you speak to Siri or Alexa on your phone. This course will explore some of the ideas that make AI possible

- **[Search](#lecture-0---search)**: Finding a solution to a problem, like a navigator app that finds the best route from your origin to the destination, or like playing a game and figuring out the next move
- **[Knowledge](#lecture-1---knowledge)**: Representing information and drawing inferences from it
- **[Uncertainty](#lecture-2---uncertainty)**: Dealing with uncertain events using probability
- **[Optimization](#lecture-3---optimization)**: Finding not only a correct way to solve a problem, but a better—or the best—way to solve it
- **[Learning](#lecture-4---learning)**: Improving performance based on access to data and experience. For example, your email is able to distinguish spam from non-spam mail based on past experience
- **[Neural Networks](#lecture-5---neural-networks)**: A program structure inspired by the human brain that is able to perform tasks effectively
- **[Language](#lecture-6---language)**: Processing natural language, which is produced and understood by humans

## Get Started

- To setup the environment on your device, please follow the guide in [docs](docs/)
- To practice doing projects, check all the projects with their specifications in [DIY](DIY/)

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

Last lecture shows how AI can represent knowledge and from that, derive new knowledge. But in reality, usually we don't have that much knowledge for certain. In fact, most of the times AI can only have partial knowledge and leaving some space for uncertainty. Still, we would want the AI to make the best possible decision during these situations

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

## Lecture 4 - [Learning](4.Learning/)

Machine learning provides a computer with data, rather than explicit instructions. Using these data, the computer learns to recognize patterns and becomes able to execute tasks on its own

### Objectives

- Supervised Learning
- Reinforcement Learning
- Unsupervised Learning

### Projects

- [Shopping](4.Learning/shopping/)
- [Nim](4.Learning/nim/)

## Lecture 5 - [Neural Networks](5.Neural_Networks/)

AI neural networks are inspired by neuroscience. In the brain, neurons are cells that are connected to each other, forming networks. Each neuron is capable of both receiving and sending electrical signals. Once the electrical input that a neuron receives crosses some threshold, the neuron activates, thus sending its electrical signal forward

### Objectives

- Structure and Algorithms
- Computer Vision
- Recurrent Neural Networks

### Projects

- [Traffic](5.Neural_Networks/traffic/)

## Lecture 6 - [Language](6.Language/)

Natural Language Processing spans all tasks where the AI gets human language as input. It can be challenging since natural languages have complex syntax and are sometimes ambiguous

### Objectives

- Syntax
- Bayes & TF-IDF
- Semantics

### Projects

- [Parser](6.Language/parser/)
- [Questions](6.Language/questions/)

## Contact ME

If you have any questions regarding the course material or any of the projects, please feel free to contact me through my emails <kevintian.li@mail.utoronto.ca> or <kevin.li20021106@gmail.com>
