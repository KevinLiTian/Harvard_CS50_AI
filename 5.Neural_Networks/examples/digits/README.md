# Digits

This example shows the implementation of training a neural network to identify human handwriting of digits 0-9 using the famous `MNIST` dataset

## Handwriting

`handwriting.py` uses the `tensorflow` sequencial neural network and the MNIST dataset to train a neural network that identifies human handwriting of digits 0-9

## Recognition

`recognition.py` is a pygame which allows you to hand write something and the trained neural network will identify the digit you wrote (not certain, but the best probability)

In the `digits` directory, run the command `python recognition.py model.h5`

A pygame window should pop up and you can use your mouse to draw something

![1](https://user-images.githubusercontent.com/99038613/179424233-51522b53-1586-420e-9df1-c11a01630490.jpg)

Click `Classify` to let the neural network classify what the number you are writing. Click `Reset` to clear the drawing area and the classification

![2](https://user-images.githubusercontent.com/99038613/179424236-f84a38d5-2cd8-48c9-849c-0c17b8a26ff3.jpg)
