# Modules
import matplotlib.pyplot as plt
import networkx as nx

from math import pi
import matplotlib.pyplot as plt
import numpy as np

from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename
from tkinter import *   

from collections import defaultdict
import keyboard

import bisect


# -------------------------------------------------------------------------------------------------

# START MENU - Window
finalList = []
filename = "" 
nVertices = 0
edges_list = []
isDirected = False
loadingGraph = False
window = Tk() 

lbl_line1 = Label(window, text = "_"*100, fg='grey', font=("Helvetica", 18, "bold"), bg='white')
lbl_line1.place(relx=0.5, rely=0.2, anchor=CENTER)

lbl_line2 = Label(window, text = "_"*100, fg='grey', font=("Helvetica", 18, "bold"), bg='white')
lbl_line2.place(relx=0.5, rely=0.8, anchor=CENTER)

# LABEL
lbl_welcome = Label(window, text = "Welcome to algorithm Fleury program!", fg='#2B45EC', font=("Helvetica", 23), bg='white')
lbl_welcome.place(relx=0.5, rely=0.1, anchor=CENTER)

lbl_menu = Label(window, text = "MENU", fg='#419BE9', font=("Helvetica", 20, "bold"), bg='white')
lbl_menu.place(relx=0.5, rely=0.35, anchor=CENTER)


lbl_cr_graph = Label(window, text = "Create your own graph", fg = '#56575A', font=("Helvetica", 18), bg='white')
lbl_cr_graph.place(relx = 0.1, rely=0.55, anchor=W)

lbl_load_graph = Label(window, text = "Load your graph from a text file", fg = '#56575A', font=("Helvetica", 18), bg='white')
lbl_load_graph.place(relx = 0.1, rely=0.67, anchor=W)


# load graph option
def load_graph_clicked():
    global loadingGraph
    global filename
    loadingGraph = True
    filename = askopenfilename(filetypes=[("Text files", "*.txt")]) # show an "Open" dialog box and return the path to the selected file
    window.destroy()


# create graph option - new window
def create_graph_clicked():
    window.destroy()
    
    window1 = Tk()

    # vertices
    lbl_desc_v = Label(window1, text = "Type number of vertices in the graph: ", fg='#2B45EC', font=("Helvetica", 16, "bold"), bg='white')
    lbl_desc_v.place(relx=0.1, rely=0.08, anchor=W)
    
    lbl_desc_vScheme = Label(window1, text = "(vertex numbers begin with 0) ", fg='#56575A', font=("Helvetica", 16), bg='white')
    lbl_desc_vScheme.place(relx=0.1, rely=0.13, anchor=W)

    ntr_vertices = Entry(window1, width = 5, bd=4, font=("Helvetica", 20))
    ntr_vertices.place(relx=0.1, rely=0.2, anchor=W)

    # is it directed?
    lbl_desc_v = Label(window1, text = "Mark what kind of graph it should be: ", fg='#2B45EC', font=("Helvetica", 16, "bold"), bg='white')
    lbl_desc_v.place(relx=0.1, rely=0.3, anchor=W)

    def check_if_directed():
        global isDirected
        if choice.get() == 1:
            isDirected = True
        if choice.get() == 2:
            isDirected = False
            
    choice = IntVar()
    choice.set(2)
    directed = Radiobutton(window1, text="Directed", variable= choice, value= 1, fg='#56575A', font=("Helvetica", 14), bg='white', selectcolor='white', command = check_if_directed )
    directed.place(relx=0.1, rely=0.37, anchor=W)
    not_directed = Radiobutton(window1, text="Undirected", variable= choice, value= 2, fg='#56575A', font=("Helvetica", 14), bg='white', selectcolor='white', command = check_if_directed)
    not_directed.place(relx=0.3, rely=0.37, anchor=W)


    # edges
    lbl_desc = Label(window1, text = "Type edge vertices and confirm by clicking add button ", fg='#2B45EC', font=("Helvetica", 16, "bold"), bg='white')
    lbl_desc.place(relx=0.1, rely=0.5, anchor=W)
        
    lbl_scheme = Label(window1, text = "Scheme: v1[space]v2 ", fg='#56575A', font=("Helvetica", 16), bg='white')
    lbl_scheme.place(relx=0.1, rely=0.56, anchor=W)

    ntr_edge = Entry(window1, width = 20, bd=4, font=("Helvetica", 20))
    ntr_edge.place(relx=0.1, rely=0.62, anchor=W)

    def clicked_add_edge():
        global edges_list
        edges_list.append(tuple(list(map(int, ntr_edge.get().split() )))) # (1, 2) przedzielona spacja z prawej strony
        ntr_edge.delete(0, END)
        
    btn_add = Button(window1, text = "  Add ", fg = 'black', font=("Helvetica", 13, "bold"), padx=3, pady=3, activebackground='grey', command=clicked_add_edge)
    btn_add.place(relx = 0.58, rely=0.62, anchor=W)

    # end
    def get_vertices_number():
        global nVertices
        nVertices = int(ntr_vertices.get())
        window1.destroy()

    btn_end = Button(window1, text = "  DONE! ", fg = 'black', font=("Helvetica", 13, "bold"), padx=3, pady=3, activebackground='grey', command=get_vertices_number)
    btn_end.place(relx = 0.8, rely=0.8, anchor=W)

    window1.title('Create your own graph')
    window1.geometry("700x600+10+10")
    window1.configure(bg='white')
    window1.mainloop()




btn_cr_graph = Button(window, text = "  Start  ", fg = 'black', font=("Helvetica", 13), padx=3, pady=3, activebackground='grey', command=create_graph_clicked)
btn_cr_graph.place(relx = 0.75, rely=0.55, anchor=W)

btn_load_graph = Button(window, text = "  Start  ", fg = 'black', font=("Helvetica", 13), padx=3, pady=3, activebackground='grey', command=load_graph_clicked)
btn_load_graph.place(relx = 0.75, rely=0.67, anchor=W)


window.title('Fleury Algorithm')              # title of the window
window.geometry("700x600+10+10")              # width * height + XPOS + YPOS
window.configure(bg='white')
window.mainloop()  

# -------------------------------------------------------------------------------------------------

# Canvas creation
plt.ion()
fig = plt.figure(figsize=(10,8))
plot = fig.add_subplot()


# GRAPHICAL REPRESENTATION OF THE FLEURY ALGORITHM ---------------------------------------------------------------------------------
# the edge of the graph under consideration is green
def graphic_consideredEdge(G, u, v, pos, colorr):
    if G.has_edge(u,v):
        plt.clf()
        G.remove_edge(u,v)
        G.add_edge(u, v, color=colorr) # edge with color
        
        edges = G.edges()
        colors = [c for (u,v,c) in g_graphic.edges(data='color')]
        
        # re-drawing the figure
        plt.clf()  
        nx.draw(G, pos=pos, edge_color = colors, node_size=800, with_labels=True)
        fig.canvas.draw()
        
        # to flush the GUI events
        fig.canvas.flush_events()
        keyboard.wait('space')
        
# removing edge from the graph (plot)
def graphic_removeEdge(G, u, v, pos):
    if G.has_edge(u,v):
        G.remove_edge(u,v)
    
        # re-drawing the figure
        plt.clf()
        nx.draw(G, pos=pos, node_size=800, with_labels=True)
        fig.canvas.draw()
        
        # to flush the GUI events
        fig.canvas.flush_events()
        keyboard.wait('space')

# -------------------------------------------------------------------------------------------------

# FLEURY ALGORITHM --------------------------------------------------------------------------------
class Graph:
  
    # constructor
    def __init__(self,vertices):
        self.V= vertices #No. of vertices
        self.graph = defaultdict(list) # default dictionary to store graph
        self.Time = 0
  
    # function to add an edge to graph
    def addEdge(self,u,v, isDirected):
        if isDirected == False:          # if graph NOT directed
            self.graph[u].append(v)
            self.graph[v].append(u)
        else:                       # else
            self.graph[u].append(v)

 
    # This function removes edge u-v from graph   
    def rmvEdge(self, u, v, isDirected):
        for index, key in enumerate(self.graph[u]):
            if key == v:
                self.graph[u].pop(index)
                break
        if isDirected == False:
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
    def isValidNextEdge(self, u, v, graphic_graph, pos, isDirected):
        # The edge u-v is valid in one of the following two cases:
  
        #  1) If v is the only adjacent vertex of u
        if len(self.graph[u]) == 1:
            graphic_consideredEdge(graphic_graph, u, v, pos, 'green')
            return True
        else:
            # 2) If there are multiple adjacents, then u-v is not a bridge
            
               
            # Steps to check if u-v is a bridge:
            # 2.a) count of vertices reachable from u  
            visited =[False]*(self.V)
            count1 = self.DFSCount(u, visited) 
 
            # 2.b) Remove edge (u, v) and after removing the edge, 
            #      count vertices reachable from u
            self.rmvEdge(u, v, isDirected)
            
            visited =[False]*(self.V)
            if isDirected:
                count2 = self.DFSCount(v, visited)
            else:
                count2 = self.DFSCount(u, visited)
        
            #2.c) Add the edge back to the graph
            bisect.insort(self.graph[u], v) 
            #self.addEdge(u,v, isDirected)

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
            print("Rozpatrywana krawedz ", u, " -> " if isDirected else " - " , v)
            #If edge u-v is not removed and it's a a valid next edge
            if self.isValidNextEdge(u, v, graphic_graph, pos, isDirected):
                finalList.append("%d-%d" %(u,v))
                graphic_removeEdge(graphic_graph, u, v, pos)
                self.rmvEdge(u, v, isDirected)
                self.printEulerUtil(v, graphic_graph, pos)
 
 
     
    # The main function that print Eulerian Trail. 
    # It first finds an odd degree vertex (if there is any) 
    # and then calls printEulerUtil() to print the path/circle:
    def printEulerTour(self, graphic_graph, pos, isEulerian):
        #Find a start vertex -  with odd degree if graph is semieulerian
        u = 0
        if not isEulerian:
            for i in range(0, self.V):
                if isDirected:
                    edges = 0
                    for v in range(0, self.V):
                        if i in self.graph[v]:
                            edges = edges+1
                    edges = edges + len(self.graph[i])
                    if edges %2 != 0 :
                        u = i
                        break
                else:
                    if len(self.graph[i]) %2 != 0 :
                        u = i
                        break
            # Print tour starting from odd vertex
            self.printEulerUtil(u, graphic_graph, pos)
        else:
            self.printEulerUtil(u, graphic_graph, pos)
        
# ----------------------------------------------------------------------------------------------

if __name__ == "__main__":
    #Creating a graph based on the menu selections
    if loadingGraph == True:    # if graph has to be loaded
        # open file and read lines
        with open(filename) as f:
            lines = f.readlines()
            
        # read if graph is directed
        isDirected = True if lines[0].split()[0] == '->' else False
        # read number of vertices
        nVertices = int(lines[1])
        g1 = Graph(nVertices)

        if isDirected:
            g_graphic = nx.MultiDiGraph()   # dimultigraph, because it can have multiple edges/petals
        else:  
            g_graphic = nx.MultiGraph()     # Multigraph, because it can have multiple edges/petals
            
        # read edges
        for i in range(2, len(lines)):
            line = lines[i].split()
            g1.addEdge(int(line[0]), int(line[1]), isDirected)
            g_graphic.add_edge(int(line[0]), int(line[1]), color='black')
            
    else:                       # if graph has to be created
        g1 = Graph(nVertices)
        
        if isDirected:
            g_graphic = nx.MultiDiGraph() # dimultigraf, bo może miec krawedzie wielokrotne/petle
        else:
            g_graphic = nx.MultiGraph() # multigraf, bo może miec krawedzie wielokrotne/petle

        for i in range(len(edges_list)):
            g1.addEdge(edges_list[i][0], edges_list[i][1], isDirected)
            g_graphic.add_edge(edges_list[i][0], edges_list[i][1], color='black')


    # checking if graph is eulerian/semieulerian
    isEulerian = nx.is_eulerian(g_graphic)
    isSemiEulerian = nx.is_semieulerian(g_graphic)

    if isEulerian or isSemiEulerian:
        # drawing graph
        pos = nx.spring_layout(g_graphic)
        plot = nx.draw(g_graphic, pos=pos, node_size=800, with_labels=True)
        plt.show()
        # setting labels
        plt.title("Fleury working...")

        # starting the algorithm
        g1.printEulerTour(g_graphic, pos, isEulerian)
        
        
        # result window
        end_window = Tk()
        
        lbl_end = Label(end_window, text = "Result", fg='#2B45EC', font=("Helvetica", 22, "bold"), bg='white')
        lbl_end.place(relx=0.5, rely=0.32, anchor=CENTER)
        
        txt = Text(end_window, width=50, height=5, bd=4, font=("Helvetica", 18))
        txt.place(relx=0.5, rely=0.5, anchor=CENTER)
        for edge in finalList:
            txt.insert(END, edge + "   ")
        
        end_window.title('Results')                     # title of the window
        end_window.geometry("700x600+10+10")            # width * height + XPOS + YPOS
        end_window.configure(bg='white')
        end_window.mainloop()  
        
    else:
        plt.close(fig)
        
        euler_window = Tk()
        lbl_euler = Label(euler_window, text="Graph is not eulerian or semieulerian", fg='#2B45EC', font=("Helvetica", 22, "bold"), bg='white')
        lbl_euler.place(relx=0.5, rely=0.5, anchor=CENTER)
        
        euler_window.title('Error!')                      # title of the window
        euler_window.geometry("700x200+10+10")            # width * height + XPOS + YPOS
        euler_window.configure(bg='white')
        euler_window.mainloop() 
        


