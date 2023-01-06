import array as arr
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def  estimateprice(milleage, teta0, teta1):
    #print(teta0 +  (teta1* float(milleage)))
    print("estimate price : ",(teta0 +  (teta1 * float(milleage))))

fichier = open("teta.csv", "r")
valeur = (fichier.read()).split()[1].split(",")
estimateprice(input("enter valeur estimate:") , float(valeur[0]),float(valeur[1]))
