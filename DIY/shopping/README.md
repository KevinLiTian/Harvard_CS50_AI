## Specification

Complete the implementation of `load_data`, `train_model`, and `evaluate` in `shopping.py`.

The `load_data` function should accept a CSV filename as its argument, open that file, and return a tuple `(evidence, labels)`. `evidence` should be a list of all of the evidence for each of the data points, and `labels` should be a list of all of the labels for each data point.

- Since you’ll have one piece of evidence and one label for each row of the spreadsheet, the length of the `evidence` list and the length of the `labels` list should ultimately be equal to the number of rows in the CSV spreadsheet (excluding the header row). The lists should be ordered according to the order the users appear in the spreadsheet. That is to say, `evidence[0]` should be the evidence for the first user, and `labels[0]` should be the label for the first user.
- Each element in the `evidence` list should itself be a list. The list should be of length 17: the number of columns in the spreadsheet excluding the final column (the label column).
- The values in each `evidence` list should be in the same order as the columns that appear in the evidence spreadsheet. You may assume that the order of columns in `shopping.csv` will always be presented in that order.
- Note that, to build a nearest-neighbor classifier, all of our data needs to be numeric. Be sure that your values have the following types:
  - `Administrative`, `Informational`, `ProductRelated`, `Month`, `OperatingSystems`, `Browser`, `Region`, `TrafficType`, `VisitorType`, and `Weekend` should all be of type `int`
  - `Administrative_Duration`, `Informational_Duration`, `ProductRelated_Duration`, `BounceRates`, `ExitRates`, `PageValues`, and `SpecialDay` should all be of type float.
  - `Month` should be `0` for January, `1` for February, `2` for March, etc. up to `11` for December.
  - `VisitorType` should be `1` for returning visitors and `0` for non-returning visitors.
  - `Weekend` should be `1` if the user visited on a weekend and `0` otherwise.
- Each value of `labels` should either be the integer `1`, if the user did go through with a purchase, or `0` otherwise.
- For example, the value of the first evidence list should be `[0, 0.0, 0, 0.0, 1, 0.0, 0.2, 0.2, 0.0, 0.0, 1, 1, 1, 1, 1, 1, 0]` and the value of the first label should be `0`.

The `train_model` function should accept a list of evidence and a list of labels, and return a `scikit-learn` nearest-neighbor classifier (a k-nearest-neighbor classifier where `k = 1`) fitted on that training data.

- Notice that we’ve already imported for you `from sklearn.neighbors import KNeighborsClassifier`. You’ll want to use a `KNeighborsClassifier` in this function.

The `evaluate` function should accept a list of `labels` (the true labels for the users in the testing set) and a list of `predictions` (the labels predicted by your classifier), and return two floating-point values `(sensitivity, specificity)`.

- `sensitivity` should be a floating-point value from 0 to 1 representing the “true positive rate”: the proportion of actual positive labels that were accurately identified.
- `specificity` should be a floating-point value from 0 to 1 representing the “true negative rate”: the proportion of actual negative labels that were accurately identified.
- You may assume each label will be `1` for positive results (users who did go through with a purchase) or `0` for negative results (users who did not go through with a purchase).

You should not modify anything else in `shopping.py` other than the functions the specification calls for you to implement, though you may write additional functions and/or import other Python standard library modules. You may also import `numpy` or `pandas` or anything from `scikit-learn`, if familiar with them, but you should not use any other third-party Python modules. You should not modify `shopping.csv`.

## Hints

- For information and examples about how to load data from a CSV file, see Python’s [CSV documentation](https://docs.python.org/3/library/csv.html)
