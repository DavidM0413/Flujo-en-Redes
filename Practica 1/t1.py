from random import random
import math
n = 30
p = 0.2
d = ((2)**(1/2))/2
nodos=[]
aristas=[]
def distancia(p1, p2):
    return(((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**(1/2))
def absoluto(x):
    return((x**2)**(1/2))
#with open("nodos.dat", "w") as salida:
for v in range(n):
    x= random()
    y= random()
    r= 2 + random()
    nodos.append((x,y,r))

        #print(x,y,r,c, file=salida)

for i in range(len(nodos)):
    count = 0
    for j in range(len(nodos)):
        if absoluto((nodos[i][2] - nodos[j][2]))/(0.0001+distancia((nodos[i][0],nodos[i][1]), (nodos[j][0],nodos[j][1])))**2 < p:
            if distancia((nodos[i][0],nodos[i][1]), (nodos[j][0],nodos[j][1])) < d:
                aristas.append((nodos[i][0],nodos[i][1], nodos[j][0],nodos[j][1], (1 - distancia((nodos[i][0],nodos[i][1]), (nodos[j][0],nodos[j][1])))))
                count = count +1
            else:
                aristas.append((nodos[i][0],nodos[i][1], nodos[j][0],nodos[j][1], (1 + distancia((nodos[i][0],nodos[i][1]), (nodos[j][0],nodos[j][1])))))
                count = count +1
    nodos[i] = ((nodos[i][0], nodos[i][1], nodos[i][2], count))
   
with open("nodos.dat", "w") as salida:
    for v in range(len(nodos)):
        x= nodos[v][0]
        y= nodos[v][1]
        r= nodos[v][2]
        c= nodos[v][3]
        print(x,y,r,c, file=salida)

with open("tarea1.plot", "w") as archivo:
     print("set term png", file = archivo)
     print("set key off", file = archivo)
     #print("unset colorbox", file = archivo)
     print("set output 'grafo1.png'", file = archivo)
     print("set xrange [-0.1:1.1]", file = archivo)
     print("set yrange [-0.1:1.1]", file = archivo)
     print("set size square", file = archivo)
     num = 1
     for a in aristas:
         (x1, y1, x2, y2, t) = a
         print("set arrow {:d} from {:f}, {:f} to {:f}, {:f} nohead lw {:f}".format(num, x1, y1, x2, y2, t), file = archivo)
         num += 1
     print("show arrow", file = archivo)
     print("plot 'nodos.dat' using 1:2:3:4 with points pt 7 ps var lc palette frag var", file = archivo)
     print("quit()", file = archivo)
