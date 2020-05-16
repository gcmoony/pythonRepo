import random

def chooseMap():
    choices = ["Customs",
               "Shoreline",
               "Factory",
               "Reserve",
               "Labs",
               "Interchange",
               "Woods"]
    print("Go to: ", random.choice(choices))

chooseMap()