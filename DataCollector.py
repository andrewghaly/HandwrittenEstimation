import json
from ImageAverage import imageToAnalyze
from random import randint
import numpy as np
import matplotlib.pyplot as plt
values = []
randHand = randint(1,3)
print randHand
#randHand = 1
for x in range(0,100):
    randValue = randint(1,50)


    if(randHand == 1):
        #print("Actual Hand: Andrew")
        imageAverage = imageToAnalyze('C:\\Users\\ghalya\\Pictures\\Hands\\Ghaly_hand\\andrew_r_' + str(randValue) + '.png')
    elif(randHand == 2):
       # print("Actual Hand: Albert")
        imageAverage = imageToAnalyze('C:\\Users\\ghalya\\Pictures\\Hands\\Saunders_hand\\al_r_' + str(randValue) + '.png')
    elif(randHand == 3):
       # print("Actual Hand: Tom")
        imageAverage = imageToAnalyze('C:\\Users\\ghalya\\Pictures\\Hands\\DeMarco_hand\\tom_r_' + str(randValue) + '.png')

    count = xTotal = yTotal = 0
    for i, j in imageAverage:
        xTotal += i
        yTotal += j
        count += 1

    #print "[", xTotal/count, ",", yTotal/count, "]"

    with open('aggregate_data', 'r') as data_file:
        data = json.load(data_file)

    closestAverage = 10000
    person = ""
    if abs((data["Andrew"]["average"][0] - xTotal/count) + (data["Andrew"]["average"][1] - yTotal/count)) < closestAverage:
        closestAverage = abs((data["Andrew"]["average"][0] - xTotal/count) + (data["Andrew"]["average"][1] - yTotal/count))
        person = "Andrew"

    if abs((data["Bert"]["average"][0] - xTotal/count) + (data["Bert"]["average"][1] - yTotal/count)) < closestAverage:
        closestAverage = abs((data["Bert"]["average"][0] - xTotal/count) + (data["Bert"]["average"][1] - yTotal/count))
        person = "Bert"

    if abs((data["Tom"]["average"][0] - xTotal/count) + (data["Tom"]["average"][1] - yTotal/count)) < closestAverage:
        closestAverage = abs((data["Tom"]["average"][0] - xTotal/count) + (data["Tom"]["average"][1] - yTotal/count))
        person = "Tom"

    if person is "Andrew":
        values.append(1)
    elif person is "Bert":
        values.append(2)
    elif person is "Tom":
        values.append(3)
    #with open('aggregate_data', 'w') as f:
       # json.dump(data, f)

        #pprint(data["Andrew"]["average"])


def createHist(values):
    hist, bin_edges = np.histogram(values)
    plt.bar(bin_edges[:-1], hist, width=.25, color="red")
    plt.xlim(1, 3.5)
    plt.show()
    print values
createHist(values)