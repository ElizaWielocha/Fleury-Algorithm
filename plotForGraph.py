
import matplotlib.pyplot as plt
import networkx as nx

# Generator grafu
def createGraph(vNumber):
    isConnected = False
    
    while isConnected == False:
        # erdos_renyi_graph(n, p, seed=None, directed=False) # funkcja pozwalajaca na stworzenie grafu spojnego
        G = nx.erdos_renyi_graph(vNumber, 0.5, seed=123, directed=False)
        isConnected = nx.is_connected(G)
    
    return G

# wyswietlanie grafu
def showGraph(G):
    plot = plt.subplot()
    nx.draw(G, node_size=800, with_labels=True)
    plt.show()


#print("Number of:")
#vNumber = int(input("Vertices = "))
#G = createGraph(vNumber)
#showGraph(G)

# algorytm Fleuryego

# https://th-www.if.uj.edu.pl/ztms/download/MScTheses/Lukasz_Malinowski_MSc.pdf
# https://www.geeksforgeeks.org/fleurys-algorithm-for-printing-eulerian-path/
# https://networkx.org/documentation/stable/_downloads/networkx_reference.pdf


from collections import defaultdict
  
#This class represents an undirected graph using adjacency list representation
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
        for index, key in enumerate(self.graph[v]):
            if key == u:
                self.graph[v].pop(index)
 
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
    def isValidNextEdge(self, u, v):
        # The edge u-v is valid in one of the following two cases:
  
          #  1) If v is the only adjacent vertex of u
        if len(self.graph[u]) == 1:
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
            return False if count1 > count2 else True
 
 
    # Print Euler tour starting from vertex u
    def printEulerUtil(self, u):
        #Recur for all the vertices adjacent to this vertex
        for v in self.graph[u]:
            #If edge u-v is not removed and it's a a valid next edge
            if self.isValidNextEdge(u, v):
                print("%d-%d " %(u,v)),
                self.rmvEdge(u, v)
                self.printEulerUtil(v)
 
 
     
    '''The main function that print Eulerian Trail. It first finds an odd
   degree vertex (if there is any) and then calls printEulerUtil()
   to print the path '''
    def printEulerTour(self):
        #Find a vertex with odd degree
        u = 0
        for i in range(self.V):
            if len(self.graph[i]) %2 != 0 :
                u = i
                break
        # Print tour starting from odd vertex
        print ("\n")
        self.printEulerUtil(u)
 
# Create a graph given in the above diagram
 
g1 = Graph(5)
g_temp = createGraph(5)
showGraph(g_temp)

for u,v in g_temp.edges():
    g1.addEdge(u,v)


g1.printEulerTour()
    


