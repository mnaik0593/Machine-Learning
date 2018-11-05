import csv
import random
import math
import operator

Set1 = []
Set2 = []
Set3 = []
Set4 = []
Set5 = []

def euclideanDistance(instance1, instance2, length):
	distance = 0
	for x in range(length):
		distance += pow((instance1[x] - instance2[x]), 2)
	return math.sqrt(distance)

def getNeighbors(trainingSet, testInstance, k):
	distances = []
	length = len(testInstance)-1
	for x in range(len(trainingSet)):
		dist = euclideanDistance(testInstance, trainingSet[x], length)
		distances.append((trainingSet[x], dist))
	distances.sort(key=operator.itemgetter(1))
	neighbors = []
	for x in range(k):
		neighbors.append(distances[x][0])
	return neighbors

def getResponse(neighbors):
	classVotes = {}
	for x in range(len(neighbors)):
		response = neighbors[x][-1]
		if response in classVotes:
			classVotes[response] += 1
		else:
			classVotes[response] = 1
	sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True)
	return sortedVotes[0][0]

def getAccuracy(testSet, predictions):
	correct = 0
	for x in range(len(testSet)):
		if testSet[x][-1] == predictions[x]:
			correct += 1
	return (correct/float(len(testSet))) * 100.0

def flattenArrayN(my_nest):
    my_flat = [] 
    for i in my_nest:
        for j in i:
            my_flat.append(j)
    return my_flat 

with open('iris.csv', 'r') as csvfile:
    lines = csv.reader(csvfile)
    dataset = list(lines)
    for x in range(len(dataset)):
        for y in range(4):
            dataset[x][y] = float(dataset[x][y])
        rint = random.random()     
        if  rint < 0.2:
             Set1.append(dataset[x])
        if  rint >= 0.20 and rint < 0.40:
            Set2.append(dataset[x])
        if  rint >= 0.40 and rint < 0.60:
            Set3.append(dataset[x])
        if  rint >= 0.60 and rint < 0.80:
            Set4.append(dataset[x])
        if  rint >= 0.80:
            Set5.append(dataset[x])

testSet = Set1
trainingSet1 = Set2,Set3,Set4,Set5
trainingSet = flattenArrayN(trainingSet1)
predictions=[]
k = 4
for x in range(len(testSet)):
    neighbors = getNeighbors(trainingSet, testSet[x], k)
    result = getResponse(neighbors)
    predictions.append(result)
    print('> predicted=' + repr(result) + ', actual=' + repr(testSet[x][-1]))
accuracy1 = getAccuracy(testSet, predictions)
print('Accuracy: ' + repr(accuracy1) + '%')

testSet = Set2
trainingSet1 = Set1,Set3,Set4,Set5
trainingSet = flattenArrayN(trainingSet1)
predictions=[]
k = 4
for x in range(len(testSet)):
    neighbors = getNeighbors(trainingSet, testSet[x], k)
    result = getResponse(neighbors)
    predictions.append(result)
    print('> predicted=' + repr(result) + ', actual=' + repr(testSet[x][-1]))
accuracy2 = getAccuracy(testSet, predictions)
print('Accuracy: ' + repr(accuracy2) + '%')

testSet = Set3
trainingSet1 = Set1,Set2,Set4,Set5
trainingSet = flattenArrayN(trainingSet1)
predictions=[]
k = 4
for x in range(len(testSet)):
    neighbors = getNeighbors(trainingSet, testSet[x], k)
    result = getResponse(neighbors)
    predictions.append(result)
    print('> predicted=' + repr(result) + ', actual=' + repr(testSet[x][-1]))
accuracy3 = getAccuracy(testSet, predictions)
print('Accuracy: ' + repr(accuracy3) + '%')

testSet = Set4
trainingSet1 = Set1,Set3,Set2,Set5
trainingSet = flattenArrayN(trainingSet1)
predictions=[]
k = 4
for x in range(len(testSet)):
    neighbors = getNeighbors(trainingSet, testSet[x], k)
    result = getResponse(neighbors)
    predictions.append(result)
    print('> predicted=' + repr(result) + ', actual=' + repr(testSet[x][-1]))
accuracy4 = getAccuracy(testSet, predictions)
print('Accuracy: ' + repr(accuracy4) + '%')

testSet = Set5
trainingSet1 = Set1,Set3,Set4,Set2
trainingSet = flattenArrayN(trainingSet1)
predictions=[]
k = 4
for x in range(len(testSet)):
    neighbors = getNeighbors(trainingSet, testSet[x], k)
    result = getResponse(neighbors)
    predictions.append(result)
    print('> predicted=' + repr(result) + ', actual=' + repr(testSet[x][-1]))
accuracy5 = getAccuracy(testSet, predictions)
print('Accuracy: ' + repr(accuracy5) + '%')

final_accuracy = (accuracy1+accuracy2+accuracy3+accuracy4+accuracy5)/5
print('final',final_accuracy )
