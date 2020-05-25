import random

def chooseMap():
    choices = ["Customs",
               "Shoreline",
               "Factory",
               "Reserve",
               "Labs",
               "Interchange",
               "Woods"]
    return random.choice(choices)

chooseMap()