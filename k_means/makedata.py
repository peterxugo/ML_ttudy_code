from pylab import *
import numpy as np
from random import random


    
    
def makedata(r,w,num,buer,ox,oy,):



    x1 = np.array(np.arange(-r,r+0.01,0.01))
    y1 = (buer)*(r**2 - x1**2)**0.5+oy
    x1 = x1+ox

    x2 = np.array(np.arange(-w,w+0.01,0.01))
    y2 = (buer)*(w**2 - x2**2)**0.5+oy
    x2 = x2+ox
    
    x = np.array([(random()-0.5)*2*r for i in range(num)])
    y = []
    for j in x:
        R = r - random()*(r-w)
        while R < abs(j) :
            R = r - random()*(r-w)
        y.append((buer)*(R**2 - j**2)**0.5+oy)
    x = x + ox



    plot(x,y,'r.')
    plot(x1,y1,'b-')
    plot(x2,y2)
    ax = gca()
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_position(('data',0))
    ax.yaxis.set_ticks_position('left')
    ax.spines['left'].set_position(('data',0))
    return list(x),y
    
    



    
if __name__ == '__main__':
    x1,y1 = makedata(10,6,1000,1,0,0,)
    x2,y2 = makedata(10,6,1000,-1,5,-5)
    x = x1.extend(x2)
    y = y1.extend(y2)
    plot(x,y,'ro')
    show()
