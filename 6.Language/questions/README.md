# Questions

An AI that replies to queries using tf-idf

## Background

Question Answering (QA) is a field within natural language processing focused on designing systems that can answer questions. Among the more famous question answering systems is [Watson](https://en.wikipedia.org/wiki/IBM_Watson), the IBM computer that competed (and won) on Jeopardy!. A question answering system of Watson’s accuracy requires enormous complexity and vast amounts of data, but in this problem, we’ll design a very simple question answering system based on inverse document frequency

## Files

In the `corpus` directory, there are some documents from wikipedia which contains some information for the AI to use. One can add more information to this directory to expand the functionality of the Q&A AI. In the `questions.py`, the AI reads from the documents, tokenize files and sentences, then use tf-idf to calculate the importance of certain words, reply the users' queries with the most relevant sentence

## How to Use

Make sure `nltk` is installed, if not, use the following command

`pip install nltk`

In the `questions` directory, run the command

`python questions.py corpus`

Then enter some query as prompt to get a reply from the AI

## Example Output

```shell
$ python questions.py corpus
Query: What are the types of supervised learning?
Types of supervised learning algorithms include Active learning , classification and regression.

$ python questions.py corpus
Query: When was Python 3.0 released?
Python 3.0 was released on 3 December 2008.

$ python questions.py corpus
Query: How do neurons connect in a neural network?
Neurons of one layer connect only to neurons of the immediately preceding and immediately following layers.
```
