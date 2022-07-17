# Digits

This example shows the implementation of training a neural network to identify human handwriting of digits 0-9 using the famous `MNIST` dataset

## Handwriting

`handwriting.py` uses the `tensorflow` sequencial neural network and the MNIST dataset to train a neural network that identifies human handwriting of digits 0-9

## Recognition

`recognition.py` is a pygame which allows you to hand write something and the trained neural network will identify the digit you wrote (not certain, but the best probability)

In the `digits` directory, run the command `python recognition.py model.h5`

A pygame window should pop up and you can use your mouse to draw something

Figure 1

Click `Classify` to let the neural network classify what the number you are writing. Click `Reset` to clear the drawing area and the classification

Figure 2
