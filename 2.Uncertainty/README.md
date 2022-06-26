- Probability: Uncertainty can be represented as a number of events and the likelihood, or probability, of each of them happening
  - Possible Worlds: Every possible situation can be thought of as a world, represented by the lowercase Greek letter omega ω. For example, rolling a die can result in six possible worlds: a world where the die yields a 1, a world where the die yields a 2, and so on. To represent the probability of a certain world, we write P(ω)
  - Axioms in Probability: Every value representing probability must range between 0 and 1. The probabilities of every possible event, when summed together, are equal to 1
  - Unconditional Probability: Unconditional probability is the degree of belief in a proposition in the absence of any other evidence. All the questions that we have asked so far were questions of unconditional probability, because the result of rolling a die is not dependent on previous events.
- Conditional Probability: Conditional probability is the degree of belief in a proposition given some evidence that has already been revealed
- Random Variables: A random variable is a variable in probability theory with a domain of possible values that it can take on
  - Independence: Independence is the knowledge that the occurrence of one event does not affect the probability of the other event
- Bayes's Rule: Bayes’ rule is commonly used in probability theory to compute conditional probability
- Joint Probability: Joint probability is the likelihood of multiple events all occurring
- Probability Rules
  - Negation: P(¬a) = 1 - P(a)
  - Inclusion-Exclusion: P(a ∨ b) = P(a) + P(b) - P(a ∧ b)
  - Marginalization: P(a) = P(a, b) + P(a, ¬b)
  - Conditioning: P(a) = P(a | b)P(b) + P(a | ¬b)P(¬b)
- Bayesian Networks: A Bayesian network is a data structure that represents the dependencies among random variables
  - Inference: In the last lecture, the AI makes inferences using knowledge through entailments. The AI can also make inferences using probabilities
  - Inference by Enumeration: Inference by enumeration is a process of finding the probability distribution of variable X given observed evidence e and some hidden variables Y
- Sampling: Sampling is one technique of approximate inference
  - Likelihood Weighting: Normal sampling will discard samples we don't need for certain queries, that is inefficient. Likelihood weighting is a way to get around these situations
- Markov Models
  - The Markov Assumption: The Markov assumption is an assumption that the current state depends on only a finite fixed number of previous states
  - Markov Chain: A Markov chain is a sequence of random variables where the distribution of each variable follows the Markov assumption
- Hidden Markov Models: A hidden Markov model is a type of a Markov model for a system with hidden states that generate some observed event
  - Sensor Markov Assumption: The assumption that the evidence variable depends only on the corresponding state