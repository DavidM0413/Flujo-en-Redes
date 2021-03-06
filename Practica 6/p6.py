from random import random, choice, normalvariate
from math import cos, sin, pi
import math
from time import time
from copy import deepcopy
def medio(p1, p2):
    return(((p1[0] + p2[0])/2), ((p1[1] + p2[1])/2))

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
def Manhattan (p1, p2):
    p = (abs(p1[0] - p2[0]), abs(p1[1] - p2[1]))
    x = p[0] + p[1]
    return(x)
        
class grafo:
    def __init__(self):
        self.n = 0 
        self.x = []
        self.y = []
        self.nodos = []
        self.coord = dict()
        self.vecinos = dict()
        self.s = 0
        self.t = 0
        self.A = []
        self.P = []
        self.L = 0
        self.aux = []

    def crear(self, k):
        self.n = k*k
        t = 0
        for i in range(k):
            for j in range(k):
                self.nodos.insert(t, ((1/(k-1))*j, (1/(k-1))*i))
                self.coord[t] = (j,i)
                self.x.insert(t, self.nodos[t][0])
                self.y.insert(t, self.nodos[t][1])
                self.vecinos[t] = set()
                t+=1
        self.s = 0
        self.t = (k*k) - 1
        self.nodo_s = (self.x[0], self.y[0])
        self.nodo_t = (self.x[(k*k) - 1], self.y[(k*k) - 1])
        
        
    def delnodo(self):
        n = len(self.x)
        k = math.floor(random()*n)
        if self.x[k] is not self.x[0] and self.y[k] is not self.y[(n-1)] and self.y[k] is not self.y[0] and self.x[k] is not self.x[(n-1)]:
            nodo = [self.x[k], self.y[k]]
            del self.x[k]
            del self.y[k]
            agh = []
            for i in range(0,len(self.A)):
                if (nodo[0] is self.A[i][0] and nodo[1] is self.A[i][1]) or (nodo[0] is self.A[i][2] and nodo[1] is self.A[i][3]):
                    agh.append(i)
            agh.sort(reverse = True)    
            for j in agh:
                del self.A[j]
                del self.P[j]
                    
    def fusion(self):
        while(len(self.x >2)):
            r = math.ceil(random()*len(self.A))
            if (self.A[r] is not (self.nodo_s[0], self.nodo_s[1], self.nodo_t[0], self.nodo_t[1]) or self.A[r] is not (self.nodo_t[0], self.nodo_t[1], self.nodo_s[0], self.nodo_s[1])):
                
                a1 = (self.A[r][0], self.A[r][1])
                a2 = (self.A[r][2], self.A[r][3])
                i1 = self.nodos.index(a1)
                i2 = self.nodos.index(a2)
                print(self.A[r])
                del self.A[r]
                del self.P[r]
                if i1 < i2:
                    del self.x[i2]
                    del self.y[i2]
                    del self.x[i1]
                    del self.y[i1]
                else:
                    del self.x[i1]
                    del self.y[i1]
                    del self.x[i2]
                    del self.y[i2]
                self.nodos.append(medio(a1, a2))
                aux = medio(a1, a2)
                if a1 is self.nodo_s:
                    self.nodo_s = aux
                if a1 is self.nodo_t:
                    self.nodo_t = aux
                if a2 is self.nodo_s:
                    self.nodo_s = aux
                if a2 is self.nodo_t:
                    self.nodo_t = aux
                self.x.append(medio(a1, a2)[0])
                self.y.append(medio(a1, a2)[1])
                for i in range(len(self.A)):
                    if self.A[i][0] is a1[0] and self.A[i][1] is a1[1]:
                        self.A[i] = (aux[0], aux[1], self.A[i][2], self.A[i][3])
                         
                    if self.A[i][2] is a1[0] and self.A[i][3] is a1[1]:
                        self.A[i] = (self.A[i][0], self.A[i][1], aux[0], aux[1])
                     
                    if self.A[i][0] is a2[0] and self.A[i][1] is a2[1]:
                        self.A[i] = (aux[0], aux[1], self.A[i][2], self.A[i][3])
                     
                    if self.A[i][2] is a2[0] and self.A[i][3] is a2[1]:
                        self.A[i] = (self.A[i][0], self.A[i][1], aux[0], aux[1])
                
            
         
       
      
    
    def camino(self, s, t, f): # construcción de un camino aumentante
        cola = [s]
        usados = set()
        camino = dict()
        while len(cola) > 0:
            u = cola.pop(0)
            usados.add(u)
            
            for i in range(len(self.A)):
                #w = index_v((self.A[i][0], self.A[i][1]), self.nodos)
                w = self.nodos.index((self.A[i][0], self.A[i][1]))
                v = self.nodos.index((self.A[i][2], self.A[i][3]))
                #v = index_v((self.A[i][2], self.A[i][3]), self.nodos)
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
 
    def ford_fulkerson(self): # algoritmo de Ford y Fulkerson
        maximo = 0
        f = dict()
        while True:
            aum = self.camino(self.s, self.t, f)
            #print(aum)
            if aum is None:
                break # ya no hay
            incr = min(aum.values(), key = (lambda k: k[1]))[1]
            u = self.t
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
            
                

    def conexiones(self, l, p):
        self.L = l
        k = self.n**(1/2)
        for i in range(self.n):
            for j in range(self.n):
                if Manhattan(self.coord[i], self.coord[j]) <= l:  
                    self.A.append((self.x[i], self.y[i], self.x[j], self.y[j]))
                    self.vecinos[i].add(j)
                    self.vecinos[j].add(i)
                    self.P.append(math.ceil(abs(normalvariate(5, (5**.5)))))
                    
        
        count = 0
        for i in range(self.n):
            for j in range(self.n):
                 if random() < p:
                     if (self.x[i], self.y[i], self.x[j], self.y[j]) not in self.A:
                        self.A.append((self.x[i], self.y[i], self.x[j], self.y[j]))
                        self.P.append(math.ceil(abs(normalvariate(5, (5**.5)))))
                        count+=1
        
        
        
        
    
    def delarista(self):
        b = 15
        for i in range(b):
            n = len(self.A)
            k = math.floor(random()*n)
            if k < len(self.A):
                del self.A[k]
                del self.P[k]

    
        
        
    def gnuplot(self):
        with open("nodos.dat", "w") as salida:
            for v in range(len(self.x)):
                x = self.x[v]
                y = self.y[v]
                
                print(x, y, file=salida)
        
        with open("tarea5.plot", "w") as archivo:
             print("set term pdf", file = archivo)
             print("set key off", file = archivo)
             print("set output 'test5.pdf'", file = archivo)
             print("set xrange [-0.1:1.1]", file = archivo)
             print("set yrange [-0.1:1.1]", file = archivo)
             print("set size square", file = archivo)
             print("set xtics format ''", file = archivo)
             print("set ytics format ''", file = archivo)
             num = 1
             for i in range(len(self.A)):
                 (x1, y1, x2, y2) = self.A[i]
                 print("set arrow {:d} from {:f}, {:f} to {:f}, {:f} lw 1 nohead filled size 0.1,9".format(num, x1, y1, x2, y2), file = archivo)
                 num += 1
                 
             print("show arrow", file = archivo)
             print("plot 'nodos.dat' using 1:2 with points pt 7", file = archivo)
             print("quit()", file = archivo)

    
                    
k = 3
g1 = grafo()
g1.crear(k)
g1.conexiones(1, 0)
g1.fusion()
g1.gnuplot()
