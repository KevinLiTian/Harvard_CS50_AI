# Guide

Welcome to learning Artificial Intelligence!

## Setting Python Environment

It is recommended that [Miniconda](https://docs.conda.io/en/latest/miniconda.html) is used to manage Python packages. First install [Miniconda](https://docs.conda.io/en/latest/miniconda.html), update your `conda` environment, and then create a new `conda` environment with Python 3.9 using the command:

```shell
conda update conda -y
conda create -n AI python=3.9
conda activate AI
```

where `AI` is the preferred name of your new environment. You can name it whatever you want. You can turn off the `conda` environment using the command:

`conda deactivate`

## Install Dependencies

Then use `pip` to install all the packages needed which are specified in the `requirements.txt`. It is recommanded to use the command below to install all the packages at once:

`pip install -r requirements.txt --upgrade`
