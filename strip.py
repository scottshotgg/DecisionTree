import os

training = open("spam_train.data", "r")

trainingsplit = training.read().split("\r\n")
print trainingsplit
print len(trainingsplit)
x = []
y = []

for i in range(len(trainingsplit) - 1):
	trainingsplit[i] = trainingsplit[i].split(",")
	x.append(trainingsplit[i][0:len(trainingsplit[i]) - 1])
	y.append(trainingsplit[i][len(trainingsplit[i]) - 1:])


print x, y

#trainingstrip = open("training_strip.data", "w")
#trainingstrip.write("\n".join(trainingsplit))