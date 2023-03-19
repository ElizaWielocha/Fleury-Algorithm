import matplotlib.pyplot as plt
import networkx as nx

from math import pi
import matplotlib.pyplot as plt
import numpy as np
import time

from collections import defaultdict

# tworzenie plotna
plt.ion()
fig = plt.figure()
plot = fig.add_subplot()



# GRAFICZNIE FLEURY ---------------------------------------------------------------------------------
# rozparywana krawedz grafu jest zielona
def graphic_consideredEdge(G, u, v, pos, colorr):
    plt.clf()
    G.remove_edge(u,v)
    G.add_edge(u, v, color=colorr)
    
    edges = G.edges()
    colors = [c for (u,v,c) in g_graphic.edges(data='color')]
    
    nx.draw(G, pos=pos, edge_color = colors, node_size=800, with_labels=True)
    fig.canvas.draw()
     
    # to flush the GUI events
    fig.canvas.flush_events()
    input()
    #time.sleep(2)
    
# usuwanie z grafu (plot) krawedzi
def graphic_removeEdge(G, u, v, pos):
    G.remove_edge(u,v)
 
    # re-drawing the figure
    plt.clf()
    nx.draw(G, pos=pos, node_size=800, with_labels=True)
    fig.canvas.draw()
     
    # to flush the GUI events
    fig.canvas.flush_events()
    input()
    #time.sleep(3)

# -------------------------------------------------------------------------------------------------
    
class Graph:
  
    def __init__(self,vertices):
        self.V= vertices #No. of vertices
        self.graph = defaultdict(list) # default dictionary to store graph
        self.Time = 0
  
    # function to add an edge to graph
    def addEdge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)
 
    # This function removes edge u-v from graph   
    def rmvEdge(self, u, v):
        for index, key in enumerate(self.graph[u]):
            if key == v:
                self.graph[u].pop(index)
                break
        for index, key in enumerate(self.graph[v]):
            if key == u:
                self.graph[v].pop(index)
                break
 
    # A DFS based function to count reachable vertices from v
    def DFSCount(self, v, visited):
        count = 1
        visited[v] = True
        for i in self.graph[v]:
            if visited[i] == False:
                count = count + self.DFSCount(i, visited)        
        return count
 
    # The function to check if edge u-v can be considered as next edge in
    # Euler Tour
    def isValidNextEdge(self, u, v, graphic_graph, pos):
        # The edge u-v is valid in one of the following two cases:
  
          #  1) If v is the only adjacent vertex of u
        if len(self.graph[u]) == 1:
            graphic_consideredEdge(graphic_graph, u, v, pos, 'green')
            return True
        else:
            '''
             2) If there are multiple adjacents, then u-v is not a bridge
                 Do following steps to check if u-v is a bridge
  
            2.a) count of vertices reachable from u'''   
            visited =[False]*(self.V)
            count1 = self.DFSCount(u, visited)
 
            '''2.b) Remove edge (u, v) and after removing the edge, count
                vertices reachable from u'''
            self.rmvEdge(u, v)
            visited =[False]*(self.V)
            count2 = self.DFSCount(u, visited)
 
            #2.c) Add the edge back to the graph
            self.addEdge(u,v)
 
            # 2.d) If count1 is greater, then edge (u, v) is a bridge
            if count1 > count2:
                graphic_consideredEdge(graphic_graph, u, v, pos, 'red')
                return False
            else:
                graphic_consideredEdge(graphic_graph, u, v, pos, 'green')
                return True
 
 
    # Print Euler tour starting from vertex u
    def printEulerUtil(self, u, graphic_graph, pos):
        #Recur for all the vertices adjacent to this vertex
        for v in self.graph[u]:
            #If edge u-v is not removed and it's a a valid next edge
            if self.isValidNextEdge(u, v, graphic_graph, pos):
                print("%d-%d " %(u,v)),
                graphic_removeEdge(graphic_graph, u, v, pos)
                self.rmvEdge(u, v)
                self.printEulerUtil(v, graphic_graph, pos)
 
 
     
    '''The main function that print Eulerian Trail. It first finds an odd
   degree vertex (if there is any) and then calls printEulerUtil()
   to print the path '''
    def printEulerTour(self, graphic_graph, pos):
        #Find a vertex with odd degree
        u = 0
        for i in range(self.V):
            if len(self.graph[i]) %2 != 0 :
                u = i
                break
        # Print tour starting from odd vertex
        print ("\n")
        self.printEulerUtil(u, graphic_graph, pos)
        
# ----------------------------------------------------------------------------------------------

# przyklad z wczytywaniem z pliku tekstowego
with open('graf2.txt') as f:
    lines = f.readlines()

nVertices = int(lines[0])
g1 = Graph(nVertices)
# multigraf, bo może miec krawedzie wielokrotne/petle
g_graphic = nx.MultiGraph()

for i in range(1, len(lines)):
    line = lines[i].split()
    g1.addEdge(int(line[0]), int(line[1]))
    g_graphic.add_edge(int(line[0]), int(line[1]), color='black')
    
    
# wyswietl krawedze grafu:
for (u,v,c) in g_graphic.edges(data='color'):
    print(u,v)

pos = nx.spring_layout(g_graphic)
plot = nx.draw(g_graphic, pos=pos, node_size=800, with_labels=True)
plt.show()
# setting labels
plt.title("Fleury working...")

g1.printEulerTour(g_graphic, pos)

    
# ZADANIE: SPRAWDZAC CZY WPROWADZONY GRAF JEST EULEROWSKI
# Graf przyjmuje krawedzie wielokrotne, ale petli jeszcze nie. Trzeba to dodać
# Graficznie graf nie wyswietla multikrawedzi, ale jak usuwana jest jedna z 2 tych samych to zostaje ta druga
# -co do petli nie wiem, nie sprawdzalam.

'''
Jeżeli wszystkie wierzchołki grafu nieskierowanego mają stopień parzysty, 
a graf jest spójny, to znaczy, że da się skonstruować zamkniętą ścieżkę Eulera nazywaną cyklem Eulera. 
Jeżeli najwyżej dwa wierzchołki mają nieparzysty stopień, to możliwe jest zbudowanie tylko takiej ścieżki Eulera, 
która nie jest zamknięta.
'''