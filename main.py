import array as arr
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

class linear_regression:
    def _init_(self, data):
        for index in range(len(las)-1):
            v = las[index+1].split(',')
            self.l1.append(int(v[0]))
            self.l2.append(int(v[1]))
        self.l1li[0] = min(l1)
        self.l2li[0] = min(l2)
        self.l1li[1] = max(l1)
        self.l2li[1] = max(l2)
        self.index = las[0].split(',')
        self.l1= []
        self.l2 = []
        self.km = [] 
        self.price = []
        self.lear = 0.5
        self.tmp0 = 0.0
        self.tmp1 = 0.0
        self.teta0 = 0.0
        self.teta1 = 0.0
        self.error = []

    def  estimateprice(teta0, teta1, milleage):
        return (teta0 +  (teta1* milleage))

    def estimatetmpteta0(teta0,teta1, km, price,lear):
        tmp = 0
        for index in range(len(km)):
            tmp += estimateprice(teta0, teta1, km[index]) - price[index]
        return (tmp * lear / len(self.km))

    def estimatetmpteta1(teta0,teta1, km, price,lear):
        tmp = 0
        for index in range(len(self.km)):
            tmp += (estimateprice(self.teta0, teta1, self.km[index]) - self.price[index]) * float(self.km[index])
    return (tmp * self.lear / len(self.km))

    def error_price(teta0, teta1, km, price,lear):
        tmp = 0
        for index in range(len(km)):
            tmp += (estimateprice(teta0, teta1, km[index]) - price[index]) ** 2
        return tmp / len(km)


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
        while (len(error) < 2 or  error[-2] - error[-1] != 0.0) and len(error) != 1000000:
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
line = linear_regression((data.read()).split())
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