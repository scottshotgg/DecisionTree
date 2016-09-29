import os 
import math
#from sklearn import tree

# Used for stripping the file
def stripFile(filename):
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
def countYN(data):
	for classs in data['y']:
		if classs == ord("p"):
			array[1] += 1
		elif classs == ord("e"):
			array[0] += 1
	return array


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

def calculateExpectedValues(array, probarray):
	print array
	for value in range(len(array)):
		print "arrayvalue: ", array[value]
		if probarray[value] == 0:
			print probarray[value]
			for line in range(len(data['x'])):
				print chr(data['x'][line][value])
				#if chr(data['x'][line][value]) == array[value]:
					#expectedvalue = data['y'][line]
					#print expectedvalue
					#break




data = stripFile("mush_train.data")

for r in range(5):

	array = [0] * 2

	array = countYN(data)

	print "counted data", array

	base = entropy(float(array[1]), float(array[0]))

	stuffarray = calculateInformationGain(data)

	#print stuffarray[0]
	#print base

	choice = calculateNextDecision(base, stuffarray[0])

	attprobability = stuffarray[1][choice - 1]
	print attprobability

	highestIndex = 0
	highest = 1
	highestincr = 0

	for value in attprobability:
		if value < highest and value != 0:
			highest = value
			highestIndex = highestincr

		highestincr += 1

	print highestIndex
	print highest


	splitvaluearray = stuffarray[2][choice - 1]

	print "split value is", splitvaluearray[highestIndex]
	print attprobability

	# need a function to calculate the expected values
	#calculateExpectedValues(splitvaluearray, attprobability)

	print "\n"
	valueincr = 0
	for value in splitvaluearray:
		if attprobability[valueincr] == 0:
			print value
			vary = 0
			for nextvalue in data['x']:
				#print nextvalue
				if chr(nextvalue[choice - 1]) == value:
					#print value
					expectedval = data['y'][vary]
					print "expected value", chr(expectedval)
					vary += 1
					break
				vary += 1
		valueincr += 1


	newdata = {}
	datarrayx = []
	datarrayy = []
	for line in range(len(data['x'])):
		#print "char", chr(data['x'][line][choice - 1])
		#print "splitvaluearray char", splitvaluearray[highestIndex]
		if chr(data['x'][line][choice - 1]) == splitvaluearray[highestIndex]:
			#print data['x'][line]
			datarrayx.append(data['x'][line])
			datarrayy.append(data['y'][line])

	newdata['x'] = datarrayx
	newdata['y'] = datarrayy

	print len(newdata['x']), len(newdata['y'])
	data = newdata

#chooseAttribute(choice, data)

#array = countYN()







