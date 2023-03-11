import matplotlib.pyplot as plt
import networkx as nx

# Generator grafu
def createGraph(vNumber):
    isConnected = False
    
    while isConnected == False:
        # erdos_renyi_graph(n, p, seed=None, directed=False) # funkcja pozwalajaca na stworzenie grafu spojnego
        G = nx.erdos_renyi_graph(vNumber, 0.5, seed=123, directed=False)
        isConnected = nx.is_connected(G)
    
    for u,v in G.edges():
        G.remove_edge(u,v)
        G.add_edge(u,v, color = 'black')
        
    return G


G = createGraph(6)

from math import pi
import matplotlib.pyplot as plt
import numpy as np
import time
 
# enable interactive mode
plt.ion()
 
# creating subplot and figure
fig = plt.figure()
plot = fig.add_subplot()
pos = nx.spring_layout(G)
plot = nx.draw(G, pos=pos, node_size=800, with_labels=True)
plt.show()
 
# setting labels
plt.title("Updating plot...")
 
# looping
for u,v in G.edges():
    # zielona krawedz
    plt.clf()
    G.remove_edge(u,v)
    G.add_edge(u, v, color='green')
    
    edges = G.edges()
    colors = [G[u][v]['color'] for u,v in G.edges()]
    
    nx.draw(G, pos=pos, edge_color = colors, node_size=800, with_labels=True)
    fig.canvas.draw()
     
    # to flush the GUI events
    fig.canvas.flush_events()
    time.sleep(2)
    
   
    # usuwanie krawedzi
    G.remove_edge(u,v)
    print(f'{u} - {v}')
    #line1.set_xdata(x*_)
    #line1.set_ydata(y)
 
    # re-drawing the figure
    plt.clf()
    nx.draw(G, pos=pos, node_size=800, with_labels=True)
    fig.canvas.draw()
     
    # to flush the GUI events
    fig.canvas.flush_events()
    time.sleep(3)