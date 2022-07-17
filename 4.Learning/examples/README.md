# Learning Examples

To distinguish published and counterfeit banknotes is a useful real world problem to solve. We are able to achieve this by machine learning

## Files

- `banknotes.csv`: The data file that contains some features of the banknotes and whether they are published or counterfeit
- `banknotes0.py`: Hardcoded machine learning technique to train a model, several models available for selection and testing
- `banknotes1.py`: Recommanded way, uses machine learning library `scikit-learn` to train a model, several models available for selection and testing

## How to Use

Take a look at either Python file, at the top there are some models available:

```Python
model = Perceptron()
model = svm.SVC()
model = KNeighborsClassifier(n_neighbors=1)
model = GaussianNB()
```

Choose one each time and test out which works best

In the `examples` directory, run the command

`python banknotes0.py` or `python banknotes1.py`
