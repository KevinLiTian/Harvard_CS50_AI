## Specification

Complete the implementations of `joint_probability`, `update`, and `normalize`

The `joint_probability` function should take as input a dictionary of people, along with data about who has how many copies of each of the genes, and who exhibits the trait. The function should return the joint probability of all of those events taking place

- The function accepts four values as input: `people`, `one_gene`, `two_genes`, and `have_trait`
  - `people` is a dictionary of people as described in the “Understanding” section. The keys represent names, and the values are dictionaries that contain mother and father keys. You may assume that either `mother` and `father` are both blank (no parental information in the data set), or `mother` and `father` will both refer to other `people` in the people dictionary
  - `one_gene` is a set of all people for whom we want to compute the probability that they have one copy of the gene
  - `two_genes` is a set of all people for whom we want to compute the probability that they have two copies of the gene.
  - `have_trait` is a set of all people for whom we want to compute the probability that they have the trait
  - For any person not in `one_gene` or `two_genes`, we would like to calculate the probability that they have no copies of the gene; and for anyone not in `have_trait`, we would like to calculate the probability that they do not have the trait
- For example, if the family consists of Harry, James, and Lily, then calling this function where `one_gene = {"Harry"}`, `two_genes = {"James"}`, and `trait = {"Harry", "James"}` should calculate the probability that Lily has zero copies of the gene, Harry has one copy of the gene, James has two copies of the gene, Harry exhibits the trait, James exhibits the trait, and Lily does not exhibit the trait
- For anyone with no parents listed in the data set, use the probability distribution `PROBS["gene"]` to determine the probability that they have a particular number of the gene
- For anyone with parents in the data set, each parent will pass one of their two genes on to their child randomly, and there is a `PROBS["mutation"]` chance that it mutates (goes from being the gene to not being the gene, or vice versa)
- Use the probability distribution `PROBS["trait"]` to compute the probability that a person does or does not have a particular trait

The `update` function adds a new joint distribution probability to the existing probability distributions in `probabilities`

- The function accepts five values as input: `probabilities`, `one_gene`, `two_genes`, `have_trait`, and `p`
  - `probabilities` is a dictionary of people as described in the “Understanding” section. Each person is mapped to a `"gene"` distribution and a `"trait"` distribution
  - `one_gene` is a set of people with one copy of the gene in the current joint distribution
  - `two_genes` is a set of people with two copies of the gene in the current joint distribution
  - `have_trait` is a set of people with the trait in the current joint distribution
  - `p` is the probability of the joint distribution.
- For each person `person` in `probabilities`, the function should update the `probabilities[person]["gene"]` distribution and `probabilities[person]["trait"]` distribution by adding `p` to the appropriate value in each distribution. All other values should be left unchanged
- For example, if `"Harry"` were in both `two_genes` and in `have_trait`, then `p` would be added to `probabilities["Harry"]["gene"][2]` and to `probabilities["Harry"]["trait"][True]`.
- The function should not return any value: it just needs to update the `probabilities` dictionary

The `normalize` function updates a dictionary of probabilities such that each probability distribution is normalized (i.e., sums to 1, with relative proportions the same)

- The function accepts a single value: `probabilities`.
  - `probabilities` is a dictionary of people as described in the “Understanding” section. Each person is mapped to a `"gene"` distribution and a `"trait"` distribution.
- For both of the distributions for each person in `probabilities`, this function should normalize that distribution so that the values in the distribution sum to 1, and the relative values in the distribution are the same
- For example, if `probabilities["Harry"]["trait"][True]` were equal to `0.1` and `probabilities["Harry"]["trait"][False]` were equal to `0.3`, then your function should update the former value to be `0.25` and the latter value to be `0.75`: the numbers now sum to 1, and the latter value is still three times larger than the former value.
- The function should not return any value: it just needs to update the `probabilities` dictionary

You should not modify anything else in `heredity.py` other than the three functions the specification calls for you to implement, though you may write additional functions and/or import other Python standard library modules. You may also import `numpy` or `pandas`, if familiar with them, but you should not use any other third-party Python modules

## Example Joint Probability

To help you think about how to calculate joint probabilities, we’ve included below an example

Consider the following value for `people`:

```
{
  'Harry': {'name': 'Harry', 'mother': 'Lily', 'father': 'James', 'trait': None},
  'James': {'name': 'James', 'mother': None, 'father': None, 'trait': True},
  'Lily': {'name': 'Lily', 'mother': None, 'father': None, 'trait': False}
}
```

We will here show the calculation of `joint_probability(people, {"Harry"}, {"James"}, {"James"})`. Based on the arguments, `one_gene` is `{"Harry"}`, `two_genes` is `{"James"}`, and `has_trait` is `{"James"}`. This therefore represents the probability that: Lily has 0 copies of the gene and does not have the trait, Harry has 1 copy of the gene and does not have the trait, and James has 2 copies of the gene and does have the trait

We start with Lily (the order that we consider people does not matter, so long as we multiply the correct values together, since multiplication is commutative). Lily has 0 copies of the gene with probability `0.96` (this is `PROBS["gene"][0]`). Given that she has 0 copies of the gene, she doesn’t have the trait with probability `0.99` (this is `PROBS["trait"][0][False]`). Thus, the probability that she has 0 copies of the gene and she doesn’t have the trait is `0.96 \* 0.99 = 0.9504`

Next, we consider James. James has 2 copies of the gene with probability `0.01` (this is `PROBS["gene"][2]`). Given that he has 2 copies of the gene, the probability that he does have the trait is `0.65`. Thus, the probability that he has 2 copies of the gene and he does have the trait is `0.01 \* 0.65 = 0.0065`

Finally, we consider Harry. What’s the probability that Harry has 1 copy of the gene? There are two ways this can happen. Either he gets the gene from his mother and not his father, or he gets the gene from his father and not his mother. His mother Lily has 0 copies of the gene, so Harry will get the gene from his mother with probability `0.01` (this is `PROBS["mutation"]`), since the only way to get the gene from his mother is if it mutated; conversely, Harry will not get the gene from his mother with probability 0.99. His father James has 2 copies of the gene, so Harry will get the gene from his father with probability `0.99` (this is `1 - PROBS["mutation"]`), but will get the gene from his mother with probability `0.01` (the chance of a mutation). Both of these cases can be added together to get `0.99 _ 0.99 + 0.01 _ 0.01 = 0.9802`, the probability that Harry has 1 copy of the gene.

Given that Harry has 1 copy of the gene, the probability that he does not have the trait is `0.44` (this is `PROBS["trait"][1][False]`). So the probability that Harry has 1 copy of the gene and does not have the trait is `0.9802 \* 0.44 = 0.431288`

Therefore, the entire joint probability is just the result of multiplying all of these values for each of the three people: `0.9504 _ 0.0065 _ 0.431288 = 0.0026643247488`

## Hints

- Recall that to compute a joint probability of multiple events, you can do so by multiplying those probabilities together. But remember that for any child, the probability of them having a certain number of genes is conditional on what genes their parents have
