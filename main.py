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

    def  estimate_abscisse(self, x):
        return (self.teta0 + (self.teta1 * x))
            
    def  estimate_abscisse_absolue(self, x):
        return (self.teta0_asbolue + (self.teta1_asbolue * x))

    def estimate_tmpteta0(self):
        tmp = 0
        for index in range(len(self.ordonnee)):
            tmp += self.estimate_abscisse(self.ordonnee[index]) - self.abscisse[index]
        return (tmp * self.lear / len(self.ordonnee))

    def estimate_tmpteta1(self):
        tmp = 0
        for index in range(len(self.ordonnee)):
            tmp += (self.estimate_abscisse(self.ordonnee[index]) - self.abscisse[index]) * float(self.ordonnee[index])
        return (tmp * self.lear / len(self.ordonnee))

    def error_abscisse(self):
        tmp = 0
        for index in range(len(self.ordonnee)):
            tmp += (self.estimate_abscisse(self.ordonnee[index]) - self.abscisse[index]) ** 2
        return tmp / len(self.ordonnee)

    def init_valeur_relative(self):
        for index in range(len(self.ordonnee_relative)):
            self.ordonnee.append((self.ordonnee_relative[index] - self.ordonnee_relative_limite[0])/ (self.ordonnee_relative_limite[1] - self.ordonnee_relative_limite[0]))
            self.abscisse.append((self.abscisse_relative[index] - self.abscisse_relative_limite[0])/ (self.abscisse_relative_limite[1] - self.abscisse_relative_limite[0]))

    def show_relative(self):
        plt.figure("ft_linear_regression")
        plt.scatter(self.ordonnee, self.abscisse)
        plt.plot([min(self.ordonnee), max(self.ordonnee)],[self.estimate_abscisse(min(self.ordonnee)), self.estimate_abscisse(max(self.ordonnee))], color = 'green', linestyle = 'solid')
        plt.ylabel(self.index[0])
        plt.xlabel(self.index[1])
        plt.title("relative")
        plt.show()


    def show_absolue(self):
        plt.figure("ft_linear_regression")
        plt.scatter(self.ordonnee_relative, self.abscisse_relative)
        plt.plot([0,  self.ordonnee_relative_limite[1]],[self.estimate_abscisse_absolue(0), \
                            self.estimate_abscisse_absolue(self.ordonnee_relative_limite[1])], \
                            color = 'green', linestyle = 'solid')
        plt.ylabel(self.index[0])
        plt.xlabel(self.index[1])
        plt.title("absolue")
        plt.show()

    def show_error(self):
        plt.figure("ft_linear_regression")
        plt.plot(self.error)
        plt.title("error")
        plt.show()

    def estimate_teta(self):
        tmp0 = 0
        tmp1 = 0
        while (len(self.error) < 2 or  self.error[-2] - self.error[-1] != 0.0) and len(self.error) != 1000000:
            tmp0 -= self.estimate_tmpteta0()
            tmp1 -= self.estimate_tmpteta1()
            self.error.append(self.error_abscisse())
            self.teta0 = tmp0
            self.teta1 = tmp1
        self.teta1_asbolue = self.teta1 / ((self.ordonnee_relative_limite[1] - self.ordonnee_relative_limite[0]) / (self.abscisse_relative_limite[1] - self.abscisse_relative_limite[0]))
        self.teta0_asbolue = (self.teta0 * (self.abscisse_relative_limite[1] - self.abscisse_relative_limite[0])) + self.abscisse_relative_limite[0] - self.teta1_asbolue * self.ordonnee_relative_limite[0]
        self.error.append(self.error_abscisse())
    
data = open("data.csv", "r")
line = linear_regression((data.read()).split())
data.close()
line.init_valeur_relative()
line.estimate_teta()
line.show_relative()
line.show_absolue()
line.show_error()
fin = open("ft_linear_regression.csv","w")
fin.write(line.index[0]+","+line.index[1]+"\n")
valeur = "%f,%f\n" % (line.teta0_asbolue,line.teta1_asbolue)
fin.write(valeur)
fin.close()