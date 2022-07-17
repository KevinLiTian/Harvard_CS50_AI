# Vectors

A sophisticated way to represent meanings of words is by representing words using vectors

## How to Use

In the `vectors` directory, use the command `python` to open up `Python Shell`

Use `from vectors import *` to get the data and all helper functions in `vectors.py`

To check the vector a of word, for example "city", use `words["city"]`

To check the distance between two word vectors, use `distance(words["book"], words["book"])`. This example should give a result of 0 since they are the same word and thus have the same vector.

To test out how well the vectors can represent the meaning of the words, we can use the following code:

```Python
>>> distance(words["book"], words["novel"])
0.3436623421719047

>>> distance(words["book"], words["breakfast"])
0.6351827719357863

>>> distance(words["breakfast"], words["lunch"])
0.2006302059301045
```

We can see that words that have similar meanings generally have shorter distance in the vector space, which means this vector representation of words is quite powerful

We can also find the words that are closest in vector space given a word using:

```Python
>>> closest_words(words["book"])
['book', 'books', 'essay', 'memoir', 'essays', 'novella', 'anthology', 'blurb', 'autobiography', 'audiobook']

>>> closest_words(words["city"])
['city', 'town', 'township', 'village', 'borough', 'the', 'residents', 'area', 'metropolitan', 'population']
```

The most interesting part is that because words are represented by vectors, we are able to do mathematics with them. It may sounds nonsense since how can word plus word work? But they are nothing but vectors and vectors can do plus and minus and all that

```Python
>>> closest_word(words["king"] - words["man"] + words["woman"])
'queen'
```
