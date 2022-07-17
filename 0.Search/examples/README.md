# Search Examples

This example shows the example algorithm for both BFS and DFS since the only difference between them is the data structure used to store the neighbor nodes. This program also outputs the total number of states explored and a png showing the states explored as red and the final path found as yellow

## How to Use

Make sure `pillow` is installed on your device as it's the dependency to output images. If not, run

`pip install pillow`

In the `example` directory, run the command:

`python maze.py maze.txt`

Where `maze.txt` can be the three pre-defined `maze1.txt`, `maze2.txt`, and `maze3.txt`, or you can use the similar syntax to create your own maze!

In order to change from BFS to DFS or vice versa, find the `solve` function of the `Maze` class, modify and `frontier` data structure to either a `StackFrontier` or a `QueueFrontier` which are implemented already

## What to Learn

Check step by step how the `solve` function of the `Maze` class works, since this function is the Python implementation of BFS/DFS search algorithm. Other functions and classes are helpers to produce the maze and help with the final output
