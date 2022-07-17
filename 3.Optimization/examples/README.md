# Optimization Examples

3 examples demonstrates local search, linear programming and constraint satisfaction problem respectively

## Hospitals

The problem we are to solve is: inside a space, there are randomly located houses. We are to place some number of hospitals so that the sum of distance from any house to its closest hospital results as small as possible

![1](https://user-images.githubusercontent.com/99038613/179422421-7789a0a9-7fcc-42c4-a70a-6417b4bb50f2.jpg)

The idea of local search here is to first randomly place the hospitals on the graph, then each step we move one hospital for one grid. If the total distance goes down, we accept this state and repeat the process. This is a typical hill climbing search

## Production

Given some object function or cost function, and constraint functions which are all defined based on some variables, we can use linear programming to optimize the objective/cost function by assigning the variables the optimal value. We can use the `scipy` which comes with `scikit-learn` library to do this task

## Scheduling

The problem here is to assign the exam period for students. Some of them are taking multiple classes at the same time, so those classes cannot have the exam on the same period. This is a typical constraint satisfaction problem where we can use the `backtrack` algorithm to solve, or use the `python-constraint` library
