""" Glimpse into propositional logic """

from logic import *

rain = Symbol("rain") # It is raining
hagrid = Symbol("hagrid") # Harry visited Hagrid
dumbledore = Symbol("dumbledore") # Harry visited Dumbledore

""" Knowledge to Represent
1. If it's not raining, then Harry visited Hagrid
2. Harry either visited Hagrid or visited Dumbledore
3. Harry cannot visit both Hagrid and Dumbledore
4. Harry visited Dumbledore
Query: Is it raining or not?
"""
knowledge = And(
    Implication(Not(rain), hagrid),
    Or(hagrid, dumbledore),
    Not(And(hagrid, dumbledore)),
    dumbledore
)

print(knowledge.formula())
print(model_check(knowledge, rain))
