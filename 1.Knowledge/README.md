# Knowledge

Instead of randomly taking actions and finding the optimal series of actions, with some knowledge about the world, the AI will make inferences and entailments to prove a statement

### [Knowledge-Based Agents](https://www.geeksforgeeks.org/knowledge-based-agents-in-ai/)

Similar to the previous agent definition, but knowledge-based agents are agents that reason and infer by operating on internal representations of knowledge instead of taking actions under states

### Sentence

Sentence is an assertion about the world in a knowledge representation language. A sentence is how AI stores knowledge and uses it to infer new information

## [Propositional Logic](https://iep.utm.edu/prop-log/#:~:text=Propositional%20logic%2C%20also%20known%20as%20sentential%20logic%2C%20is%20that%20branch,common%20way%20of%20combining%20statements.)

Propositional logic, also known as sentential logic, is that branch of logic that studies ways of combining or altering statements or propositions to form more complicated statements or propositions. Joining two simpler propositions with the word “and” is one common way of combining statements

### Propositional Symbols

Propositional symbols are used to represent an assertion in reality

### [Logical Connectives](https://en.wikipedia.org/wiki/Logical_connective)

Logical connectives are logical symbols that connect propositional symbols in order to reason in a more complex way about the world

- **NOT (¬)**: Inverses the truth value of the proposition
- **AND (∧)**: When two proposition, P and Q, are connected by ∧, the resulting proposition P ∧ Q is true only in the case that both P and Q are true
- **OR (∨)**: True as as long as either of its arguments is true. This means that for P ∨ Q to be true, at least one of P or Q has to be true
- **XOR (⊕)**: Exclusive OR, true if and only if one of P or Q is true
- **Implication (→)**: Represents a structure of “if P then Q.”
- **Biconditional (⇔)**: Implication that goes both directions

### Model

Provides information about the world based on existing sentences which also known as the Knowledge Base (KB). Input a query about the world into the model, it will output its best result based on the KB

### Knowledge Base (KB)

The combination of all existing sentences, where the knowledge-based agents store all their knowledge

### Entailment (⊨)

If α ⊨ β (α entails β), then in any possible world where α is true, then β must be true. For example, if there are two statements:

- "Harry will go outside if it is raining"
- "It is raining"

Then the AI is able to make entailment stating that "Harry is outside" based on these two sentences

### Knowledge Engineering

The process of figuring out how to represent propositions and logic using programming. For instance, in the `Knights` project, the `logic.py` is fully implemented already to represent propositional logics with Python

## [Inference](https://en.wikipedia.org/wiki/Inference)

The process of deriving new sentences from old ones

### Inference Rules

- **Modus Ponens**: If we know an implication and its antecedent is true, then the consequent must also be true. If a → b is true, and a is true, then b must be true
- **And Elimination**: If an AND proposition is true, then any one atomic proposition within it must also be true. If (a ∧ b) is true, then a, b must all be true
- **Double Negation Elimination**: A proposition that is negated twice is true. If (¬)(¬a) is true, then a must be true
- **Implication Elimination**: An implication is equivalent to an OR relation between the negated antecedent and the consequent

    <img src="https://user-images.githubusercontent.com/99038613/176773992-c88872d1-9a8b-497c-af92-8019c929ba0a.jpg" width="60%" height="60%">

- **Biconditional Elimination**:A biconditional proposition is equivalent to an implication and its inverse with an And connective

    <img src="https://user-images.githubusercontent.com/99038613/176774268-caea480b-47b2-4eb0-9b10-1307353de97b.jpg" width="60%" height="60%">

- **De Morgan's Law**: Turning AND connective to OR or vice versa

    <img src="https://user-images.githubusercontent.com/99038613/176774450-ccc7b58c-c6b3-47f4-960b-364a64146dfe.jpg" width="60%" height="60%">

    <img src="https://user-images.githubusercontent.com/99038613/176774456-b2f0f3b9-0f62-4efe-ba3f-ebe4dff0ed31.jpg" width="60%" height="60%">

- **Distributive Property**: AND and OR can be distributed just like multiplication. If a ∨ (b ∧ c) is true, then (a ∨ b) ∧ (a ∨ c) must be true

### Knowledge and Search

Inference can be viewed as a search problem. The initial state is the starting KB, the actions are inference rules and inferencing, the goal is a statement we are trying to prove

### Resolution

A power inference rule that states that if one of two atomic propositions in an OR proposition is false, the other has to be true

- **Complimentary Literals**: Two of the same atomic propositions where one is negated and the other is not, such as P and ¬P
- **Clause**: A disjunction of literals (a propositional symbol or a negation of a propositional symbol, such as P, ¬P)
- **Disjunction**: Consists of propositions that are connected with an Or logical connective (P ∨ Q ∨ R)
- **Conjunction**: Consists of propositions that are connected with an And logical connective (P ∧ Q ∧ R)
- **Conjunctive Normal Form (CNF)**: A conjunction of clauses
- **Empty Clause**: Resolving complimentary literals will result in the empty clause which is always of value false

## [First Order Logic](https://www.javatpoint.com/first-order-logic-in-artificial-intelligence)

First order logic is another type of logic that allows us to express more complex ideas more succinctly than propositional logic. First order logic uses two types of symbols: Constant Symbols and Predicate Symbols. Constant symbols represent objects, while predicate symbols are like relations or functions that take an argument and return a true or false value

For example, we return to the logic puzzle with different people and house assignments at Hogwarts. The constant symbols are people or houses, like Minerva, Pomona, Gryffindor, Hufflepuff, etc. The predicate symbols are properties that hold true or false of some constant symbols. For example, we can express the idea that Minerva is a person using the sentence Person(Minerva). Similarly, we can express the idea the Gryffindor is a house using the sentence House(Gryffindor). All the logical connectives work in first order logic the same way as before. For example, ¬House(Minerva) expresses the idea that Minerva is not a house. A predicate symbol can also take two or more arguments and express a relation between them. For example, BelongsTo expresses a relation between two arguments, the person and the house to which the person belongs. Thus, the idea that Minerva belongs to Gryffindor can be expressed as BelongsTo(Minerva, Gryffindor). First order logic allows having one symbol for each person and one symbol for each house. This is more succinct than propositional logic, where each person—house assignment would require a different symbol

### Universal Quantification

Quantification is a tool that can be used in first order logic to represent sentences without using a specific constant symbol. Universal quantification uses the symbol ∀ to express “for all.” So, for example, the sentence ∀x. BelongsTo(x, Gryffindor) → ¬BelongsTo(x, Hufflepuff) expresses the idea that it is true for every symbol that if this symbol belongs to Gryffindor, it does not belong to Hufflepuff.

### Existential Quantification

Existential quantification is an idea parallel to universal quantification. However, while universal quantification was used to create sentences that are true for all x, existential quantification is used to create sentences that are true for at least one x. It is expressed using the symbol ∃. For example, the sentence ∃x. House(x) ∧ BelongsTo(Minerva, x) means that there is at least one symbol that is both a house and that Minerva belongs to it. In other words, this expresses the idea that Minerva belongs to a house.

Existential and universal quantification can be used in the same sentence. For example, the sentence ∀x. Person(x) → (∃y. House(y) ∧ BelongsTo(x, y)) expresses the idea that if x is a person, then there is at least one house, y, to which this person belongs. In other words, this sentence means that every person belongs to a house.

There are other types of logic as well, and the commonality between them is that they all exist in pursuit of representing information. These are the systems we use to represent knowledge in our AI

## Examples

Check out some [examples](examples/) that practice these theories
