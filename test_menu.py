from tkinter import *
from tkinter.filedialog import askopenfilename

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
'''
Attributes:
    text : caption of the button
    bg : background colour
    fg : foreground colour
    font : font name and size
    image : to be displayed instead of text
    command : function to be called when clicked
'''


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




