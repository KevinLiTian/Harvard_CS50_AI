# Hospitals

Place hospitals on the grid so that the sum of distance from any house to its closest hospital results as small as possible. We can use hill climbing algorithm here to solve for local optimums. In order to have a better chance of finding the global optimum, we can use the random restart algorithm which re-run several iterations of hill climbing with each starting at a different start point (place hospitals differently at the beginning)

## How to Use

In the `hospitals` directory, run the command `python hospitals.py`

You will see some png images generated in this directory, each of which is a step taken to minimize the cost

In order to use the random restart algorithm, go to the `main` function and comment out the `hill_climb` function while uncomment the `random_restart` function

## What to Learn

Check the `hill_climb` function, understand the overall idea as well as what each step is doing. Also check the `random_restart` function, check how it is working and utilizing the `hill_climb` function
