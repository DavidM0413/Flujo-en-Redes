from random import random, choice
from math import cos, sin, pi
import math
from time import time
def index(p,L):
    for i in range(len(L)):
        if p is L[i]:
            return(i)

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
        self.x = []
        self.y = []
        self.nodos = []
        self.vecinos = dict()
        
        self.A = []
        self.P = []
        
        self.aux = []

    def crear(self, n):
        angulo = (2*pi)/n
        self.n = n
        for nodo in range(self.n):
            
            self.nodos.insert(nodo, ((0.5 + (0.35*cos(angulo*nodo))) ,(0.5 + (0.35*sin(angulo*nodo)))))
            self.x.insert(nodo, self.nodos[nodo][0])
            self.y.insert(nodo, self.nodos[nodo][1])
            self.vecinos[nodo] = set()
        
        

    
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
                   
                    dif = self.P[index_A(u, v, self.A, self.nodos)] - actual # de aqui obtengo el indice
                    
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
            #print(aum)
            if aum is None:
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

    def avgdist(self):
        distancia = self.floyd_warshall()
        suma = 0
        for (k,val) in distancia.items():
            suma = suma + val
        prom = suma/len(distancia)
        return(prom)

    def cluscoef(self):
        clust = 0
        for v in range(len(self.nodos)):
            m = 0
            for u in self.vecinos[v]:
                for w in self.vecinos[v]:
                    if u in self.vecinos[w]:
                        m+= 1
            n = len(self.vecinos[v])
            if n > 1:
                clust += m/(n*(n-1))
        return(clust/len(self.nodos))
            
                

    def conexiones(self, k, prob):
        t = 0
        for r in range(k):
            for i in range(self.n):
                if i < (self.n - (r+1)):
                    self.A.insert(t,(self.x[i], self.y[i], self.x[i+(r+1)], self.y[i+(r+1)]))
                    self.P.insert(t, (r+1))
                    self.vecinos[i].add(i+(r+1))
                    self.vecinos[i+(r+1)].add(i)
                    t+=1
                else:
                    self.A.insert(t, (self.x[i], self.y[i], self.x[(i + (r+1)) - self.n], self.y[(i + (r+1)) - self.n]))
                    self.P.insert(t, (r+1))
                    self.vecinos[i].add((i + (r+1)) - self.n)
                    self.vecinos[(i + (r+1)) - self.n].add(i)
                    t+1
        for i in range(self.n):
            for j in range(self.n):
                if i is not j:
                    if random() < prob:
                        if (self.x[i], self.y[i], self.x[j], self.y[j]) not in self.A:
                            self.A.insert(t, (self.x[i], self.y[i], self.x[j], self.y[j]))
                            self.vecinos[i].add(j)
                            self.vecinos[j].add(i)
                    
                            if abs(i-j) <= self.n/2:
                                self.P.insert(t, abs(i-j))
                            else:
                                self.P.insert(t, self.n - abs(i-j))
                            t+=1
        
        
        
            
                    

    def gnuplot(self):
        with open("nodos.dat", "w") as salida:
            for v in range(self.n):
                x = self.nodos[v][0]
                y = self.nodos[v][1]
                
                print(x, y, file=salida)
        
        with open("tarea4.plot", "w") as archivo:
             print("set term pdf", file = archivo)
             print("set key off", file = archivo)
             print("set output 'test.pdf'", file = archivo)
             print("set xrange [-0.1:1.1]", file = archivo)
             print("set yrange [-0.1:1.1]", file = archivo)
             print("set size square", file = archivo)
             num = 1
             for i in range(len(self.A)):
                 (x1, y1, x2, y2) = self.A[i]
                 print("set arrow {:d} from {:f}, {:f} to {:f}, {:f} lw 1 nohead filled size 0.1,9".format(num, x1, y1, x2, y2), file = archivo)
                 num += 1
                 
             print("show arrow", file = archivo)
             print("plot 'nodos.dat' using 1:2 with points pt 7", file = archivo)
             print("quit()", file = archivo)
            


                    
n = 15


#for i in range(10):
prob = 2**(-4)
    #prob = 2**(-(10-i+1))
g1 = grafo()
g1.crear(n)
g1.conexiones(3, prob)
g1.gnuplot()
print(g1.avgdist())

