# Uncertainty

Uncertainty can be represented as a number of events and the likelihood, or probability, of each of them happening. An AI should be able to make predictions even if events are not certain

## Probability

### Possible Worlds

Every possible situation can be thought of as a world, represented by the lowercase Greek letter omega ω. For example, rolling a die can result in six possible worlds: a world where the die yields a 1, a world where the die yields a 2, and so on. To represent the probability of a certain world, we write P(ω) where w is a certain world and P is the probability of that world taking place

### Axioms in Probability

Every value representing probability must range between 0 and 1. The probabilities of every possible event, when summed together, are equal to 1

### Unconditional Probability

Unconditional probability is the degree of belief in a proposition in the absence of any other evidence. For instance, the results of rolling a die in a row is unconditional because a roll of die is not dependent on previous rolls

### Conditional Probability

Conditional probability is the degree of belief in a proposition given some evidence that has already been revealed. For instance, children's gene is conditional since it is dependent on their parents' genes

### Bayes's Rule

Bayes’ rule is commonly used in probability theory to compute conditional probability. In words, Bayes’ rule says that the probability of b given a is equal to the probability of a given b, times the probability of b, divided by the probability of a

<img src="https://user-images.githubusercontent.com/99038613/176779929-785a9a47-bfcf-44bd-9cb4-5043e5ef8275.jpg" width="60%" height="60%">

### Joint Probability

Joint probability is the likelihood of multiple events all occurring, and the probability can be calculated as the multiplication of the probabilities of each single event taking place

### Probability Rules

- **Negation**: P(¬a) = 1 - P(a)
- **Inclusion-Exclusion**: P(a ∨ b) = P(a) + P(b) - P(a ∧ b)
- **Marginalization**: P(a) = P(a, b) + P(a, ¬b)
- **Conditioning**: P(a) = P(a | b)P(b) + P(a | ¬b)P(¬b)

### Independence

Independence is the knowledge that the occurrence of one event does not affect the probability of the other event. For instance, rolling a die twice in a row, the first roll and the second roll is independent of each other

## Random Variables

A random variable is a variable in probability theory with a domain of possible values that it can take on. For instance, a random variable can be a roll, and it can take on values from 1 to 6 with even probabilities

### [Bayesian Networks](https://www.bayesfusion.com/bayesian-networks/)

A Bayesian network is a data structure that represents the dependencies among random variables

<img src="https://user-images.githubusercontent.com/99038613/176780156-0c407208-1fab-4106-baf0-27e43510820b.jpg" width="60%" height="60%">

### Inference

In the last lecture, the AI makes inferences using knowledge through entailments. The AI can also make inferences using probabilities

### Inference by Enumeration

Inference by enumeration is a process of finding the probability distribution of variable X given observed evidence e and some hidden variables Y

## Sampling

Sampling is one technique of approximate inference by letting the AI simute the process of selection based on given probabilities

### [Likelihood Weighting](https://en.wikipedia.org/wiki/Likelihood_function)

Normal sampling will discard samples we don't need for certain queries, that is inefficient. Likelihood weighting is a way to get around these situations

### [Markov Models](https://en.wikipedia.org/wiki/Markov_model)

To be able to predict events in the future, we will use Markov Models

#### The Markov Assumption

The Markov assumption is an assumption that the current state depends on only a finite fixed number of previous states in order not have to store or use too many data

### Markov Chain

A Markov chain is a sequence of random variables where the distribution of each variable follows the Markov assumption. That is, each event in the chain occurs based on the probability of the event before it

To start constructing a Markov chain, we need a transition model that will specify the the probability distributions of the next event based on the possible values of the current event

<img src="https://user-images.githubusercontent.com/99038613/179137384-8090b40a-940d-4605-8461-0052312a75a6.jpg" width=60%>

In this example, the probability of tomorrow being sunny based on today being sunny is 0.8. This is reasonable, because it is more likely than not that a sunny day will follow a sunny day. However, if it is rainy today, the probability of rain tomorrow is 0.7, since rainy days are more likely to follow each other. Using this transition model, it is possible to sample a Markov chain. Start with a day being either rainy or sunny, and then sample the next day based on the probability of it being sunny or rainy given the weather today. Then, condition the probability of the day after tomorrow based on tomorrow, and so on, resulting in a Markov chain:

![3](https://user-images.githubusercontent.com/99038613/179137478-9f3f7b58-d331-404e-bbe9-3c28aaf5a826.jpg)

### Hidden Markov Models

A hidden Markov model is a type of a Markov model for a system with hidden states that generate some observed event

### Sensor Markov Assumption

The assumption that the evidence variable depends only on the corresponding state

## Examples

Check out some [examples](examples/) that practice these theories
