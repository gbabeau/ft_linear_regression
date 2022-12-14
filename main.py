import array as arr
import numpy as np
import matplotlib.pyplot as plt



def  estimateprice(teta0, teta1, milleage):
    return (teta0 +  teta1* milleage)


data = open("data.csv", "r")
la = (data.read()).split()
data.close()
km  = []
price  = []
lear = 0.07
tmp0 = 0
tmp1 = 0
teta0 = 0.0
teta1 = 0.0
for index in range(len(la)-1):
        v = la[index+1].split(',')
        km.append(int(v[0]))
        price.append(int(v[1]))
print(km)
print(price)

for i in range(2):
    for index in range(len(km)):
        tmp0 += estimateprice(teta0, teta1, km[index]) - price[index]
        print(estimateprice(teta0, teta1, km[index]) - price[index])
        tmp1 += (estimateprice(teta0, teta1, km[index]) - price[index])  * price[index]
    print("tmp0 : ",tmp0)
    print("tmp1 : ",tmp1)
    tmp0 *= lear/len(km)
    tmp1 *= lear/len(km)
    teta0 += tmp0
    teta1 += tmp1
    print("teta0 : ",teta0)
    print("teta1 : ",teta1)
    print(len(km))
plt.scatter(price, km)
plt.plot([estimateprice(teta0, teta1, km[0]), estimateprice(teta0, teta1, km[-1])], [km[0], km[-1]], color = 'green', linestyle = 'solid')
plt.plot([estimateprice(teta0, teta1, km[index]), price[-1]], [km[0], km[-1]], color = 'red', linestyle = 'solid')
plt.show()
