# Learning

Previously, the behavior of AI is explicitly defined, the algorithms are written for the program to execute; however, humans are not almighty, there are things we don't know. Machine learning gives AI the ability to learn from data itself and recognize patterns that humans cannot

## Supervised Learning

Supervised learning is a task where a computer learns a function that maps inputs to outputs based on a dataset of input-output pairs. The dataset are tagged/labeled by humans for AI to recognize the relationship between the input-output pairs

### Classification

One of the tasks under supervised learning is classification. The AI learns a function that maps an input to a discrete output. For instance, given a set of data with input humidity and pressure, output either raining or not. There are several common methods that are used in classification tasks

### Nearst-Neighbor Classification

Assigning a variable the value of the closest observation. For instance, given an unknown humidity and pressure, this classification method will find in its training dataset which humidity and pressure pair of data is numerically the closest to the given known pair, and assign the value (rain/not rain) of known pair to the unknown pair

- **K-Nearst-Neighbor Classification**: Since there might be outliers and noises in the dataset, there is limitations to the NN classification. A way to get around is the KNN classification. Comparing to choosing the only closest data point in the training dataset, this method choose k number of closest data point (k can be customized) and assign the value of the most frequent value

### Perceptron Learning

Other than considering the neighbors, another way of going about a classification problem is the perceptron learning. Oppose to only looking at a small area of data, perceptron learning looks in a bigger picture, and tries to create a decision boundary, or graphically, create a straight line separating two types of data. This method can also be called linear regression

<img src="https://user-images.githubusercontent.com/99038613/179422902-04df9c74-740a-4f48-9eae-64930a51a6ef.jpg" width=60%>

This method creates a "hard" threshhold function so that anything on one side of the boundary is of a certain value and on the other side another. But it might be too certain and in the real world, sometimes events involves some degree of uncertainty. So if we want to incorporate uncertainty and give the probability of a data point belongs to a certain category, a logistic function can be used instead to create a "soft" threshhold function. This method is called logistic regression

<img src="https://user-images.githubusercontent.com/99038613/179422910-16120f5e-bdd1-4402-9cd7-a6014d7d11ad.jpg" width=60%>

<img src="https://user-images.githubusercontent.com/99038613/179422913-d6bf43e1-8972-4e72-afe8-ad187440a8fc.jpg" width=60%>

### Support Vector Machine

In addition to nearst-neighbors, linear and logistic regressions, another approach to the classification problem is Support Vector Machine. This method adds another vector to the boundary line to make the best decision separating the data.

For example, in the figures below, the normal linear regression might generate a boundary line that looks like the white line in the middle graph. With the additional vector, it can create maximum margin separator that optimally generalizes the decision boundary.

<img src="https://user-images.githubusercontent.com/99038613/176823781-411939f2-6c03-46d5-9bd5-96960892559e.jpg">

Or like the figure below, with the additional vector, the boundary can be in more complex shapes instead of a straight line

<img src="https://user-images.githubusercontent.com/99038613/176823866-a3404d58-1cfd-4f7f-875d-8230a1054190.jpg" width=60% height=60%>

### Regression

In classification problems, the AI maps inputs to discrete outputs. Regression is a supervised learning task that maps inputs to continuous outputs. For instance, a financial company might use regression to map the advertisement cost to sales revenue to get specific number of how much expenditures correspond to how much benefits

### Loss Function

Loss function is a way to quantify the utility lost by any of the decision rules above. The less accurate the prediction, the larger the loss. The AI or the programmar can use the loss function to evaluate the quality of the machine learning model in order to make further

- **0-1 Loss Function**: The loss function returns 1 when the predicted is the same as the actual and 0 otherwise, mostly used in classification problem
- **L1 Loss Function**: The loss function returns the absolute difference between the predicted and the actual
- **L2 Loss Function**: The loss function returns the square of the difference between the predicted and the actual. Penalizes outliers more harshly than the L1 since the difference is being squared

One should choose loss functions accordingly to the need of the problem

### Overfitting

As loss function becomes the quality indicator of the machine learning model, there is one severe problem, overfitting. This means that the model fits the training dataset too perfectly so that it fails to generalize to the unknown data. For instance, the figures below illustrates graphically the overfitting models. They are perfect for the training dataset, the loss function will always be 0, but they might not be a good model for predictions for other unknown data

<img src="https://user-images.githubusercontent.com/99038613/176824053-e2b69fd6-6de0-4644-b0b3-bf52f6ab246e.jpg">

### Regularization

Regularization is used in order to avoid overfitting. The idea is that the quality of the model should not only depend on the loss function, but also its complexity. The model should not be too complex such like in overfitting models

One way to test if the model is overfitting is to split the given dataset into training and testing sets, the AI uses the training set for training and use the test set to test the quality of the model. If the model is overfitting then it will not perform well when prediction the test set

## Reinforcement Learning

Reinforcement learning is another approach to machine learning. Instead of training on given datasets, the AI will make actions under certain states, where after each action, the AI gets feedback in the form of reward or punishment (a positive or a negative numerical value), so the AI will learn from experience and understand which actions are good under whichs states

### Markov Decision Processes

Similar to the Markov chain in the uncertainty lecture, the reinforcement learning process can be viewed as a Markov decision process. Under each state, the AI will have a set of actions to choose from and each action will be associated to a reward or punishment (instead of probabilities in the Markov chain). The reward for each action under each state is initially all set to 0 and will be changed by the AI based on its experience

### [Q-Learning](https://en.wikipedia.org/wiki/Q-learning)

Q-Learning is one model of reinforcement learning, where a function Q(s, a) outputs an estimate of the value of taking action a in state s. There is also a formula to update the value of action a in state s as the AI gain experience:

![屏幕截图 2022-07-01 003131](https://user-images.githubusercontent.com/99038613/176824214-ec694fde-9aa1-4b0b-95f1-d6df16bc756e.jpg)

But there is limitation to reinforcement learning, the AI will learn the way to get rewards, but the way it learned is not necessarily the optimal way. Since the AI will choose the action with the highest reward, which is called the greedy decision making, once it finds a way, it will never explore other ways. This brings us to the tradeoff between exploration vs exploitation. In general, at the beginning of the game, the AI should have a higher chance of making random moves to explore the environment and as it learns more about the environment, there should be a higher chance the AI will make greedy moves

## Unsupervised Learning

In supervised learning, the data are labeled, and the AI is to find relationship between some label and others. In unsupervised learning, the data are not labeled, and the AI is to find the patterns in these data

### Clustering

Clustering is a typical task of unsupervised learning which is to group the data into clusters

### [K-Means Clustering](https://en.wikipedia.org/wiki/K-means_clustering)

KMC is a clustering algorithm that groups data into k clusters. It initially selects k random centers and marks each data point to its closest center. Then iteratively, the center moves to the average mid point of all its marked data points, then each data point will be remarked to the current closest center. This iterative clustering algorithm will terminate when no data point changes its belonging and finally converges

![1](https://user-images.githubusercontent.com/99038613/179422984-6359733e-20aa-4f1a-8f76-1981d599730e.jpg)

## Examples

Check out some [examples](examples/) that practice these theories
