
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


