from math import log
def calcShannonEnt(dataSet):
	shannonEnt = 0.0
	numEntries = len(dataSet)
	labelCounts = {}
	for featVec in dataSet:
		currenLabel = featVec[-1]
		labelCounts[currenLabel] = labelCounts.get(currenLabel,0)+1
	for key in labelCounts:
		prob = float(labelCounts[key])/numEntries
		shannonEnt -= prob * log(prob,2)
	return shannonEnt
def splitDataSet(dataSet, axis, value):
	retDataSet = []
	for featVec in dataSet:
		if featVec[axis] == value:
			reducedFeatVec = featVec[:axis]
			reducedFeatVec.extend(featVec[axis+1:])
			retDataSet.append(reducedFeatVec)
	return retDataSet

print calcShannonEnt([[1, 1, 'maybe'], [1, 1, 'yes'], [1, 0, 'no'], [0, 1, 'no'], [0, 1, 'no']])