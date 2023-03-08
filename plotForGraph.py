
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


print("Number of:")
vNumber = int(input("Vertices = "))
G = createGraph(vNumber)
showGraph(G)

# algorytm Fleuryego

# https://th-www.if.uj.edu.pl/ztms/download/MScTheses/Lukasz_Malinowski_MSc.pdf
# https://www.geeksforgeeks.org/fleurys-algorithm-for-printing-eulerian-path/
# https://networkx.org/documentation/stable/_downloads/networkx_reference.pdf


from main.algorithms.dfs import DfsIterative

class Fleury( object ):
    #algorytm wyszukujący cykl Eulera w grafie
    
    def __init__(self, graph):
        # inicjacja algorytmu grafem, 
        # na ktorym zostanie wywolany algorytm szukania cyklu Eulera
        self.graph = graph
        
    def run(self, source):
        # metoda uruchamiajaca algorytm szukajacy cyklu Eulera. 
        # Wynik algorytmu, czyli sciezka jaka nalezy przejsc aby uzyskac cykl Eulera
        # zapisywany jest w zmiennej self.current_trail
        node = source
        self.current_trail = [node]
        graph_copy = self.graph.copy()
        while list(graph_copy.iteradjacent(node)):
            for edge in list(graph_copy.iteroutedges(node)):
                if not self._is_bridge(edge, graph_copy):
                    break
            graph_copy.del_edge(edge)
            self.current_trail.append(edge.target)
            node = edge.target
            
            
    def _is_bridge(self, edge, graph):
        # metoda sprawdza czy podana krawedz w 
        # grafie przekazanym jako drugi argument jest mostem
        # czyli krawedzia rozpoznajaca graf w przypadku jej usuniecia
        dfs = DfsIterative(graph)
        list1 =list()
        list2 = list()
        dfs.run(edge.source,
                pre_action=lambda node: list1.append(node))
        graph.del_edge(edge)
        dfs.run(edge.source,
                pre_action=lambda node: list2.append(node))
        graph.add_edge(edge)
        return len(list1) != len(list2)
                