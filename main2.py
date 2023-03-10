import array as arr

def  estimateprice(milleage, teta0, teta1, index):
    print("estimate " + index + " : ",(teta0 +  (teta1 * float(milleage))))

fichier = open("ft_linear_regression.csv", "r")
tmp = (fichier.read()).split()
index = tmp[0].split(",")
valeur = tmp[1].split(",")
estimateprice(input("numbers of "+ index[0]+" : ") , float(valeur[0]),float(valeur[1]), index[1])
