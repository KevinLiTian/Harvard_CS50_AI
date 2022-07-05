""" An AI that replies to queries using tf-idf """

import os
import sys
import string
import math

import nltk

FILE_MATCHES = 1
SENTENCE_MATCHES = 1


def main():
    """ Main Function
    Load data from second command line argument
    Tokenize each file and sentences
    Calculate idfs of each word, then use tf*idf
    to determine the importance of words
    Based on that, reply the sentence with the most important words
    """
    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python questions.py corpus")

    # Calculate IDF values across files
    files = load_files(sys.argv[1])
    file_words = {
        filename: tokenize(file)
        for filename, file in files.items()
    }
    file_idfs = compute_idfs(file_words)

    # Prompt user for query
    query = set(tokenize(input("Query: ")))

    # Determine top file matches according to TF-IDF
    filenames = top_files(query, file_words, file_idfs, top_n=FILE_MATCHES)

    # Extract sentences from top files
    sentences = {}
    for filename in filenames:
        for passage in files[filename].split("\n"):
            for sentence in nltk.sent_tokenize(passage):
                tokens = tokenize(sentence)
                if tokens:
                    sentences[sentence] = tokens

    # Compute IDF values across sentences
    idfs = compute_idfs(sentences)

    # Determine top sentence matches
    matches = top_sentences(query, sentences, idfs, top_n=SENTENCE_MATCHES)
    for match in matches:
        print(match)


def load_files(directory):
    """
    Given a directory name, return a dictionary mapping the filename of each
    `.txt` file inside that directory to the file's contents as a string.
    """
    fname_string = {}
    # Read from each .txt file in the directory
    # Map each file name to the string read from the file
    for fname in os.listdir(directory):
        with open(os.path.join(directory, fname), encoding='utf-8') as file:
            fname_string[fname] = file.read()

    return fname_string


def tokenize(document):
    """
    Given a document (represented as a string), return a list of all of the
    words in that document, in order.

    Process document by coverting all words to lowercase, and removing any
    punctuation or English stopwords.
    """
    # Lowercase the sentence
    document = document.lower()

    # Tokenize each element in the sentence
    word_list = nltk.word_tokenize(document)

    # Filter out punctions and stopwords (common words that are unlikely to be useful)
    word_list = [word for word in word_list
                if word not in string.punctuation and
                word not in nltk.corpus.stopwords.words("english")]

    return word_list


def compute_idfs(documents):
    """
    Given a dictionary of `documents` that maps names of documents to a list
    of words, return a dictionary that maps words to their IDF values.

    Any word that appears in at least one of the documents should be in the
    resulting dictionary.
    """
    # Dict format: {word: [filenames it appears in]}
    word_appearance = {}

    # Iterate each document and each word inside the document
    # Append the filename the word appeared in to a list mapped by word
    for document in documents:
        for word in documents[document]:
            # If the word never appeared, create it and append current filename
            if word not in word_appearance:
                word_appearance[word] = []
                word_appearance[word].append(document)

            # Or if this is the first time the word appears in current file
            # then add the filename to the list in the dictionary
            elif document not in word_appearance[word]:
                word_appearance[word].append(document)

    # After getting which files the word appears in, calculate the idf
    # using the length of the list which represents num of documents it appears
    word_idf = {}

    # Constant of the total number of documents
    total_num_doc = len(documents)

    # Using the formula idf = log_e(total_num / num_appeared)
    for word, doc_list in word_appearance.items():
        word_idf[word] = math.log(total_num_doc / len(doc_list))

    return word_idf


def top_files(query, files, idfs, top_n):
    """
    Given a `query` (a set of words), `files` (a dictionary mapping names of
    files to a list of their words), and `idfs` (a dictionary mapping words
    to their IDF values), return a list of the filenames of the the `n` top
    files that match the query, ranked according to tf-idf.
    """
    file_score = {fname: 0 for fname in files}

    for word in query:
        for fname, word_list in files.items():
            term_freq = word_list.count(word)
            file_score[fname] += term_freq * idfs[word]

    # Get the list of tuples from the file_score dict
    # Sort by score (x[1] in tuple), descending order
    rank_by_score = sorted(file_score.items(), key=lambda x: x[1], reverse=True)

    # Return only the list of file names of the n most relevant files
    return [filename[0] for filename in rank_by_score[:top_n]]


def top_sentences(query, sentences, idfs, top_n):
    """
    Given a `query` (a set of words), `sentences` (a dictionary mapping
    sentences to a list of their words), and `idfs` (a dictionary mapping words
    to their IDF values), return a list of the `n` top sentences that match
    the query, ranked according to idf. If there are ties, preference should
    be given to sentences that have a higher query term density.
    """
    # Each sentence is mapped to the sum of idf score and the query_term_density
    sentence_score = {sentence: [0, 0] for sentence in sentences}

    # Check each word in the query if it's in the sentence
    # Add word idf and qtd to corresponding sentence if it is
    for word in query:
        for sentence, word_list in sentences.items():
            if word in word_list:
                sentence_score[sentence][0] += idfs[word]
                sentence_score[sentence][1] += word_list.count(word) / len(word_list)

    # Rank sentences by scores, return list of tuples (sentence, score), descending order
    rank_by_score = sorted(sentence_score.items(), key=lambda x: (x[1][0], x[1][1]), reverse=True)
    return [sentence[0] for sentence in rank_by_score[:top_n]]


if __name__ == "__main__":
    main()
