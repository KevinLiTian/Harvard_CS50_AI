# Test Result

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
