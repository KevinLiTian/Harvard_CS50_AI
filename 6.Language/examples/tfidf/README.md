# TF-IDF

Sometimes we want to know the important topics within a large article, or the main content of each chapter of a book. The intuition is to see the term frequency of each word, how many times they appear in the article should relate to its importance. This idea is partially true since more important words will occur more often

## TF

In `tf0.py`, we are only considering the term frequency of each word

In the `tfidf` directory, run the command `python tf0.py holmes`

We get words such as "the", "a", "and", ... It's true that they appear frequently but themselves are meaningless and cannot represent the topics or main contents of articles

## TF Exclude

In `tf1.py`, we exlude meaningless words that appeared in the previous program by explicitly defining the words that we want to exclude

In the `tfidf` directory, run the command `python tf1.py holmes`

We get words such as "Holmes", "Sherlock", "Watson", ... Sure they are the main characters of the story, but we don't really care that much about them since they appear in any chapters, what we really want is the unique main contents of each chapter

## TF-IDF

IN `tfidf.py`, not only do we considre the term frequency, but also the "inverse document frequency". IDF considers how unique is a word inside a chapter. If a word appears frequently in one chapter but almost never appears in other chapters most likely means that they are the main contents of that chapter

In the `tfidf` directory, run the command

`python tfidf.py holmes` or `python tfidf.py federalist`
