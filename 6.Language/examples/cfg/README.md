# Context-Free Grammar

By defining the syntax of a language (ie. sentence = noun + verb), we construct a so called context-free grammar which does not care about the actual meaning of the sentence, we only want the AI to identify the structure of a sentence

## How to Use

In the `cfg` directory, run the command

`python cfg0.py` or `python cfg1.py`

The AI will prompt you to write a sentence, note that the AI can only identify sentences using the words specified in each Python files

## Example Output

```shell
python cfg0.py
Sentence: she saw the city
         S
  _______|___
 |           VP
 |    _______|___
 NP  |           NP
 |   |        ___|___
 N   V       D       N
 |   |       |       |
she saw     the     city
```
