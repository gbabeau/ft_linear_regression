import array as arr
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


l1= []
l2 = []
l1li = [0,0]
l2li = [0,0]
km = [] 
price = []
lear = 0.5
tmp0 = 0.0
tmp1 = 0.0
teta0 = 0.0
teta1 = 0.0
error = []



def  estimateprice(teta0, teta1, milleage):
    return (teta0 +  (teta1* milleage))

def estimatetmpteta0(teta0,teta1, km, price,lear):
    tmp = 0
    for index in range(len(km)):
        tmp += estimateprice(teta0, teta1, km[index]) - price[index]
    return (tmp * lear / len(km))

def estimatetmpteta1(teta0,teta1, km, price,lear):
    tmp = 0
    for index in range(len(km)):
        tmp += (estimateprice(teta0, teta1, km[index]) - price[index]) * float(km[index])
    return (tmp * lear / len(km))

def error_price(teta0, teta1, km, price,lear):
    tmp = 0
    for index in range(len(km)):
        tmp += (estimateprice(teta0, teta1, km[index]) - price[index]) ** 2
    return tmp / len(km)

def init_valeur_aboslue(las):
    global l1li, l2li
    for index in range(len(las)-1):
        v = las[index+1].split(',')
        l1.append(int(v[0]))
        l2.append(int(v[1]))
    l1li[0] = min(l1)
    l2li[0] = min(l2)
    l1li[1] = max(l1)
    l2li[1] = max(l2)
    return las[0].split(',')

def init_valeur_relative(l1, l2, l2li, l1li):
    for index in range(len(l1)):
        km.append((l1[index] - l1li[0])/ (l1li[1] - l1li[0]))
        price.append((l2[index] - l2li[0])/ (l2li[1] - l2li[0]))

def show_relative():
    plt.scatter(km,price)
    plt.plot([min(km), max(km)],[estimateprice(teta0, teta1, min(km)), estimateprice(teta0, teta1, max(km))], color = 'green', linestyle = 'solid')
    plt.ylabel(index[0])
    plt.xlabel(index[1])
    plt.show()


def show_absolue():
    plt.scatter(l1,l2)
    plt.plot([0,  l1li[1]],[estimateprice(nteta0 , nteta1, 0), \
                            estimateprice(nteta0, nteta1, l1li[1])], \
                            color = 'green', linestyle = 'solid')
    plt.ylabel(index[0])
    plt.xlabel(index[1])
    plt.show()

def show_error():
    plt.plot(error)
    plt.show()

def estimate_teta(teta0, teta1):
    tmp0 = 0
    tmp1 = 0
    while len(error) < 2 or  error[-2] - error[-1] != 0.0 :
        tmp0 -= estimatetmpteta0(teta0, teta1, km, price,lear)
        tmp1 -= estimatetmpteta1(teta0, teta1, km, price,lear)
        error.append(error_price(teta0, teta1, km, price,lear))
        teta0 = tmp0
        teta1 = tmp1
    nteta1 = teta1 / ((l1li[1]- l1li[0])/ (l2li[1] - l2li[0]))
    nteta0 = (teta0 * (l2li[1] - l2li[0])) + l2li[0] - nteta1 * l1li[0]
    error.append(error_price(teta0, teta1, km, price,lear))
    return nteta0, nteta1, teta0, teta1

data = open("data.csv", "r")
index = init_valeur_aboslue((data.read()).split())
data.close()
init_valeur_relative(l1, l2, l2li, l1li)
nteta0 , nteta1, teta0 , teta1 = estimate_teta(teta0, teta1)
show_relative()
show_absolue()
show_error()
fin = open("teta.csv","w")
fin.write("teta0,teat1\n")
valeur = "%f,%f\n" % (nteta0,nteta1)
fin.write(valeur)
fin.close()