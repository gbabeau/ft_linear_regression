import array as arr
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def  estimateprice(teta0, teta1, milleage):
    #print(teta0 +  (teta1* float(milleage)))
    return (teta0 +  (teta1* float(milleage)))

def estimatetmpteta0(teta0,teta1, km, price,lear):
    tmp = 0
    for index in range(len(km)):
        tmp += estimateprice(teta0, teta1, km[index]) - price[index]
    return (tmp * float(lear / float(len(km))))

def estimatetmpteta1(teta0,teta1, km, price,lear):
    tmp = 0
    for index in range(len(km)):
        tmp += (estimateprice(teta0, teta1, km[index]) - price[index]) * float(km[index])
    return (tmp * float(lear / float(len(km))))


data = open("data.csv", "r")
la = (data.read()).split()
data.close()
km  = []
price  = []
l1  = []
l2  = []
l1li = [0,0]
l2li = [0,0]
lear = 0.6
tmp0 = 0.0
tmp1 = 0.0
teta0 = 0.0
teta1 = 0.0
for index in range(len(la)-1):
        v = la[index+1].split(',')
        l1.append(int(v[0]))
        l2.append(int(v[1]))
        if  index == 0 :
            l1li[0] = int(v[0])
            l1li[1] = int(v[0])
            l2li[0] = int(v[1])
            l2li[1] = int(v[1])
        if int(v[0]) < l1li[0] :
            l1li[0] = int(v[0]) 
        if int(v[0]) > l1li[1] :
            l1li[0] = int(v[0])
        if int(v[1]) < l2li[0] :
            l2li[0] = int(v[1]) 
        if int(v[1]) > l2li[1] :
            l2li[1] = int(v[1]) 
        
for index in range(len(la)-1):
    v = la[index+1].split(',')
    km.append((l1[index] - l1li[0])/ (l1li[1] - l1li[0]))
    price.append((l2[index] - l2li[0])/ (l2li[1] - l2li[0]))
for index in range(1000):
    tmp0 -= estimatetmpteta0(teta0, teta1, km, price,lear)
    tmp1 -= estimatetmpteta1(teta0, teta1, km, price,lear)
    teta0 = tmp0
    teta1 = tmp1
    #print("teta0 : ",teta0,", teta1 : ",teta1)
plt.scatter(km,price)
slope, intercept, r, p, std_err = stats.linregress(km, price)

def myfunc(x):
  return slope * x + intercept
print("les valeur sont", teta0, teta1, intercept, slope)


mymodel = list(map(myfunc, km))
plt.plot( [km[0], km[-1]],[myfunc(km[0]),myfunc(km[-1])])
plt.plot([km[0], km[-1]],[estimateprice(teta0, teta1, km[0]), estimateprice(teta0, teta1, km[-1])], color = 'green', linestyle = 'solid')
plt.ylabel("price")
plt.xlabel("km")
plt.show()
slope, intercept, r, p, std_err = stats.linregress(l1, l2)
plt.scatter(l1,l2)
nteta1 = teta1 / ((l1li[1]- l1li[0])/ (l2li[1] - l2li[0]))
nteta0 = (teta0 * (l2li[1] - l2li[0])) + l2li[0] - nteta1 * l1li[0]
plt.plot( [0, l1li[1]],[myfunc(0),myfunc(l1li[-1])])
plt.plot([0,  l1li[1]],[estimateprice(nteta0 , nteta1, 0), \
                            estimateprice(nteta0, nteta1, l1li[1])], \
                            color = 'green', linestyle = 'solid')
plt.ylabel("price")
plt.xlabel("km")
print("dif =",  estimateprice(nteta0 , nteta1, 0)- myfunc(0),\
                 estimateprice(nteta0 , nteta1, l1li[1]) - myfunc(l1li[1]))
plt.show()
fin = open("teta.csv","w")
fin.write("teta0,teat1\n")
valeur = "%f,%f\n" % (nteta0,nteta1)
fin.write(valeur)