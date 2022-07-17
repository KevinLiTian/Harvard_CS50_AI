# Neural Networks Examples

3 exampels demonstrating what neural networks are capable of and how to implement them with Python using libaries such as `tensorflow` and `scikit-learn`

## Banknotes

Instead of using machine learning to train models like in `Learning`, this implementation uses the `tensorflow` suquencial neural network to train a network that identifies counterfeit banknotes from published ones

## Convolution

Demonstrate how neural networks can be applied to image processing, implements the image convolution which can be added to a convolutional neural network. This specific implementation uses the famous `[-1, -1, -1, -1, 8, -1, -1, -1, -1]` filter which results in a new image with only the shape of objects in the original image

## Digits

Using the famout `MNIST` dataset, train a neural network to identify handwritings of digits 0-9. Comes with a Pygame that allows user to handwrite digits and the neural network will identify the number user wrote
