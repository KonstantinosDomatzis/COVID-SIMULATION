import random

class Human:
    def __init__(self, name, age, height, weight, isVulnerable ):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.isVulnerable = isVulnerable
        self.isSick = False
        self.isAlive = True
        self.sicknessDay = 0
        self.immune = False
        self.immuneDay = 0


    def printData(self):
        print(f"Name : {self.name}, "
              f"age : {self.age}, "
              f"height : {self.height}, "
              f"weight : {self.weight}, "
              f"is sick : {self.isSick}, "
              f"is vulnerable : {self.isVulnerable}")


    def contact(self): #assume each contact has about 7% to make someone sick and 11% if he is vulnerable
        randN = random.random()
        if ((self.isVulnerable and randN <= 0.11) or randN < 0.07) and self.immune == False:
            self.isSick = True
            self.sicknessDay = 1