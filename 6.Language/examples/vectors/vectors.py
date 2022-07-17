""" Word Vectors """

from scipy.spatial.distance import cosine

import numpy as np

with open("words.txt", encoding='utf-8') as f:
    words = dict()
    for i in range(50000):
        row = next(f).split()
        word = row[0]
        vector = np.array([float(x) for x in row[1:]])
        words[word] = vector


def distance(w1, w2):
    """ Calculate the distance between two vectors using COS """
    return cosine(w1, w2)


def closest_words(embedding):
    """ The closest words regarding the vector distance """
    distances = {
        w: distance(embedding, words[w])
        for w in words
    }
    return sorted(distances, key=lambda w: distances[w])[:10]


def closest_word(embedding):
    """ The closest word regarding the vector distance """
    return closest_words(embedding)[0]
