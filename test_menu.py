from tkinter import *
from tkinter.filedialog import askopenfilename
'''
window = Tk()                             # setup the application object
# This will create a top-level window (root) having a frame with a title bar, 
# control box with the minimize and close buttons, 
# and a client area to hold other widgets.

# These window properties 
#window.title('Hello Python')              # title of the window
#window.geometry("300x200+10+20")          # width * height + XPOS + YPOS
#window.mainloop()                         # object enters an event listening loop
# The application is now constantly waiting for any event generated on the elements in it.



# BUTTON
# Buton(window, attributes)
Attributes:
    text : caption of the button
    bg : background colour
    fg : foreground colour
    font : font name and size
    image : to be displayed instead of text
    command : function to be called when clicked



w = Canvas(window, width=471, height=351, highlightthickness=0)
w.configure(bg='black')
w.create_rectangle(5, 100, 470, 350, fill="", outline = 'white')
w.pack()

# LABEL
lbl_welcome = Label(window, text = "Welcome to algorithm Fleury program!", fg='yellow', font=("Helvetica", 20), bg='black')
lbl_welcome.place(relx=0.5, rely=0.1, anchor=CENTER)

lbl_menu = Label(window, text = "MENU", fg='green', font=("Helvetica", 18, "bold"), bg='black')
lbl_menu.place(relx=0.5, rely=0.35, anchor=CENTER)


lbl_cr_graph = Label(window, text = "Create your own graph", fg = 'white', font=("Helvetica", 15), bg='black')
lbl_cr_graph.place(relx = 0.1, rely=0.55, anchor=W)

lbl_load_graph = Label(window, text = "Load your graph from a text file", fg = 'white', font=("Helvetica", 15), bg='black')
lbl_load_graph.place(relx = 0.1, rely=0.67, anchor=W)


def load_graph_clicked():
    Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
    filename = askopenfilename(filetypes=[("Text files", "*.txt")]) # show an "Open" dialog box and return the path to the selected file
    window.destroy()

def create_graph_clicked():
    print("Working")

btn_cr_graph = Button(window, text = "  Start  ", fg = 'black', font=("Helvetica", 13), command=create_graph_clicked)
btn_cr_graph.place(relx = 0.75, rely=0.55, anchor=W)

btn_load_graph = Button(window, text = "  Start  ", fg = 'black', font=("Helvetica", 13), command=load_graph_clicked)
btn_load_graph.place(relx = 0.75, rely=0.67, anchor=W)



# ENTRY
#txtField = Entry(window, text = "This is enrty Widget", bd = 5)
#txtField.place(x=80, y=150)


window.title('Fleury Algorithm')              # title of the window
window.geometry("500x400+10+10")          # width * height + XPOS + YPOS
window.configure(bg='black')
window.mainloop()  

'''
edges_list = []

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
        print("Working")
        
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
    print(edges_list)
    
btn_add = Button(window1, text = "  Add ", fg = 'green', font=("Helvetica", 13, "bold"), padx=3, pady=3, activebackground='grey', command=clicked_add_edge)
btn_add.place(relx = 0.58, rely=0.62, anchor=W)


# end
def get_vertices_number():
    global nVertices
    nVertices = int(ntr_vertices.get())
    print(nVertices)
    window1.destroy()

btn_end = Button(window1, text = "  DONE! ", fg = 'green', font=("Helvetica", 13, "bold"), padx=3, pady=3, activebackground='grey', command=get_vertices_number)
btn_end.place(relx = 0.8, rely=0.8, anchor=W)



window1.title('Fleury Algorithm')              # title of the window
window1.geometry("700x600+10+10")              # width * height + XPOS + YPOS
window1.configure(bg='black')
window1.mainloop()

