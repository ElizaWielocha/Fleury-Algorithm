import networkx as nx
import matplotlib.pyplot as plt
import pygraphviz

g1 = nx.MultiGraph(directed=True)

node1 = 'a'
node2 = 'b'

g1.add_edge(node1,node2,key=1)
g1.add_edge(node2,node1,key=2)

A = nx.to_agraph(g1)
A.add_subgraph()


plt.plot()
nx.draw(A, prog='dot')
#nx.draw(g1, with_labels=True, arrows = True, connectionstyle='arc3, rad = 0.1')
plt.show()



