import os 
import math
import sys
#from sklearn import tree

# Used for stripping the file
def stripFile(filename, percentage):
	mushrooms = open(filename)
	y = []
	x = []

	for line in mushrooms:
		#print line

		array = line.split(',')
		array[len(array) - 1] = array[len(array) - 1].replace('\r\n', '')
		print array

		for l in range(len(array)):
			array[l] = ord(array[l])

		y.append(array[0])
		x.append(array[1:])

	if percentage != 1:
		amount = int(len(y) * float(percentage))
		print len(y)
		print "amount", amount

		newy = y[0:amount]
		newx = x[0:amount]

		return {'y': newy, 'x': newx}

	return {'y': y, 'x': x}


# Used for determining the next decision that we need to split on
def calculateNextDecision(base, logarray):
	highestGain = 0
	highestGainIndex = 0
	gaininc = 1
	for value in logarray:
		if value is not 0:
			gain = base[5] - value
			if gain > highestGain:
				highestGain = gain
				highestGainIndex = gaininc
			#print gaininc, "Gain:", gain, "Highest Gain:", highestGain
			print "%2d" % gaininc, "Gain: %17.10f" % gain, "\nHighest Gain: %10.10f" % highestGain
			print "\n" 
			gaininc += 1
	print "we would pick attribute", highestGainIndex

	#print logarray

	return highestGainIndex


# Used for calculating the entropy values
def entropy(yes, no):
	total = no + yes
	yescalc = 0
	nocalc = 0
	nt = 0
	yt = 0
	print yes, no
	if yes != 0:
		yt = yes / total
		yescalc = yt * math.log(yt, 2.0)
	if no != 0:
		nt = no / total
		nocalc = nt * math.log(nt, 2.0)

	added = -(yescalc + nocalc)


	print nocalc
	print yescalc
	print added
	print total / len(data['x'])
	final = added * total / len(data['x'])
	print final
	arraythat = [total, nt, yt, nocalc, yescalc, added]
	print arraythat

	return arraythat


# Used for counting the Yes and No values from a 2xn array containing the classes and attributes
def countYN(datapassed):
	arr = [0, 0]
	for classs in datapassed['y']:
		if classs == ord("p"):
			arr[1] += 1
		elif classs == ord("e"):
			arr[0] += 1
	return arr


# Used for calculating the seperating the classes and counting them, probably way more complex than it needs to be
def calculateInformationGain(data):
	featureCount = [[dict() for y in range(2)] for x in range(22)]
	#for feature in data['x'][len(data['x'][0])]:
	print "featureCount:", featureCount
	raw_input("me")
	l = 0
	for line in data['x']:
		#print len(data['x'])
		#print line
		for feature in range(len(line)):
			#print "\"", chr(data['y'][l]), "\""
			#print type(data['y'][0])

			try:
				if data['y'][l] is ord("p"):
					featureCount[feature][1][chr(line[feature])] += 1
				else:
					featureCount[feature][0][chr(line[feature])] += 1

			except KeyError:
				if data['y'][l] is ord("p"):
					featureCount[feature][1][chr(line[feature])] = 1
				else:
					featureCount[feature][0][chr(line[feature])] = 1

			#raw_input()
			#print featureCount[feature][0]
			#print featureCount[feature][1]
		#print featureCount
		l += 1
	print "\n"
	logarrays = []
	sumvararray = []
	featarrays = []
	itervarthatiamusing = 1
	for feature in featureCount:
		print "FEATURE", itervarthatiamusing
		itervarthatiamusing += 1
		print "feature", feature
		print "\n"

		logarray = [0] * 22
		itervalue = 0
		
		# get all the attributes from feature[0]
		featarray = []
		attributecounter = 0
		for attribute in feature[0]:
			if attribute not in featarray:
				print attribute
				featarray.append(attribute)
			attributecounter += 1
		print featarray

		# get all the attributes from feature[1]
		for attribute in feature[1]:
			if attribute not in featarray:
				print attribute
				featarray.append(attribute)
			attributecounter += 1
		print featarray
		featarrays.append(featarray)

		yes = 0
		no = 0
		for feat in featarray:
			try:
				yes = float(feature[1][feat])
				try:
					no = float(feature[0][feat])
				except KeyError:
					print "Exception at no = 0"
					no = 0

			except KeyError:
				print "Exception at yes = 0"
				yes = 0
				try:
					no = float(feature[0][feat])
				except:
					no = 0
					print "why are you trying to do this"

			print "\n", feat
			entropycalc = entropy(yes, no)
			
			logarray[itervalue] = entropycalc[5] * entropycalc[0] / len(data['x'])

			itervalue += 1
			sumvar = 0

		logarrays.append(logarray)

		print "logarrays:", logarrays
		for value in logarray:
			sumvar += value
		print "sumvar", sumvar
		sumvararray.append(sumvar)

		print "\n"
				 # calculation is already decided
	print sumvararray
	return [sumvararray, logarrays, featarrays]


#def chooseAttribute(choice, data):

def findExpectedClass(choice, var):
	total = 0
	cumulativeprob = 0
	for line in range(len(data['x'])):
		#print chr(data['x'][line][choice - 1])
		if chr(data['x'][line][choice - 1]) == var:
			total += 1
			if chr(data['y'][line]) == 'p':
				cumulativeprob += 1
			
				#if chr(data['x'][line][value]) == array[value]:
					#expectedvalue = data['y'][line]
					#print expectedvalue
					#break

			#print "cumulativeprob!!!", cumulativeprob
	probability = float(cumulativeprob) / float(total)
	print "PROBABILITY", probability
	if probability > .5:
		return 'p'
	else:
		return 'e'

def findBranches(choice, splitvaluearray, attprobability):
	branches = {}
	expectedbranches = {}

	valueinc = 0
	for value in splitvaluearray:
		if attprobability[valueinc] == 0:
			expected = findExpectedClass(choice, splitvaluearray[valueinc])
			expectedbranches[value] = expected
			print "expected class for", value, "is", expected
		else:
			branches[value] = attprobability[valueinc]

		valueinc += 1

	print expectedbranches
	return [branches, expectedbranches]


def findData(data, choice, value):

	arrayx = []
	arrayy = []

	for line in range(len(data['x'])):
		if chr(data['x'][line][choice - 1]) == value:
			arrayx.append(data['x'][line])
			arrayy.append(data['y'][line])

	return {'x': arrayx, 'y':arrayy}


def computeBranches(data, choice, branches):
	print branches

	branchData = {}
	for value in branches:
		print value
		branchData[value] = findData(data, choice, value)

	return branchData


def sequence(branche, level):
	calculateInformationGain(branche)
	arrayyy = countYN(branche)
	print "counted data", arrayyy
	based = entropy(float(arrayyy[1]), float(arrayyy[0]))
	stuffedarray = calculateInformationGain(branche)
	choice = calculateNextDecision(based, stuffedarray[0])
	attprobability = stuffedarray[1][choice - 1]
	splitvaluearray = stuffedarray[2][choice - 1]
	print splitvaluearray
	print attprobability
	branchesFound = findBranches(choice, splitvaluearray, attprobability)

	print tree
	if len(branchesFound[0]) == 0:
		print "\n\n\n\n\n\n\n END OF THIS SUBTREE \n\n\n\n\n\n\n"
		print "\n\n\n\n\n\LEVEL", level,"\n\n\n\n\n"
		try:
			tree['Level ' + str(level)][str(choice)] = ["-1", branchesFound[1]]
		except KeyError:
			try:
				tree['Level ' + str(level)].append(str(choice))
				tree['Level ' + str(level)][str(choice)] = ["-1", branchesFound[1]]
			except KeyError:
				tree['Level ' + str(level)] = {}
				tree['Level ' + str(level)][str(choice)] = {}
				tree['Level ' + str(level)][str(choice)] = ["-1", branchesFound[1]]

	else:	
		branchesComputered = computeBranches(branche, choice, branchesFound[0])

		print "BRANCHES: ", len(branchesComputered)
		for branc in branchesComputered:
			print "choice", str(choice)
			print "array", splitvaluearray
			try:
				tree['Level ' + str(level)][str(choice)].append([branc, branchesFound[1]]) 
			except KeyError:
				tree['Level ' + str(level)] = {}
				tree['Level ' + str(level)][str(choice)] = [branc, branchesFound[1]] 
			print "\n\n\n\n\n\LEVEL", level ,"\n\n\n\n\n"
			sequence(branchesComputered[branc], level + 2)


def classify(datax, datay):
	searcharray = [0, 2, 4, 6]
	for level in searcharray:
		tl = tree['Level ' + str(level)]
		print tl
		for attribute in tl.keys():
			end = 0
			print "level", level, attribute
			splitchar = tl[str(attribute)][0]
			predicted = tl[str(attribute)][1]

			print "predicted", predicted
			print "split char", splitchar

			lineatt = chr(datax[int(attribute) - 1])
			print "line attribute", lineatt
			if lineatt in predicted:
				print "predicted", predicted[lineatt]
				print chr(datay)
				if predicted[lineatt] == chr(datay):
					return 1
				else:
					return 0

			elif lineatt == splitchar:
				print "going to next level\n"
	import random
	return random.uniform(0, 1)


def calculateAccuracy(data):
	print "Testing ACCURACY: "

	print len(data['x'])


	#level = 0
	cumulativeprob = 0
	for line in range(len(data['x'])):
		cumulativeprob += classify(data['x'][line], data['y'][line])
		print cumulativeprob
	#classify(data['x'][0], data['y'][0])
	accuracy = 100 * float(cumulativeprob) / float(len(data['y']))

	return accuracy


# "main"

print sys.argv
percentage = float(sys.argv[1])

tree = {}

data = stripFile("mush_train.data", percentage)

branchesComputed = data
level = 0

print "\n\n\n\n\n\LEVEL", level ,"\n\n\n\n\n"
sequence(branchesComputed, level)

level = 0
for value in tree:
	print "Level", level, tree['Level ' + str(level)]
	print "\n"
	level += 2

raw_input("Press enter for training data")

print "Training accuracy:"
acc = calculateAccuracy(data)
print "\n", acc, "%"

raw_input("Press enter for testing data")

data = stripFile("mush_test.data", 1)

print len(data['y'])

print "Training accuracy:"
acc = calculateAccuracy(data)
print "\n", acc, "%"




print tree
