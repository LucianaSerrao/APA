
#https://www.geeksforgeeks.org/union-find/
#https://www.geeksforgeeks.org/kruskals-minimum-spanning-tree-algorithm-greedy-algo-2/
#https://www.python-course.eu/graphs_python.php

import numpy as np
import itertools
from sort import heap_sort, counting_sort

class GraphXY: 
  
    def __init__(self): 
        self.graph = {} 
    
    def get_vertices(self):
        return list(self.graph.keys())
    
    def get_edges(self):
        return self.edges
    
    def add_vertex(self, vertex, x, y):
        if vertex not in self.graph:
            self.graph[vertex] = [x, y]
            
    def generate_edges(self):  #todas as combinações de vértices 2 a 2
        self.edges = [list(x) for x in itertools.combinations(self.graph, 2)]
    
    def add_weights(self):  #append no 3º índice de cada uma das combinações a distânica (adiciona os pesos das arestas)
        for edge in self.edges:
            edge.append(int(np.sqrt(np.power(self.graph[edge[0]][0] - self.graph[edge[1]][0], 2) + np.power(self.graph[edge[0]][1] - self.graph[edge[1]][1], 2))))

    def find(self, parent, i): 
        if parent[i] == i: 
            return i 
        return self.find(parent, parent[i]) 

    def union(self, parent, rank, x, y): 
        xroot = self.find(parent, x) 
        yroot = self.find(parent, y) 
  
        # Anexa árvore de classificação menor sob 
        # a raiz da árvore de classificação maior (Union by Rank) 
        if rank[xroot] < rank[yroot]: 
            parent[xroot] = yroot 
        elif rank[xroot] > rank[yroot]: 
            parent[yroot] = xroot 
  
        # Se as classificações são iguais, então define uma como raiz  
        # e incrementa 1 
        else : 
            parent[yroot] = xroot 
            rank[xroot] += 1
  
    def kruskal(self, sort_method='heap'): 
        result =[] #guarda o MST resultante 
  
        i = 0 # variável de índice, usada para arestas 
        e = 0 # variável de índice, usada para result[] 

        if sort_method == 'heap': 
            self.edges = heap_sort(self.edges)
        elif sort_method == 'counting':
            self.edges = counting_sort(self.edges)
        else:
            self.edges = sorted(self.edges, key=lambda item: item[2])
        
        parent = []
        rank = [] 
        # Cria subconjuntos V com elementos únicos
        for node in range(len(self.graph)): 
            parent.append(node) 
            rank.append(0) 
        # Número de arestas para serem tomadas é igual a V-1 
        while e < len(self.graph) -1 : 
  
            # Step 2: Seleciona a menor aresta e incrementa  
                    # o índice para próxima iteração 
            u,v,w =  self.edges[i] 
            i = i + 1
            x = self.find(parent, u) 
            y = self.find(parent ,v) 
            # Se, ao incluir essa aresta, não formar um ciclo,  
                        # inclui ela em resultado e incrementa o índice
                        # do resultado para a próxima aresta 
            if x != y: 
                e = e + 1     
                result.append([u,v,w]) 
                self.union(parent, rank, x, y)             
            # Discarta a aresta
  
        # Printa os conteúdos de result[] pra mostrar o built MST 
        print("Edges of MST: \n") 
        for u, v , weight in result: 
            #print (str(u) + " -- " + str(v) + " == " + str(weight)) 
            print ("%d -- %d == %d" % (u,v,weight)) 
        print("\nSum of edges: ", sum(row[2] for row in result))
