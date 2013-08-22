#from numpy import *
import matplotlib.pyplot as plt
import random
import numpy as np



def makedata(r,w,num,buer,ox,oy,):
    x = np.array([(random.random()-0.5)*2*r for i in range(num)])
    y = []
    for j in x:
        R = r - random.random()*(r-w)
        while R < abs(j) :
            R = r - random.random()*(r-w)
        y.append((buer)*(R**2 - j**2)**0.5+oy)
    x = x + ox
    return x,y

 #creat data 
datax , datay = makedata(20,10,1000,1,0,0)
data = [[datax[i],datay[i]] for i in range(len(datax))]
datax2 , datay2 = makedata(25,6,1000,-1,4,10)
data.extend([[datax2[i],datay2[i]] for i in range(len(datax2))])

def euclidean(p,q):
	sumSq=0.0
	# add up the squared differences
	for i in range(len(p)):
		try:
			sumSq+=(p[i]-q[i])**2
		except:pass
	# take the square root
	return (sumSq**0.5)


def pearson(x,y):
	n=len(x)
	vals=range(n)
	sumx=sum([float(x[i]) for i in vals])
	sumy=sum([float(y[i]) for i in vals])
	sumxSq=sum([x[i]**2.0 for i in vals])
	sumySq=sum([y[i]**2.0 for i in vals])
	pSum=sum([x[i]*y[i] for i in vals])
	num=pSum-(sumx*sumy/n)
	den=((sumxSq-pow(sumx,2)/n)*(sumySq-pow(sumy,2)/n))**.5
	if den==0: return 0
	r=num/den
	return r


def point(data):
	n = len(data)

	if n == 0:return [random.random()*20,random.random()*20] ;print "--------------------------------->>>>>>"
	else :
		num = np.sum(data,axis=0)
		new_point = num/n
		return new_point

def k_means(data,k):
	n = len(data)
	l = len(data[0])
	k_contain = [[] for i in range(k)]
	data_max = max([data[i][j] for i in range(n) for j in range(l) ])
	data_min = min([data[i][j] for i in range(n) for j in range(l) ])
	diff = data_max - data_min
	k_point = [[round(diff * random.random() + data_min,2) for i in range(l)] for j in range(k) ]

	last_k_contain = []
	while k_contain != last_k_contain:
		for each in data:
			distance = [euclidean(each,j) for j in k_point]
			k_contain[np.argmin(distance)].append(each)
		if last_k_contain == k_contain:
			break
		last_k_contain = k_contain
		k_point = [point(k_contain[i]) for i in range(k)]
		k_contain = [[] for i in range(k)]
	return k_contain , k_point



for i in range(4,10):
	get_data , k_point = k_means(data,i)


	print k_point
	for num in k_point:
		plt.plot(num[0],num[1],"gH")

	
	
	for i in range(i):
		color = "#"+str(hex(random.randint(int("111111",16),int("ffffff",16)))[2:])
		print color
		for num in get_data[i]:
			plt.plot(num[0],num[1],'^',color =color)
	plt.show()

# for i in range(100):
# 	if len(hex(random.randint(int("111111",16),int("ffffff",16)))[2:])<6:
# 		print "---------------------"