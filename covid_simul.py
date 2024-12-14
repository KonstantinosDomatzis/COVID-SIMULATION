from Human import *
from Funcs import *
import random as r
from matplotlib import pyplot as plt

N = 100000 #αρχικός πληθυσμός
humans = [] #λίστα ανθρώπων
sick_humans = [] #λίστα ασθενών
dead_humans = [] #λίστα νεκρών
populate(humans,N)
patient0 = humans.pop(r.randint(0,N-1)) #επιλογή ασθενή 0
patient0.isSick = True #τον κάνουμε ασθενή
sick_humans.append(patient0) #τον προσθέτουμε στην λίστα των αρρώστων


#pandemic starts ! lets simulate the first 30 days :
#studies have shown that people typically have around 12 to 25 face-to-face interactions per day
contacts = 4

days = []
sick_number = []
for day in range(60):
    total_contacts = contacts*len(sick_humans)
    for i in range(total_contacts):
        if len(humans) > 0:
            pos = r.randint(0,len(humans) - 1)
            randomPerson = humans[pos]
            randomPerson.contact()
            if randomPerson.isSick:
                humans.pop(pos)
                sick_humans.append(randomPerson)
    day_passes(humans,sick_humans,dead_humans)
    days.append(day + 1)
    sick_number.append(len(sick_humans))
    print(len(humans), len(sick_humans), len(dead_humans))

plt.plot(days,sick_number)
plt.show()