import array as arr
import matplotlib.pyplot as plt


class linear_regression:
    ordonnee_relative = []
    abscisse_relative = []
    ordonnee = [] 
    abscisse = []
    lear = 0.5
    teta0 = 0.0
    teta1 = 0.0
    error = []
    ordonnee_relative_limite = [0,0]
    abscisse_relative_limite = [0,0]
    def __init__(self, data):
        for index in range(len(data)-1):
            v = data[index+1].split(',')
            self.ordonnee_relative.append(int(v[0]))
            self.abscisse_relative.append(int(v[1]))
        self.ordonnee_relative_limite[0] = min(self.ordonnee_relative)
        self.abscisse_relative_limite[0] = min(self.abscisse_relative)
        self.ordonnee_relative_limite[1] = max(self.ordonnee_relative)
        self.abscisse_relative_limite[1] = max(self.abscisse_relative)
        self.index = data[0].split(',')
        self.ordonnee = [] 
        self.abscisse = []
        self.lear = 0.5
        self.tmp0 = 0.0
        self.tmp1 = 0.0
        self.teta0 = 0.0
        self.teta1 = 0.0
        self.error = []

    def  estimateabscisse(self, milleage):
        return (self.teta0 +  (self.teta1* milleage))
            
    def  estimateabscisse_absolue(self, milleage):
        return (self.nteta0 +  (self.nteta1* milleage))

    def estimatetmpteta0(self):
        tmp = 0
        for index in range(len(self.ordonnee)):
            tmp += self.estimateabscisse(self.ordonnee[index]) - self.abscisse[index]
        return (tmp * self.lear / len(self.ordonnee))

    def estimatetmpteta1(self):
        tmp = 0
        for index in range(len(self.ordonnee)):
            tmp += (self.estimateabscisse(self.ordonnee[index]) - self.abscisse[index]) * float(self.ordonnee[index])
        return (tmp * self.lear / len(self.ordonnee))

    def error_abscisse(self):
        tmp = 0
        for index in range(len(self.ordonnee)):
            tmp += (self.estimateabscisse(self.ordonnee[index]) - self.abscisse[index]) ** 2
        return tmp / len(self.ordonnee)

    def init_valeur_relative(self):
        for index in range(len(self.ordonnee_relative)):
            self.ordonnee.append((self.ordonnee_relative[index] - self.ordonnee_relative_limite[0])/ (self.ordonnee_relative_limite[1] - self.ordonnee_relative_limite[0]))
            self.abscisse.append((self.abscisse_relative[index] - self.abscisse_relative_limite[0])/ (self.abscisse_relative_limite[1] - self.abscisse_relative_limite[0]))
            print(self.ordonnee[-1], self.abscisse[-1])

    def show_relative(self):
        plt.scatter(self.ordonnee, self.abscisse)
        plt.plot([min(self.ordonnee), max(self.ordonnee)],[self.estimateabscisse(min(self.ordonnee)), self.estimateabscisse(max(self.ordonnee))], color = 'green', linestyle = 'solid')
        plt.ylabel(self.index[0])
        plt.xlabel(self.index[1])
        plt.show()


    def show_absolue(self):
        plt.scatter(self.ordonnee_relative, self.abscisse_relative)
        plt.plot([0,  self.ordonnee_relative_limite[1]],[self.estimateabscisse_absolue(0), \
                            self.estimateabscisse_absolue(self.ordonnee_relative_limite[1])], \
                            color = 'green', linestyle = 'solid')
        plt.ylabel(self.index[0])
        plt.xlabel(self.index[1])
        plt.show()

    def show_error(self):
        plt.plot(self.error)
        plt.show()

    def estimate_teta(self):
        tmp0 = 0
        tmp1 = 0
        while (len(self.error) < 2 or  self.error[-2] - self.error[-1] != 0.0) and len(self.error) != 1000000:
            tmp0 -= self.estimatetmpteta0()
            tmp1 -= self.estimatetmpteta1()
            self.error.append(self.error_abscisse())
            self.teta0 = tmp0
            self.teta1 = tmp1
        self.nteta1 = self.teta1 / ((self.ordonnee_relative_limite[1]- self.ordonnee_relative_limite[0])/ (self.abscisse_relative_limite[1] - self.abscisse_relative_limite[0]))
        self.nteta0 = (self.teta0 * (self.abscisse_relative_limite[1] - self.abscisse_relative_limite[0])) + self.abscisse_relative_limite[0] - self.nteta1 * self.ordonnee_relative_limite[0]
        self.error.append(self.error_abscisse())
    
data = open("data.csv", "r")
line = linear_regression((data.read()).split())
data.close()
line.init_valeur_relative()
line.estimate_teta()
line.show_relative()
line.show_absolue()
line.show_error()
fin = open("teta.csv","w")
fin.write(line.index[0]+","+line.index[1]+"\n")
valeur = "%f,%f\n" % (line.nteta0,line.nteta1)
fin.write(valeur)
fin.close()