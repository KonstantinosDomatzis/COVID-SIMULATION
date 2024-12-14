import random

from Human import *
import random as r

def populate(humans,N):
    for i in range(N):
        name = "Person" + str(i)
        age = r.randint(0,100)
        height = round(r.random()*2,2) #we don't care about the height in a pandemic
        weight = generateWeight(age)
        isVulnerable = generateVulnerable(age,weight)
        humans.append(Human(name, age, height, weight, isVulnerable))

def generateWeight(age):
    if age <= 5:
        return 2 + r.randint(0,20)
    elif age <= 10:
        return 20 + r.randint(0,15)
    elif age <= 15:
        return 30 + r.randint(0,15)
    elif age <= 18:
        return 40 + r.randint(0,15)
    else:
        return 40 + r.randint(0,100)


def generateVulnerable(age,weight):
    randN = r.random()

    if age < 18 :
        if randN < 0.05:
            return True
        return False
    elif 18 < age < 40:
        if randN < 0.1:
            return True
        return False
    elif 40 <= age <= 60:
        if randN < 0.15:
            return True

        if weight > 90:
            return True
        else:
            return False
    elif 60 <= age <= 80:
        if randN < 0.25:
            return True

        if weight > 100:
            return True
        else:
            return False
    else:
        return True

def day_passes(humans,sick_humans,dead_humans):
    for human in humans:
        if human.immune:
            human.immuneDay += 1
            if human.immuneDay == 15:
                human.immune = False


    randN = random.random()
    i = 0
    while i < len(sick_humans):
        if randN <= 0.02:
            dead = sick_humans.pop(i)
            dead_humans.append(dead)
        else:
            sick_humans[i].sicknessDay += 1
            if sick_humans[i].sicknessDay == 15:
                sick_humans[i].sicknessDay = 0
                sick_humans[i].isSick = False
                sick_humans[i].immune = True
                h = sick_humans.pop(i)
                humans.append(h)
        i += 1