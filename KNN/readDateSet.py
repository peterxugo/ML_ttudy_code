from numpy import *
from KNN import classify0


def readDate(filename):
	date = []
	label = []
	i = 1
	subdate = []
	fp = open(filename)
	for line in fp.readlines():
		if i <= 32 :
			# subsubdate = []
			for each in line[:32]:
				subdate.append(int(each))
			i += 1
		else:
			date.append(subdate)
			label.append(int(line[1]))
			i = 1
			subdate = []
	return array(date),array(label)
if __name__ == "__main__":
	trdate , trlabel = readDate("optdigits-orig.tra")
	tsdate , tslabel = readDate("optdigits-orig.cv")
	length = len(tsdate)
	error = 0
	for i in range(length):
		getlabel = classify0(tsdate[i],trdate,trlabel,3)
		if getlabel != tslabel[i] :
			error += 1.0
			print getlabel , tslabel[i]
	print error/length
	