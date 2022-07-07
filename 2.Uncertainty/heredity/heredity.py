""" An AI that assess the likelihood that a person will have a particular genetic trait """

import csv
import itertools
import sys


PROBS = {

    # Unconditional probabilities for having gene
    "gene": {
        2: 0.01,
        1: 0.03,
        0: 0.96
    },

    "trait": {

        # Probability of trait given two copies of gene
        2: {
            True: 0.65,
            False: 0.35
        },

        # Probability of trait given one copy of gene
        1: {
            True: 0.56,
            False: 0.44
        },

        # Probability of trait given no gene
        0: {
            True: 0.01,
            False: 0.99
        }
    },

    # Mutation probability
    "mutation": 0.01
}


def main():
    """ Main Function
    Takes in arugments from command line and determines which dataset
    will be used. Then initiate a probabilities dictionary and update
    using joint probabilities. Returns the probability of each person's
    gene and trait
    """
    # Check for proper usage
    if len(sys.argv) != 2:
        sys.exit("Usage: python heredity.py data.csv")
    people = load_data(sys.argv[1])

    # Keep track of gene and trait probabilities for each person
    probabilities = {
        person: {
            "gene": {
                2: 0,
                1: 0,
                0: 0
            },
            "trait": {
                True: 0,
                False: 0
            }
        }
        for person in people
    }

    # Loop over all sets of people who might have the trait
    names = set(people)
    for have_trait in powerset(names):

        # Check if current set of people violates known information
        fails_evidence = any(
            (people[person]["trait"] is not None and
             people[person]["trait"] != (person in have_trait))
            for person in names
        )
        if fails_evidence:
            continue

        # Loop over all sets of people who might have the gene
        for one_gene in powerset(names):
            for two_genes in powerset(names - one_gene):

                # Update probabilities with new joint probability
                prob = joint_probability(people, one_gene, two_genes, have_trait)
                update(probabilities, one_gene, two_genes, have_trait, prob)

    # Ensure probabilities sum to 1
    normalize(probabilities)

    # Print results
    for person in people:
        print(f"{person}:")
        for field in probabilities[person]:
            print(f"  {field.capitalize()}:")
            for value in probabilities[person][field]:
                prob = probabilities[person][field][value]
                print(f"    {value}: {prob:.4f}")


def load_data(filename):
    """
    Load gene and trait data from a file into a dictionary.
    File assumed to be a CSV containing fields name, mother, father, trait.
    mother, father must both be blank, or both be valid names in the CSV.
    trait should be 0 or 1 if trait is known, blank otherwise.
    """
    data = dict()
    with open(filename, encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            name = row["name"]
            data[name] = {
                "name": name,
                "mother": row["mother"] or None,
                "father": row["father"] or None,
                "trait": (True if row["trait"] == "1" else
                          False if row["trait"] == "0" else None)
            }
    return data


def powerset(input_set):
    """
    Return a list of all possible subsets of set s.
    """
    input_set = list(input_set)
    return [
        set(input_set) for input_set in itertools.chain.from_iterable(
            itertools.combinations(input_set, r) for r in range(len(input_set) + 1)
        )
    ]


def joint_probability(people, one_gene, two_genes, have_trait):
    """
    Compute and return a joint probability.

    The probability returned should be the probability that
        * everyone in set `one_gene` has one copy of the gene, and
        * everyone in set `two_genes` has two copies of the gene, and
        * everyone not in `one_gene` or `two_gene` does not have the gene, and
        * everyone in set `have_trait` has the trait, and
        * everyone not in set` have_trait` does not have the trait.
    """
    # Initialize the joint_probability as 100%, then for each event, times the probability
    # of the event taking place
    joint_prob = float(1)

    # For each family member, first set their properties using the
    # input parameters and use PROBS constants to determine what is
    # the joint probability of everything taking place
    for family_member in people:
        # Number of gene the family member has
        # Depending on which gene set the current family member is in
        num_gene = (
                    2 if family_member in two_genes else
                    1 if family_member in one_gene else
                    0
                   )

        # Trait of the family member depends on if in the have_trait set
        trait = family_member in have_trait

        # The parent of the family member given in the dataset
        father = people[family_member]["father"]
        mother = people[family_member]["mother"]
        parents = [father, mother]

        # Gene Probability
        # Determine whether the gene probability is conditional
        # or unconditional based on if the family member has parents
        gene_prob = float(1)

        # No parents, unconditional probability for gene
        if father is None and mother is None:
            gene_prob = PROBS["gene"][num_gene]
            joint_prob = joint_prob * gene_prob

        # Otherwise gene probability is conditional
        else:
            # The probability of each of the parent passing the gene
            parent_passing_prob = {}
            for parent in parents:
                # If a parent has 2 gene, the only situation
                # not passing the gene is when gene mutated
                if parent in two_genes:
                    parent_passing_prob[parent] = 1 - PROBS["mutation"]

                # If a parent has 1 gene, there will be 50% chance
                # of passing the gene to their decendant
                elif parent in one_gene:
                    parent_passing_prob[parent] = 0.5

                # If a parent has 0 gene, the only situation
                # passing the gene is through mutation
                else:
                    parent_passing_prob[parent] = PROBS["mutation"]

            # Depending how many gene the family member has, consider
            # the probability of which parents passed on to them

            # Both parents passed on the gene
            if num_gene == 2:
                gene_prob = parent_passing_prob[father] * parent_passing_prob[mother]

            # One of the parents passed on the gene
            # Father passed on but mother did not or vice versa
            elif num_gene == 1:
                gene_prob = parent_passing_prob[father] * (1 - parent_passing_prob[mother]) + \
                            parent_passing_prob[mother] * (1 - parent_passing_prob[father])

            # No parents passed on the gene
            else:
                gene_prob = (1 - parent_passing_prob[father]) * (1 - parent_passing_prob[mother])

            joint_prob = joint_prob * gene_prob

        # Trait Probability
        # Depending on the number of genes, get the probability
        # of whether having the trait or not
        trait_prob = PROBS["trait"][num_gene][trait]
        joint_prob = joint_prob * trait_prob

    return joint_prob

def update(probabilities, one_gene, two_genes, have_trait, prob):
    """
    Add to `probabilities` a new joint probability `p`.
    Each person should have their "gene" and "trait" distributions updated.
    Which value for each distribution is updated depends on whether
    the person is in `have_gene` and `have_trait`, respectively.
    """
    # For each family member, update the probability distribution depending on
    # the set they are in (number of genes, have trait or not)
    for family_member in probabilities:
        # Add the probability distribution to corresponding gene number
        num_gene = (
                    2 if family_member in two_genes else
                    1 if family_member in one_gene else
                    0
                   )

        probabilities[family_member]["gene"][num_gene] += prob

        # Add the probability distribution to the corresponding trait
        trait = family_member in have_trait
        probabilities[family_member]["trait"][trait] += prob

def normalize(probabilities):
    """
    Update `probabilities` such that each probability distribution
    is normalized (i.e., sums to 1, with relative proportions the same).
    """
    # For each properties for each family member (gene, trait)
    # find the normalizing factor by using 1 / sum and times
    # every probability distribution by this factor
    for family_member in probabilities:
        for properties in probabilities[family_member]:
            factor = 1.0 / sum(probabilities[family_member][properties].values())
            for var in probabilities[family_member][properties]:
                probabilities[family_member][properties][var] *= factor


if __name__ == "__main__":
    main()
