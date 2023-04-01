import matplotlib.pyplot as plt
import networkx as nx

from math import pi
import matplotlib.pyplot as plt
import numpy as np
import time

from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename
from tkinter import *   

from collections import defaultdict
import keyboard


# START MENU 
window = Tk()   
finalList = []
filename = "" 
nVertices = 0
edges_list = []
isDirected = False
loadingGraph = False


lbl_line1 = Label(window, text = "_"*100, fg='white', font=("Helvetica", 18, "bold"), bg='black')
lbl_line1.place(relx=0.5, rely=0.2, anchor=CENTER)

lbl_line2 = Label(window, text = "_"*100, fg='white', font=("Helvetica", 18, "bold"), bg='black')
lbl_line2.place(relx=0.5, rely=0.8, anchor=CENTER)

# LABEL
lbl_welcome = Label(window, text = "Welcome to algorithm Fleury program!", fg='yellow', font=("Helvetica", 23), bg='black')
lbl_welcome.place(relx=0.5, rely=0.1, anchor=CENTER)

lbl_menu = Label(window, text = "MENU", fg='green', font=("Helvetica", 20, "bold"), bg='black')
lbl_menu.place(relx=0.5, rely=0.35, anchor=CENTER)


lbl_cr_graph = Label(window, text = "Create your own graph", fg = 'white', font=("Helvetica", 18), bg='black')
lbl_cr_graph.place(relx = 0.1, rely=0.55, anchor=W)

lbl_load_graph = Label(window, text = "Load your graph from a text file", fg = 'white', font=("Helvetica", 18), bg='black')
lbl_load_graph.place(relx = 0.1, rely=0.67, anchor=W)


# zaladuj graf
def load_graph_clicked():
    global loadingGraph
    global filename
    loadingGraph = True
    filename = askopenfilename(filetypes=[("Text files", "*.txt")]) # show an "Open" dialog box and return the path to the selected file
    window.destroy()


# Stworz graf - nowe okno
def create_graph_clicked():
    window.destroy()
    
    window1 = Tk()

    # vertices
    lbl_desc_v = Label(window1, text = "Type number of vertices in the graph: ", fg='yellow', font=("Helvetica", 16, "bold"), bg='black')
    lbl_desc_v.place(relx=0.1, rely=0.1, anchor=W)

    ntr_vertices = Entry(window1, width = 5, font=("Helvetica", 20))
    ntr_vertices.place(relx=0.1, rely=0.17, anchor=W)

    # is it directed?
    lbl_desc_v = Label(window1, text = "Mark what kind of graph it should be: ", fg='yellow', font=("Helvetica", 16, "bold"), bg='black')
    lbl_desc_v.place(relx=0.1, rely=0.3, anchor=W)

    def check_if_directed():
        global isDirected
        if choice.get() == 1:
            isDirected = True
            
    choice = IntVar()
    choice.set(2)
    directed = Radiobutton(window1, text="Directed", variable= choice, value= 1, fg='white', font=("Helvetica", 14), bg='black', selectcolor='black', command = check_if_directed )
    directed.place(relx=0.1, rely=0.37, anchor=W)
    not_directed = Radiobutton(window1, text="Undirected", variable= choice, value= 2, fg='white', font=("Helvetica", 14), bg='black', selectcolor='black', command = check_if_directed)
    not_directed.place(relx=0.3, rely=0.37, anchor=W)


    # edges
    lbl_desc = Label(window1, text = "Type edge vertices and confirm by clicking add button ", fg='yellow', font=("Helvetica", 16, "bold"), bg='black')
    lbl_desc.place(relx=0.1, rely=0.5, anchor=W)
        
    lbl_scheme = Label(window1, text = "Scheme: v1 v2 ", fg='white', font=("Helvetica", 16), bg='black')
    lbl_scheme.place(relx=0.1, rely=0.56, anchor=W)

    ntr_edge = Entry(window1, width = 20, font=("Helvetica", 20))
    ntr_edge.place(relx=0.1, rely=0.62, anchor=W)

    def clicked_add_edge():
        global edges_list
        edges_list.append(tuple(list(map(int, ntr_edge.get().split() )))) # (1, 2) przedzielona spacja z prawej strony
        ntr_edge.delete(0, END)
        
    btn_add = Button(window1, text = "  Add ", fg = 'green', font=("Helvetica", 13, "bold"), padx=3, pady=3, activebackground='grey', command=clicked_add_edge)
    btn_add.place(relx = 0.58, rely=0.62, anchor=W)

    # end
    def get_vertices_number():
        global nVertices
        nVertices = int(ntr_vertices.get())
        window1.destroy()

    btn_end = Button(window1, text = "  DONE! ", fg = 'green', font=("Helvetica", 13, "bold"), padx=3, pady=3, activebackground='grey', command=get_vertices_number)
    btn_end.place(relx = 0.8, rely=0.8, anchor=W)

    window1.title('Fleury Algorithm')
    window1.geometry("700x600+10+10")
    window1.configure(bg='black')
    window1.mainloop()




btn_cr_graph = Button(window, text = "  Start  ", fg = 'black', font=("Helvetica", 13), padx=3, pady=3, activebackground='grey', command=create_graph_clicked)
btn_cr_graph.place(relx = 0.75, rely=0.55, anchor=W)

btn_load_graph = Button(window, text = "  Start  ", fg = 'black', font=("Helvetica", 13), padx=3, pady=3, activebackground='grey', command=load_graph_clicked)
btn_load_graph.place(relx = 0.75, rely=0.67, anchor=W)


window.title('Fleury Algorithm')              # title of the window
window.geometry("700x600+10+10")              # width * height + XPOS + YPOS
window.configure(bg='black')
window.mainloop()  

# -------------------------------------------------------------------------------------------------

# tworzenie plotna
plt.ion()
fig = plt.figure()
plot = fig.add_subplot()


# GRAFICZNIE FLEURY ---------------------------------------------------------------------------------
# rozpatrywana krawedz grafu jest zielona
def graphic_consideredEdge(G, u, v, pos, colorr):
    if G.has_edge(u,v):
        plt.clf()
        G.remove_edge(u,v)
        G.add_edge(u, v, color=colorr)
        
        edges = G.edges()
        colors = [c for (u,v,c) in g_graphic.edges(data='color')]
        
        plt.clf() # nowe
        nx.draw(G, pos=pos, edge_color = colors, node_size=800, with_labels=True)
        fig.canvas.draw()
        
        # to flush the GUI events
        fig.canvas.flush_events()
        keyboard.wait('space')
        
# usuwanie z grafu (plot) krawedzi
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
    
class Graph:
  
    def __init__(self,vertices):
        self.V= vertices #No. of vertices
        self.graph = defaultdict(list) # default dictionary to store graph
        self.Time = 0
  
    # function to add an edge to graph
    def addEdge(self,u,v, isDirected):
        if not isDirected:
            self.graph[u].append(v)
            self.graph[v].append(u)
        else:
            self.graph[u].append(v)
 
    # This function removes edge u-v from graph   
    def rmvEdge(self, u, v, isDirected):
        for index, key in enumerate(self.graph[u]):
            if key == v:
                self.graph[u].pop(index)
                break
        if not isDirected:
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
            '''
             2) If there are multiple adjacents, then u-v is not a bridge
                 Do following steps to check if u-v is a bridge
  
            2.a) count of vertices reachable from u'''   
            visited =[False]*(self.V)
            count1 = self.DFSCount(u, visited) 
 
            '''2.b) Remove edge (u, v) and after removing the edge, count
                vertices reachable from u'''
            self.rmvEdge(u, v, isDirected)
            
            visited =[False]*(self.V)
            if isDirected:
                count2 = self.DFSCount(v, visited)
            else:
                count2 = self.DFSCount(u, visited)
        
            #2.c) Add the edge back to the graph
            self.addEdge(u,v, isDirected)

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
            if self.isValidNextEdge(u, v, graphic_graph, pos, isDirected):
                finalList.append("%d-%d" %(u,v))
                #print("%d-%d " %(u,v))
                graphic_removeEdge(graphic_graph, u, v, pos)
                self.rmvEdge(u, v, isDirected)
                self.printEulerUtil(v, graphic_graph, pos)
 
 
     
    '''The main function that print Eulerian Trail. It first finds an odd
   degree vertex (if there is any) and then calls printEulerUtil()
   to print the path '''
    def printEulerTour(self, graphic_graph, pos, isEulerian):
        #Find a start vertex -  with odd degree if isnt eulerian
        u = 0
        if not isEulerian:
            for i in range(self.V):
                if len(self.graph[i]) %2 != 0 :
                    u = i
                    break
            # Print tour starting from odd vertex
            #print ("\n")
            self.printEulerUtil(u, graphic_graph, pos)
        else:
            self.printEulerUtil(u, graphic_graph, pos)
        
# ----------------------------------------------------------------------------------------------

if __name__ == "__main__":
    if loadingGraph == True: # jesli graf jest wczytywany
        # przyklad z wczytywaniem z pliku tekstowego
        with open(filename) as f:
            lines = f.readlines()

        isDirected = True if lines[0].split()[0] == '->' else False
        nVertices = int(lines[1])
        g1 = Graph(nVertices)

        if isDirected:
            g_graphic = nx.MultiDiGraph() # dimultigraf, bo może miec krawedzie wielokrotne/petle
        else:
            g_graphic = nx.MultiGraph() # multigraf, bo może miec krawedzie wielokrotne/petle
            
        for i in range(2, len(lines)):
            line = lines[i].split()
            g1.addEdge(int(line[0]), int(line[1]), isDirected)
            g_graphic.add_edge(int(line[0]), int(line[1]), color='black')
    else: # jesli graf jest tworzony
        g1 = Graph(nVertices)
        
        if isDirected:
            g_graphic = nx.MultiDiGraph() # dimultigraf, bo może miec krawedzie wielokrotne/petle
        else:
            g_graphic = nx.MultiGraph() # multigraf, bo może miec krawedzie wielokrotne/petle

        for i in range(len(edges_list)):
            g1.addEdge(edges_list[i][0], edges_list[i][1], isDirected)
            g_graphic.add_edge(edges_list[i][0], edges_list[i][1], color='black')


    isEulerian = nx.is_eulerian(g_graphic)
    isSemiEulerian = nx.is_semieulerian(g_graphic)


    if isEulerian or isSemiEulerian:
        pos = nx.spring_layout(g_graphic)
        plot = nx.draw(g_graphic, pos=pos, node_size=800, with_labels=True)
        plt.show()
        # setting labels
        plt.title("Fleury working...")

        g1.printEulerTour(g_graphic, pos, isEulerian)
        
        end_window = Tk()
        
        lbl_end = Label(end_window, text = "Result", fg='yellow', font=("Helvetica", 22, "bold"), bg='black')
        lbl_end.place(relx=0.5, rely=0.32, anchor=CENTER)
        
        txt = Text(end_window, width=50, height=5, font=("Helvetica", 18))
        txt.place(relx=0.5, rely=0.5, anchor=CENTER)
        for edge in finalList:
            txt.insert(END, edge + "   ")
        
        end_window.title('Fleury Algorithm')              # title of the window
        end_window.geometry("700x600+10+10")              # width * height + XPOS + YPOS
        end_window.configure(bg='black')
        end_window.mainloop()  
        
    else:
        plt.close(fig)
        
        euler_window = Tk()
        lbl_euler = Label(euler_window, text="Graph is not eulerian or semieulerian", fg='yellow', font=("Helvetica", 22, "bold"), bg='black')
        lbl_euler.place(relx=0.5, rely=0.5, anchor=CENTER)
        
        euler_window.title('Fleury Algorithm')              # title of the window
        euler_window.geometry("700x200+10+10")              # width * height + XPOS + YPOS
        euler_window.configure(bg='black')
        euler_window.mainloop() 
        

# ZROBIONE :)
# 1. Sprawdzanie czy wprowadzony graf jest semieulerowski/eulerowski.
# 2. Algorytm przyjmuje krawedzie wielokrotne i petle.
# 3. Graficznie graf wyswietla petle.
# 4. Chyba Algorytm przyjmuje tez grafy skierowane w zaleznosci od tego czy pliki ich zawieraja '-' lub '->'


# NIEZROBIONE :(
# 1. Graficznie graf naklada na siebie multikrawedzie zamiast pokazywac je np obok siebie. 

'''
Jeżeli wszystkie wierzchołki grafu nieskierowanego mają stopień parzysty, 
a graf jest spójny, to znaczy, że da się skonstruować zamkniętą ścieżkę Eulera nazywaną cyklem Eulera. 
Jeżeli najwyżej dwa wierzchołki mają nieparzysty stopień, to możliwe jest zbudowanie tylko takiej ścieżki Eulera, 
która nie jest zamknięta.
'''