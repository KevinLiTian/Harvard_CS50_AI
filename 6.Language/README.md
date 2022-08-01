# Language

In the previous lectures, we are rephrasing human-readable problems into AI-readable problems and diving into the AI language. This lecture will make AI understand human language. This is generally called natural language processing, and there are many tasks under this area of knowledge

- **Automatic summarization**, where the AI is given text as input and it produces a summary of the text as output
- **Information extraction**, where the AI is given a corpus of text and the AI extracts data as output
- **Language identification**, where the AI is given text and returns the language of the text as output
- **Machine translation**, where the AI is given a text in the origin language and it outputs the translation in the target language
- **Named entity recognition**, where the AI is given text and it extracts the names of the entities in the text (for example, names of companies)
- **Speech recognition**, where the AI is given speech and it produces the same words in text
- **Text classification**, where the AI is given text and it needs to classify it as some type of text
- **Word sense disambiguation**, where the AI needs to choose the right meaning of a word that has multiple meanings (e.g. bank means both a financial institution and the ground on the sides of a river)

## Syntax

Syntax is sentence structure. As native speakers of some human language, we don’t struggle with producing grammatical sentences and flagging non-grammatical sentences as wrong; however, the AI has no idea about natural languages. In order for AI to understand the fundamentals of language, they have to know the sentence structures or, syntax, of the language

### Context-Free Grammar

In context-free grammar, the text is abstracted from its meaning to represent the structure of the sentence using formal grammar. In another word, the actual meaning of the text are irrelevant since we are only looking at the structure of the sentence, such as nouns, verbs, adjectives, etc. For example, the sentence:

- She saw the city.

This sentence is composed by words "she", "saw", "the", "city". We can classify "she" and "city" as nouns (N), "saw" as verb (V) and "the" as a determiner (D) connecting words. Therefore the sentence can be rewritten as:

- N V D N

This stands for the structure of the sentence. Notice that the N here can be replaced by any noun such as "he" or "dog", the same goes to V and D. The idea here is to encode the syntax of sentences such as "NVDN" or other forms of sentences so that the AI can recognize the sentences' syntax and correctly predicts which word is the noun, verb or others

- **Noun Phrase (NP)**: Sometimes, "a dog" also means the noun "dog", therefore we can encode something called the NP. Where a N can be either a single N or the NP which is the combination of D and N
- **Verb Phrase (VP)**: Similar to NP, a verb can be either a single verb or a VP which is a combination of V and NP

    <img src="https://user-images.githubusercontent.com/99038613/177066741-7f7ae85b-8483-41ca-8949-accebf57c331.jpg" width=60% height=60%>

### N-Grams

Sentences are often long, the AI might have a hard time recognizing something that long and it hasn't seen before. That's where N-Grams comes in. This method introduces similar idea to batch, it groups every n number (often 1-3) of words together and form a short sentence like in the sentence:

“How often have I said to you that when you have eliminated the impossible whatever remains, however improbable, must be the truth?”

Some N-Grams could be "How often have", "often have I", "have I said", ... Shorter sentences are more likely to appear multiple times so the AI will be able to recognize them more easily

### Tokenization

Tokenization is the task of splitting a sequence of characters into pieces (tokens). Tokens can be words or sentences, which are called word tokenization or sentence tokenization respectively

### Markov Models

Once we have tokens or n-grams, we can use them to predict words or sentences. For instance, if in an article, there's a lot of 3-grams "have I said", then if there is a "have" and "I" together, then the next word is highly possible to be "said". This operates just like the Markov chain, we use what happened before to predict what will happen after

### Information Extraction

Information Extraction is the task of extracting knowledge from documents. One way is to let the AI learn the syntax of the knowledge. For example, Harvard Business Review stated that "When Facebook was founded in 2004", we can tell the AI that there is a certain type of sentence looks like "When {company} was founded in {year}", and from these sentences we are able to extract the company name and year they were founded. Similar methods can be applied to more sentence structures to extract information

## Bayes & TF-IDF

Another way to look at sentences are treating them as a collection of unordered words. In this way, we don't care about the syntax or structure of the sentences, we are only looking at the words themselves. For example, when a website is using an AI to predict which comments are positive and which ones are negative

- “My grandson loved it! So much fun!”
- “Product broke after a few days.”
- “One of the best games I’ve played in a long time.”
- “Kind of cheap and flimsy, not worth it.”

### Naive Bayes

Recall the Bayes rule from lecture 2 Uncertainty

<img src="https://user-images.githubusercontent.com/99038613/177066748-6c6431d1-0d6b-479c-aff2-283f43ae4db2.jpg" width=60% height=60%>

From this rule we can state that the probability of a sentence is positive is equal to the probability of a comment is positive given a certain comment. And that is equal to the joint probability of a comment is positive and a comment is positive given each word in the

<img src="https://user-images.githubusercontent.com/99038613/177066756-17b0f18a-a665-45b0-9a2a-fde80f76c6b5.jpg" width=60% height=60%>

Then we are able to use this formula to calculate the probability that this comment is positive or negative since we have the data of all the joint probabilities

<img src="https://user-images.githubusercontent.com/99038613/177066765-e862d326-0f7a-42e3-b7ce-f2e5ffec37af.jpg" width=60% height=60%>

### Information Retrieval

Another task where the AI will not need to know the syntax is information retrieval. Imagine searching something on the internet, one will enter some short sentences and find what's most relevant. How does AI know what's relevant? This task is information retrieval, which the AI will retrieve the most important/relevant information in a search space such as in an article or in the internet

### TF-IDF

One common approach to go about information retrieval is the TF-IDF or the "Term Frequency - Inverse Document Frequency" method.

Intuitively, the importance of information is evaluated as how many times certain information appears in the context. If a word appears multiple times then it must be important, right? Not necessarily. For instance, in the Sherlock Holmes novel, the most frequent words are "the", "a", and other determiners, which does appear a lot but has little information. One way to avoid this is to explicitly ignore the determiners and see other frequent terms. With this approach, the most frequent words in Sherlock Holmes novel is unsurprisingly, "Holmes" and "Sherlock". Because these words appear in all chapters, or in the entire context.

The solution to this problem is the TF-IDF method. This method introduces a mathematical formula that calculates the importance of certain words by the logarithm of number of documents/chapers divided by how many times certain word appears in a document

<img src="https://user-images.githubusercontent.com/99038613/177066777-1c050265-12a6-4911-9e90-0c6911855028.jpg" width=60% height=60%>

This method considers not only how many times a word appears in a document, but how special it is, in certain context. For instance, if this word appears in all documents, the logarithm of 1 is 0, which means this word is of little importance. If a word appears multiple times in one chapter while absent in others, meaning that the word is important and might be the main information in this certain chapter

## Semantics

Semantics is the meaning of words or sentences. While sometimes we only want to know the structure a sentence, or the important information within a context, but there are times we want the AI to understand the actual, underlying meaning of each word and sentence

### WordNet

One approach is using the existing database created by researchers, the [WordNet](https://en.wikipedia.org/wiki/WordNet). It contains all the information about words such as their definitions, different senses/meanings, and relationship to other words

### Word Representation

Computers only know 0s and 1s, in order for the AI to understand natural language, we have to somehow encode the words into numbers. One way to represent words is by one hot encoding. For instance, for words "He wrote a book", we can encode that:

- [1, 0, 0, 0] (he)
- [0, 1, 0, 0] (wrote)
- [0, 0, 1, 0] (a)
- [0, 0, 0, 1] (book)

However, this method is not feasible for real world use since there are too many words to be one hot encoded. A vector of thousands of items only to represent a word is too costly. Also, by one hot encoding, we are not able to represent relationships between words since the 1 is randomly placed, so the word "book" and "novel" has no mathematical relationship for the AI to recognize.

### Word2Vec

Therefore, we turn to the idea of distributed representation, where each word is represented by a vector of less than 100 items and each item is a floating point number. This method is counter-intuitive since how can words be represented by a bunch of floating point numbers? Well, this method actually works really well in real life problems. We can test the functionality of this method by calculating the mathematical distance between two words by calculating the distance between vectors. And it turns out it can represent the relationship between words by a floating point number. For instance, the word "book" and "novel", the vector representation of the word "book" is:

book: [-0.226776 -0.155999 -0.048995 -0.569774 0.053220 0.124401 -0.091108 -0.606255 -0.114630 0.473384 0.061061 0.551323 -0.245151 -0.014248 -0.210003 0.316162 0.340426 0.232053 0.386477 -0.025104 -0.024492 0.342590 0.205586 -0.554390 -0.037832 -0.212766 -0.048781 -0.088652 0.042722 0.000270 0.356324 0.212374 -0.188433 0.196112 -0.223294 -0.014591 0.067874 -0.448922 -0.290960 -0.036474 -0.148416 0.448422 0.016454 0.071613 -0.078306 0.035400 0.330418 0.293890 0.202701 0.555509 0.447660 -0.361554 -0.266283 -0.134947 0.105315 0.131263 0.548085 -0.195238 0.062958 -0.011117 -0.226676 0.050336 -0.295650 -0.201271 0.014450 0.026845 0.403077 -0.221277 -0.236224 0.213415 -0.163396 -0.218948 -0.242459 -0.346984 0.282615 0.014165 -0.342011 0.370489 -0.372362 0.102479 0.547047 0.020831 -0.202521 -0.180814 0.035923 -0.296322 -0.062603 0.232734 0.191323 0.251916 0.150993 -0.024009 0.129037 -0.033097 0.029713 0.125488 -0.018356 -0.226277 0.437586 0.004913]

The distance between "book" and "book" is 0, since they are the same word, and since mathematically the two vectors are the same so they share a same location in the vector space, which leads to 0 distance. The distance between "book" and "novel" is 0.3437, which does not represent much by itself but if we take a look at the distance between "book" and "breakfirst", the distance is 0.6352, which means the distance between "book" and "novel" is smaller than the distance between "book" and "breakfirst", which also means the meaning of "book" is more closely to the meaning of "novel", makes sense to humans

Amazingly, since words are represented by vectors, we are able to compute the difference vector between two vectors. For instance, take the words "man" and "king" and subtract two words. It is absurd to human to subtract two words but since to the AI, they are nothing but two vectors, therefore it is able to compute the difference as a vector. And if we add this difference to the word "woman", surprisingly, we are able to get the word "queen". This means that the AI is able to understand the actual meaning of the words

`King - Man + Woman = Queen`

## Examples

Check out some [examples](examples/) that practice these theories
