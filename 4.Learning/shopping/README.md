# Shopping

An AI that uses K-Nearst Neighbor model to train and predict if users will buy the product

## Background

When users are shopping online, not all will end up purchasing something. Most visitors to an online shopping website, in fact, likely don’t end up going through with a purchase during that web browsing session. It might be useful, though, for a shopping website to be able to predict whether a user intends to make a purchase or not: perhaps displaying different content to the user, like showing the user a discount offer if the website believes the user isn’t planning to complete the purchase. How could a website determine a user’s purchasing intent? That’s where machine learning will come in

The AI will have access to the data of previous users such as what webpages they visited, how long did they stay on certain webpages, how close is the date to a special date such as valentine, etc. Finally, there is the data of whether the user bought the product or not. By using machine learning algorithm like K-Nearst Nearst-Neighbor, the AI will learn to recognize relationships between data and try to predict whether a user will buy the product or not

## Files

The `shopping.csv` file contains all the data regarding over 10k users, feel free to view them in Microsoft Excel, Google sheets or a text editor. The `shopping.py` file contains the loading of data, the training of the model and the predictions along with its evaluation

## How to Use

Make sure `scikit-learn` is installed on your device, if not, use the command

`pip install scikit-learn`

In the `shopping` directory, run the command

`python shopping.py shopping.csv`

Where the `shopping.csv` is the data file. Feel free to add more data files

## Example Output

```shell
$ python shopping.py shopping.csv
Correct: 4088
Incorrect: 844
True Positive Rate: 41.02%
True Negative Rate: 90.55%
```
