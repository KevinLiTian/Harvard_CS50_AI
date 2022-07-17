# Bayesian Network

This directory contains the implementation of a simple Bayesian network

<img src="https://user-images.githubusercontent.com/99038613/176780156-0c407208-1fab-4106-baf0-27e43510820b.jpg" width="60%" height="60%">

## Model

Constructs the Bayesian Network using `pomegranate` libary, specifying nodes and their associated possibilities

## Likelihood

Use the function `model.predict` to predict the possibility of a given event taking place

In the `bayesnet` directory, run the command `python likelihood.py`

## Inference

Given a fact, infer based on the pre-defined probabilities what are the probabilities of other events taking place. For instance, if we observed that the train is delayed, what is the probability of maintainence taking place?

In the `bayesnet` directory, run the command `python inference.py`
