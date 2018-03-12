from random import random, choice
import math
def distancia(p1, p2):
    return(((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**(1/2))
def medio(p1, p2):
    return(((p1[0] + p2[0])/2), ((p1[1] + p2[1])/2))
def index_A(p, q, A, N):
    for i in range(len(A)):
        if N[p][0] is A[i][0] and N[p][1] is A[i][1] and N[q][0] is A[i][2] and N[q][1] is A[i][3]:
            return(i)
    return(1.1)
def index_v(p, N):
    for i in range(len(N)):
        if p[0] is N[i][0] and p[1] is N[i][1]:
            return(i)
        
class grafo:
    def __init__(self):
        self.n = 0 
        self.x = dict() 
        self.y = dict()
        self.nodos = []
        self.vecinos = dict()
        self.r = dict()
        self.c = dict()
        self.A = []
        self.P = []
        self.D = []
        self.aux = []

    def crear(self, n):
        self.n = n
        for nodo in range(self.n):
            self.x[nodo] = random()
            self.y[nodo] = random()
            self.nodos.insert(nodo, (self.x[nodo], self.y[nodo]))
            self.r[nodo] = random() + 2
            self.c[nodo] = 0
        print(self.nodos[9])
        print(self.nodos[12])

    def camino(self, s, t, f): # construcción de un camino aumentante
        cola = [s]
        usados = set()
        camino = dict()
        while len(cola) > 0:
            u = cola.pop(0)
            usados.add(u)
            
        for i in range(len(self.A)):
            w = index_v((self.A[i][0], self.A[i][1]), self.nodos)
            v = index_v((self.A[i][2], self.A[i][3]), self.nodos)
            if w == u and v not in cola and v not in usados:
                actual = f.get((u, v), 0)
                dif = self.P[index_A(u, v, self.A, self.nodos)] - actual
                if dif > 0:
                    cola.append(v)
                    camino[v] = (u, dif)
        if t in usados:
            return camino
        else: # no se alcanzó
            return None
 
    def ford_fulkerson(self, s, t): # algoritmo de Ford y Fulkerson
        if s == t:
            return 0
        maximo = 0
        f = dict()
        while True:
            aum = self.camino(s, t, f)
            if aum is None:
                print("no jalo")
                break # ya no hay
            incr = min(aum.values(), key = (lambda k: k[1]))[1]
            u = t
            while u in aum:
                v = aum[u][0]
                actual = f.get((v, u), 0) # cero si no hay
                inverso = f.get((u, v), 0)
                f[(v, u)] = actual + incr
                f[(u, v)] = inverso - incr
                u = v
            maximo += incr
        return maximo
    
    def floyd_warshall(self): 
        d = {}
        for v in range(self.n):
            d[(v, v)] = 0 # distancia reflexiva es cero
            for u in range(self.n): # para vecinos, la distancia es el peso
                for r in range(len(self.A)):
                    if self.x[v] is self.A[r][0] and self.y[v] is self.A[r][1] and self.x[u] is self.A[r][2] and self.y[u] is  self.A[r][3]:
                        d[(v, u)] = self.P[r]

               
        for intermedio in range(self.n):
            for desde in range(self.n):
                for hasta in range(self.n):
                    di = None
                    if (desde, intermedio) in d:
                        di = d[(desde, intermedio)]
                    ih = None
                    if (intermedio, hasta) in d:
                        ih = d[(intermedio, hasta)]
                    if di is not None and ih is not None:
                        c = di + ih # largo del camino via "i"
                        if (desde, hasta) not in d or c < d[(desde, hasta)]:
                            d[(desde, hasta)] = c # mejora al camino actual
        return d

    def conexiones(self, prob, p = 0, d = 0):
        t = 0
        k = 0
        for i in range(self.n):
            
            for j in range(self.n):
                if i is not j:
                    
                    if abs(self.r[i] - self.r[j])/ (distancia((self.x[i], self.y[i]), (self.x[j], self.y[j])))**2 < prob:
                        test = 0
                        if len(self.A) is not 0 or k is 0:
                            for r in range(len(self.A)):
                                if (self.x[i] is self.A[r][2] and self.y[i] is self.A[r][3] and self.x[j] is self.A[r][0] and self.y[j] is self.A[r][1]):
                                    test = test +1
                            if test is 0:
                                k = 3
                                self.c[i] = self.c[i] +1
                                self.c[j] = self.c[j] +1
                                #count = count +1
                               
                                self.A.insert(t,(self.x[i], self.y[i], self.x[j], self.y[j]))
                                #self.vecinos[(self.x[i], self.y[i])].add((self.x[j], self.y[j])
                                t = t +1
                                if p:
                                    self.P.insert(t, math.ceil(random()*10))
                                    self.aux.insert(t, medio((self.x[i], self.y[i]), (self.x[j], self.y[j]))) #quiero esto, pero no sirve :(
                                if d:
                                    self.D.insert(t,choice([0,1]))
            #self.c[i]= count

    def gnuplot(self):
        with open("nodos.dat", "w") as salida:
            for v in range(self.n):
                x = self.x[v]
                y = self.y[v]
                r = self.r[v]
                c = self.c[v]
                print(x, y, r, c, file=salida)
        if len(self.D) is not 0 and len(self.P) is 0:
            with open("tarea2_dirigido.plot", "w") as archivo:
                print("set term pdf", file = archivo)
                print("set key off", file = archivo)
                print("set output 'grafo_dirigido.pdf'", file = archivo)
                print("set xrange [-0.1:1.1]", file = archivo)
                print("set yrange [-0.1:1.1]", file = archivo)
                print("set size square", file = archivo)
                num = 1
                for i in range(len(self.A)):
                    (x1, y1, x2, y2) = self.A[i]
                    if self.D[i] is 0:
                        print("set arrow {:d} from {:f}, {:f} to {:f}, {:f} lw 1 backhead filled size 0.1,9".format(num, x1, y1, x2, y2), file = archivo)
                        num += 1
                    else:
                        print("set arrow {:d} from {:f}, {:f} to {:f}, {:f} lw 1 head filled size 0.1,9 ".format(num, x1, y1, x2, y2), file = archivo)
                        num += 1
                print("show arrow", file = archivo)
                print("plot 'nodos.dat' using 1:2:3:4 with points pt 7 ps var lc palette frag var", file = archivo)
                print("quit()", file = archivo)
            
                            
        if len(self.P) is not 0 and len(self.D) is 0:
            with open("tarea2_ponderado.plot", "w") as archivo:
                print("set term pdf", file = archivo)
                print("set key off", file = archivo)
                print("set output 'grafo_ponderado.pdf'", file = archivo)
                print("set xrange [-0.1:1.1]", file = archivo)
                print("set yrange [-0.1:1.1]", file = archivo)
                print("set size square", file = archivo)
                num = 1
                for i in range(len(self.A)):
                    (x1, y1, x2, y2) = self.A[i]
                    w = self.P[i]
                    wi = w*0.3
                    (xw, yw) = self.aux[i]
                    print("set arrow {:d} from {:f}, {:f} to {:f}, {:f} lw {:f} nohead ".format(num, x1, y1, x2, y2, wi), file = archivo)
                    print("set label '{:d}' at {:f},{:f}".format(w, xw, yw), file = archivo)
                    num += 1
                print("show arrow", file = archivo)
                print("plot 'nodos.dat' using 1:2:3:4 with points pt 7 ps var lc palette frag var", file = archivo)
                print("quit()", file = archivo)
        if len(self.D) is 0 and len(self.P) is 0:
            with open("tarea2_simple.plot", "w") as archivo:
                print("set term pdf", file = archivo)
                print("set key off", file = archivo)
                print("set output 'grafo_simple.pdf'", file = archivo)
                print("set xrange [-0.1:1.1]", file = archivo)
                print("set yrange [-0.1:1.1]", file = archivo)
                print("set size square", file = archivo)
                num = 1
                for i in range(len(self.A)):
                    (x1, y1, x2, y2) = self.A[i]
                    print("set arrow {:d} from {:f}, {:f} to {:f}, {:f} lw 1 nohead ".format(num, x1, y1, x2, y2), file = archivo)
                    num += 1
                print("show arrow", file = archivo)
                print("plot 'nodos.dat' using 1:2:3:4 with points pt 7 ps var lc palette frag var", file = archivo)
                print("quit()", file = archivo)
        if len(self.D) is not 0 and len(self.P) is not 0:
            with open("tarea2_mixto.plot", "w") as archivo:
                print("set term pdf", file = archivo)
                print("set key off", file = archivo)
                print("set output 'grafo_mixto.pdf'", file = archivo)
                print("set xrange [-0.1:1.1]", file = archivo)
                print("set yrange [-0.1:1.1]", file = archivo)
                print("set size square", file = archivo)
                num = 1
                for i in range(len(self.A)):
                    (x1, y1, x2, y2) = self.A[i]
                    w = self.P[i]
                    wi = w*0.3
                    (xw, yw) = self.aux[i]
                    if self.D[i] is 0:
                        print("set arrow {:d} from {:f}, {:f} to {:f}, {:f} lw {:f} backhead filled size 0.1,9".format(num, x1, y1, x2, y2, wi), file = archivo)
                        print("set label '{:d}' at {:f},{:f}".format(w, xw, yw), file = archivo)
                        num += 1
                    else:
                        print("set arrow {:d} from {:f}, {:f} to {:f}, {:f} lw {:f} head filled size 0.1,9 ".format(num, x1, y1, x2, y2, wi), file = archivo)
                        print("set label '{:d}' at {:f},{:f}".format(w, xw, yw), file = archivo)
                        num += 1
                print("show arrow", file = archivo)
                print("plot 'nodos.dat' using 1:2:3:4 with points pt 7 ps var lc palette frag var", file = archivo)
                print("quit()", file = archivo)


                    
n = 15
prob = 0.2
d = ((2)**(1/2))/2
g1 = grafo()
g1.crear(n)
g1.conexiones(prob, p= 1)
g1.gnuplot()
print(g1.floyd_warshall())
print(g1.ford_fulkerson(9,12))
