import random

min = 1
max = 6

random.seed(a=None)

def roll():
    outcome = random.randint(min, max)
    return outcome