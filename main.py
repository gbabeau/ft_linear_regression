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
    print(tmp)
    print(tmp * float(lear / float(len(km))))
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
lear = 1
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
print(km)
print(price)
for index in range(100):
    tmp0 -= estimatetmpteta0(teta0, teta1, km, price,lear)
    print(tmp0)
    tmp1 -= estimatetmpteta1(teta0, teta1, km, price,lear)
    print(tmp1)
    teta0 = tmp0
    teta1 = tmp1
    #print("teta0 : ",teta0,", teta1 : ",teta1)
print(len(km))
print(len(price))
plt.scatter(km,price)
print(price[0])
slope, intercept, r, p, std_err = stats.linregress(km, price)

def myfunc(x):
  return slope * x + intercept
print(teta0)
print(teta1)

mymodel = list(map(myfunc, km))
plt.plot( [km[0], km[-1]],[myfunc(km[0]),myfunc(km[-1])])
plt.plot([km[0], km[-1]],[estimateprice(teta0, teta1, km[0]), estimateprice(teta0, teta1, km[-1])], color = 'green', linestyle = 'solid')
plt.plot([km[0], km[-1]], [price[0], price[-1]], color = 'red', linestyle = 'solid')
plt.ylabel("price")
plt.xlabel("km")
plt.show()
