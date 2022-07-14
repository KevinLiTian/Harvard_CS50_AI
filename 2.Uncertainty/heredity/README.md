# Heredity

An AI that assess the likelihood that a person will have a particular genetic trait

## Background

Mutated versions of the [GJB2 gene](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1285178/) are one of the leading causes of hearing impairment in newborns. Each person carries two versions of the gene, so each person has the potential to possess either 0, 1, or 2 copies of the hearing impairment version GJB2. Unless a person undergoes genetic testing, though, it’s not so easy to know how many copies of mutated GJB2 a person has. This is some “hidden state”: information that has an effect that we can observe (hearing impairment), but that we don’t necessarily directly know. After all, some people might have 1 or 2 copies of mutated GJB2 but not exhibit hearing impairment, while others might have no copies of mutated GJB2 yet still exhibit hearing impairment

Every child inherits one copy of the GJB2 gene from each of their parents. If a parent has two copies of the mutated gene, then they will pass the mutated gene on to the child; if a parent has no copies of the mutated gene, then they will not pass the mutated gene on to the child; and if a parent has one copy of the mutated gene, then the gene is passed on to the child with probability 0.5. After a gene is passed on, though, it has some probability of undergoing additional mutation: changing from a version of the gene that causes hearing impairment to a version that doesn’t, or vice versa

We can attempt to model all of these relationships by forming a Bayesian Network of all the relevant variables, as in the one below, which considers a family of two parents and a single child

<p align="center">
<img src="https://user-images.githubusercontent.com/99038613/175829745-becb1b5c-38da-454e-93f0-577da199075e.jpg" width="60%" height="60%">
</p>

Each person in the family has a Gene random variable representing how many copies of a particular gene (e.g., the hearing impairment version of GJB2) a person has: a value that is 0, 1, or 2. Each person in the family also has a Trait random variable, which is yes or no depending on whether that person expresses a trait (e.g., hearing impairment) based on that gene. There’s an arrow from each person’s Gene variable to their Trait variable to encode the idea that a person’s genes affect the probability that they have a particular trait. Meanwhile, there’s also an arrow from both the mother and father’s Gene random variable to their child’s Gene random variable: the child’s genes are dependent on the genes of their parents

Your task in this project is to use this model to make inferences about a population. Given information about people, who their parents are, and whether they have a particular observable trait (e.g. hearing loss) caused by a given gene, your AI will infer the probability distribution for each person’s genes, as well as the probability distribution for whether any person will exhibit the trait in question

## Files

There are three datasets in the `data` directory, which are three family relationships and genetic traits.
And in the `heredity.py` file, there are some probability constants and we are to use them and the dataset to infer the probability distribution of which family member has certain genetic traits. The `testcase.py` contains a unit test test case that is provided as an example in the course's project description. One can use this to confirm the functionality of the `joint_probability` function in `heredity.py`

## How to Use

One can use either the existing data in the `data` directory or custom data. If using custom data, one should be familiar with the format of the data and added into the `data` directory. Run this command in the `heredity` directory to get the probability distribution for genetic traits

`python heredity.py data/dataname`

Where dataname is the name of the data file in the `data` directory

If one wants to run the unit test `testcase.py`, use the command

`python testcase.py`

## Example Output

```shell
$ python heredity.py data/family0.csv
Harry:
  Gene:
    2: 0.0092
    1: 0.4557
    0: 0.5351
  Trait:
    True: 0.2665
    False: 0.7335
James:
  Gene:
    2: 0.1976
    1: 0.5106
    0: 0.2918
  Trait:
    True: 1.0000
    False: 0.0000
Lily:
  Gene:
    2: 0.0036
    1: 0.0136
    0: 0.9827
  Trait:
    True: 0.0000
    False: 1.0000
```
