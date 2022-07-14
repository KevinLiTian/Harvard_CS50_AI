## Specification

Complete the implementation of `load_data` and `get_model` in `traffic.py`

- The `load_data` function should accept as an argument `data_dir`, representing the path to a directory where the data is stored, and return image arrays and labels for each image in the data set
  - You may assume that `data_dir` will contain one directory named after each category, numbered `0` through `NUM_CATEGORIES - 1`. Inside each category directory will be some number of image files.
  - Use the OpenCV-Python module (`cv2`) to read each image as a `numpy.ndarray` (a `numpy` multidimensional array). To pass these images into a neural network, the images will need to be the same size, so be sure to resize each image to have width `IMG_WIDTH` and height `IMG_HEIGHT`
  - The function should return a tuple `(images, labels)`. `images` should be a list of all of the images in the data set, where each image is represented as a `numpy.ndarray` of the appropriate size. `labels` should be a list of integers, representing the category number for each of the corresponding images in the `images` list
  - Your function should be platform-independent: that is to say, it should work regardless of operating system. Note that on macOS, the `/` character is used to separate path components, while the `\` character is used on Windows. Use `os.sep` and `os.path.join` as needed instead of using your platform’s specific separator character
- The `get_model` function should return a compiled neural network model
  - You may assume that the input to the neural network will be of the shape `(IMG_WIDTH, IMG_HEIGHT, 3)` (that is, an array representing an image of width `IMG_WIDTH`, height `IMG_HEIGHT`, and `3` values for each pixel for red, green, and blue)
  - The output layer of the neural network should have `NUM_CATEGORIES` units, one for each of the traffic sign categories
  - The number of layers and the types of layers you include in between are up to you. You may wish to experiment with:
    - different numbers of convolutional and pooling layers
    - different numbers and sizes of filters for convolutional layers
    - different pool sizes for pooling layers
    - different numbers and sizes of hidden layers
    - dropout

Ultimately, much of this project is about exploring documentation and investigating different options in `cv2` and `tensorflow` and seeing what results you get when you try them!

You should not modify anything else in `traffic.py` other than the functions the specification calls for you to implement, though you may write additional functions and/or import other Python standard library modules. You may also import `numpy` or `pandas`, if familiar with them, but you should not use any other third-party Python modules. You may modify the global variables defined at the top of the file to test your program with other values

## Hints

- Check out the official [Tensorflow Keras overview](https://www.tensorflow.org/guide/keras/overview) for some guidelines for the syntax of building neural network layers. You may find the lecture source code useful as well
- The [OpenCV-Python](https://docs.opencv.org/4.5.2/d2/d96/tutorial_py_table_of_contents_imgproc.html) documentation may prove helpful for reading images as arrays and then resizing them
- Once you’ve resized an image `img`, you can verify its dimensions by printing the value of `img.shape`. If you’ve resized the image correctly, its shape should be `(30, 30, 3)` (assuming `IMG_WIDTH` and `IMG_HEIGHT` are both `30`)
- If you’d like to practice with a smaller data set, you can download the modified dataset that contains only 3 different types of road signs instead of 43 through the link in the `data` directory
