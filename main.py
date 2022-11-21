import array as arr

data = open("data.csv", "r")
la = (data.read()).split()
data.close()
km  = []
price  = []
lear = 0.01
somme0 = 0
somme1 = 0
teta0 = 0.0
tata1 = 0.0
for index in range(len(la)-1):
        v = la[index+1].split(',')
        km.append(int(v[0]))
        price.append(int(v[1]))
for b in range(10000):
    for index in range(len(la)-1):
        v = la[index+1].split(',')
        somme0 += teta0 + (tata1 * int(v[0])) - int(v[1])
       # somme1 += (teta0 + (tata1 * int(v[0])) - int(v[1])) * int(v[0])
    teta0 -= somme0 * lear / (len(km))
    #tata1 -= somme1 * lear / (len(km))
    #print(teta0)
    print(somme0)
    somme0 = 0
    somme1 = 0
print(teta0)
for b in range(10000):
    for index in range(len(la)-1):
        v = la[index+1].split(',')
       # somme0 += teta0 + (tata1 * int(v[0])) - int(v[1])
        somme1 += (teta0 + (tata1 * int(v[0])) - int(v[1])) * int(v[0])
    tata1 -= somme1 * lear / (len(km))
    print(somme1)
    break
print(tata1)