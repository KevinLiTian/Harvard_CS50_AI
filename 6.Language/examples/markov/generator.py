"""
Read in existing text, produce tone-like output
This implementation reads text written by Shakespear
analyze with markovify and produce text that in the tone
of Shakespeare
"""

import sys

import markovify


# Read text from file
if len(sys.argv) != 2:
    sys.exit("Usage: python generator.py sample.txt")
with open(sys.argv[1]) as f:
    text = f.read()

# Train model
text_model = markovify.Text(text)

# Generate sentences
print()
for i in range(5):
    print(text_model.make_sentence())
    print()
