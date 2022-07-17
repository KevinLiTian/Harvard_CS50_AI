# Convolution

Processing entire images is inefficient, that's where convolution comes in and make things easier. Convolution shrinks the sizes of images and with proper filters, we are able to get even better results then processing the original image since there are some features we care more about and some less

This implementation uses the famous `[-1, -1, -1, -1, 8, -1, -1, -1, -1]` filter which produces a new image with the shape of the objects in the orginal image

## How to Use

In the `convolution` directory, run the command `python filter.py bridge.png`

Check the original image and the produced image by convolution, what did you notice?
