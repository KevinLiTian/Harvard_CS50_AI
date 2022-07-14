# Traffic

An AI that uses Tensorflow to train a convolutional neural network to identify which traffic sign appears in a photograph

## Background

As research continues in the development of self-driving cars, one of the key challenges is computer vision, allowing these cars to develop an understanding of their environment from digital images. In particular, this involves the ability to recognize and distinguish road signs – stop signs, speed limit signs, yield signs, and more

The dataset that will be used is the [German Traffic Sign Recognition Benchmark (GTSRB)](https://benchmark.ini.rub.de/?section=gtsrb&subsection=news) dataset, which contains thousands of images of 43 different kinds of road signs

## Files

The dataset is too large, therefore the `data` directory only contains the links to download them. After downloading, the `data` directory should be replaced by the downloaded folder, namely "gtsrb". The `traffic.py` file contains the main functions including loading data, getting model, training the model and evaluating the model

## How to Use

Make sure `Tensorflow`, `opencv-python` and `scikit-learn` are installed. If not, run the following command

`pip install tensorflow opencv-python scikit-learn`

In the `traffic` directory, run the command

`python traffic.py data model_filename`

Where `data` should be either gtsrb or gtsrb-small which are downloaded through the links in the `data` directory. `Model_filename` is an optional argument that will store the trained model to the specifiled path

## Example Output

```shell
$ python traffic.py gtsrb
Epoch 1/10
500/500 [==============================] - 5s 9ms/step - loss: 3.7139 - accuracy: 0.1545
Epoch 2/10
500/500 [==============================] - 6s 11ms/step - loss: 2.0086 - accuracy: 0.4082
Epoch 3/10
500/500 [==============================] - 6s 12ms/step - loss: 1.3055 - accuracy: 0.5917
Epoch 4/10
500/500 [==============================] - 5s 11ms/step - loss: 0.9181 - accuracy: 0.7171
Epoch 5/10
500/500 [==============================] - 7s 13ms/step - loss: 0.6560 - accuracy: 0.7974
Epoch 6/10
500/500 [==============================] - 9s 18ms/step - loss: 0.5078 - accuracy: 0.8470
Epoch 7/10
500/500 [==============================] - 9s 18ms/step - loss: 0.4216 - accuracy: 0.8754
Epoch 8/10
500/500 [==============================] - 10s 20ms/step - loss: 0.3526 - accuracy: 0.8946
Epoch 9/10
500/500 [==============================] - 10s 21ms/step - loss: 0.3016 - accuracy: 0.9086
Epoch 10/10
500/500 [==============================] - 10s 20ms/step - loss: 0.2497 - accuracy: 0.9256
333/333 - 5s - loss: 0.1616 - accuracy: 0.9535
```

## Test Result

- Different numbers of convolutional and pooling layers
- Different numbers and sizes of filters for convolutional layers
- Different pool sizes for pooling layers
- Different numbers and sizes of hidden layers
- Dropout

|     |                              Model                              | Testing accuracy |
| :-: | :-------------------------------------------------------------: | :--------------: |
|  1  |                      In Class Model (Base)                      |     `0.0531`     |
|  2  |        Additional Convolution Layer after Pooling Layer         |     `0.9659`     |
|  3  |        Additional Convolution Layer before Pooling Layer        |     `0.9780`     |
|  4  |                  Additional Max-Pooling Layer                   |     `0.0539`     |
|  5  |           Modify Pool Size to 3x3 Compare to Model 3            |     `0.9809`     |
|  6  |          Modify Filter Size to 4x4 Compare to model 3           |     `0.9546`     |
|  7  |           Modify Pool Size to 3x3 Compare to model 2            |     `0.9463`     |
|  8  |           Additional Hidden Layer Compare to Model 2            |     `0.9341`     |
|  9  | Modify Hidden Layer to NUM_CATEGORIES \* 128 Compare to model 2 |     `0.9345`     |
| 10  |         Modify Drop Out Rate to 0.1 Compare to model 3          |     `0.9764`     |
| 11  |         Modify Drop Out Rate to 0.2 Compare to model 3          |     `0.9647`     |
| 12  |         Modify Drop Out Rate to 0.3 Compare to model 3          |     `0.9655`     |

- If not explicitly specified, model changes are comparing to the base model

Based on the test results, it can be concluded that the base model which only has one convolution layer, one pooling layer and a MNN performs this specific task poorly with accuracy of 0.0531. A better approach is by adding another convolution layer right after the first one and before the pooling layer which boosts the accuracy score to 0.9780. According to model 4, adding a pooling layer to the base model will not perform well. By adjusting the parameters based on model 3, the final result is maximized when modifying the pool size from 2x2 to 3x3, which scored at 0.9809

## Video Demo

[![Traffic Project Video](https://img.youtube.com/vi/IHxHY1ztV1c/0.jpg)](https://youtu.be/IHxHY1ztV1c)
