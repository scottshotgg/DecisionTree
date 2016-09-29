import os 
from sklearn import tree

mushrooms = open("mush_train.data")
y = []
x = []

for line in mushrooms:
	#print line

	array = line.split(',')
	array[len(array) - 1] = array[len(array) - 1].replace('\r\n', '')

	for l in range(len(array)):
		array[l] = ord(array[l])

	print array

	y.append(array[0])
	x.append(array[1:])


#print x
#print y

mushTree = tree.DecisionTreeClassifier(criterion="entropy")

mushTree = mushTree.fit(x, y)

print "\n\n"

chararray = []
for char in x[100]:
	chararray.append(chr(char))
print chararray

print chr(y[100])

print "\n\n"

print chr(mushTree.predict([x[100]]))