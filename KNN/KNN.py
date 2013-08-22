from numpy import *
import operator
def  creatDateSet():
    group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    label = ["A",'A','B','B']
    return group,label

   
def classify0(inx,dataSet,label,k):
    dataSetSize = dataSet.shape[0]
    diffMat = tile(inx,(dataSetSize,1)) - dataSet
    sqDiffMat = diffMat**2
    sqDistances = sqDiffMat.sum(axis = 1)
    distances = sqDistances**0.5
    sortedDistIndicies = distances.argsort()
    classCount = {}
    for i in range(k):
        voteIlabel = label[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
    sortedClassCount = sorted(classCount.iteritems(), key = operator.itemgetter(1),reverse=True)
    return sortedClassCount[0][0]

if __name__ == "__main__":
    group , label = creatDateSet()
    print group
    print classify0([3,3],group,label,2)
