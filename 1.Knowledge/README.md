## Definitions

#### [Knowledge-Based Agents](https://www.geeksforgeeks.org/knowledge-based-agents-in-ai/)

These are agents that reason by operating on internal representations of knowledge

#### Sentence

An assertion about the world in a knowledge representation language. A sentence is how AI stores knowledge and uses it to infer new information

#### [Propositional Logic](https://iep.utm.edu/prop-log/#:~:text=Propositional%20logic%2C%20also%20known%20as%20sentential%20logic%2C%20is%20that%20branch,common%20way%20of%20combining%20statements.)

##### Propositional Symbols

Used to represent an assertion in reality

- [Logical Connectives](https://en.wikipedia.org/wiki/Logical_connective): Logical connectives are logical symbols that connect propositional symbols in order to reason in a more complex way about the world
  - NOT (¬): Inverses the truth value of the proposition
  - AND (∧): When two proposition, P and Q, are connected by ∧, the resulting proposition P ∧ Q is true only in the case that both P and Q are true
  - OR (∨): True as as long as either of its arguments is true. This means that for P ∨ Q to be true, at least one of P or Q has to be true
  - XOR (⊕): Exclusive OR, true if and only if one of P or Q is true
  - Implication (→): Represents a structure of “if P then Q.”
  - Biconditional (⇔): Implication that goes both directions
- Model: Provides information about the world based on existing sentences which also known as the Knowledge Base
- Knowledge Base (KB): The combination of all existing sentences
- Entailment (⊨): If If α ⊨ β (α entails β), then in any possible world where α is true, then β must be true
- Knowledge Engineering: The process of figuring out how to represent propositions and logic in AI.
- [Inference](https://en.wikipedia.org/wiki/Inference): The process of deriving new sentences from old ones
  - Inference Rules
    - Modus Ponens: If we know an implication and its antecedent is true, then the consequent must also be true
    - And Elimination: If an AND proposition is true, then any one atomic proposition within it must also be true
    - Double Negation Elimination: A proposition that is negated twice is true
    - Implication Elimination: An implication is equivalent to an OR relation between the negated antecedent and the consequent
    - Biconditional Elimination:A biconditional proposition is equivalent to an implication and its inverse with an And connective
    - De Morgan's Law: Turning AND connective to OR or vice versa
    - Distributive Property: AND and OR can be distributed just like multiplication
    - Knowledge and Search: Inference can be viewed as a search problem. The initial state is the starting KB, the actions are inference rules and inferencing, the goal is a statement we are trying to prove
- Resolution: A power inference rule that states that if one of two atomic propositions in an OR proposition is false, the other has to be true
  - Complimentary Literals: Two of the same atomic propositions where one is negated and the other is not, such as P and ¬P
  - Clause: A disjunction of literals (a propositional symbol or a negation of a propositional symbol, such as P, ¬P)
  - Disjunction: Consists of propositions that are connected with an Or logical connective (P ∨ Q ∨ R)
  - Conjunction: Consists of propositions that are connected with an And logical connective (P ∧ Q ∧ R)
  - Conjunctive Normal Form (CNF): A conjunction of clauses
  - Empty Clause: Resolving complimentary literals will result in the empty clause which is always of value false
- [First Order Logic](https://www.javatpoint.com/first-order-logic-in-artificial-intelligence)
  - Universal Quantification: Universal quantification uses the symbol ∀ to express “for all.”
  - Existential Quantification: Existential quantification is used to create sentences that are true for at least one x. It is expressed using the symbol ∃
