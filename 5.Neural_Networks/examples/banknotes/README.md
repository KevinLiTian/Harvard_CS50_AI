# Banknotes

Using the `tensorflow keras sequencial model` and a given dataset to train a neural network that identifies the counterfeit banknotes

## Understanding

`banknotes.py` first reads in the data from `banknotes.csv`, split it into train set and test set using the `train_test_split `function in `scikit-learn`. Then create a `tensorflow` sequencial neural network, add a hidden layer of neurons and also an output layer. Configure the neural network with `model.compile` then train the network using the train set data. Test the trained network using the `model.evaluate` function with the test set data

## How to Use

In the `banknotes` directory, run the command `python banknotes.py`
