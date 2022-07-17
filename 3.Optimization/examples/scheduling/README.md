# Scheduling

Schedule exam periods so that they satisfy all constraints (no overlap)

- `schedule0.py`: Implements the `backtrack` function as well as some helpers such as `select_unassigned_variable` and `consistent` to help satisfy all constraints
- `schedule1.py`: Uses the `python-constraint` library to do the same task

## How to Use

In the `scheduling` directory, run each of the commands below to execute corresponding program

```shell
python schedule0.py
python schedule1.py
```

## What to Learn

Check out the `backtrack` function and its helpers, understand how the recursion works and why it can satisfy all constraints
