from tkinter import *

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


w = Canvas(window, width=250, height=200)
w.create_rectangle(10, 10, 100, 100, fill="", outline = 'blue')
w.pack()

# LABEL
lbl_welcome = Label(window, text = "Welcome to algorithm Fleury program!", fg='red', font=("Helvetica", 16))
lbl_welcome.place(relx=0.5, rely=0.1, anchor=CENTER)

lbl_menu = Label(window, text = "MENU", fg='red', font=("Helvetica", 16))
lbl_menu.place(relx=0.05, rely=0.35, anchor=W)


lbl_cr_graph = Label(window, text = "Create your own graph", fg = 'blue', font=("Helvetica", 16))
lbl_cr_graph.place(relx = 0.05, rely=0.5, anchor=W)

lbl_load_graph = Label(window, text = "Load your graph from a text file", fg = 'blue', font=("Helvetica", 16))
lbl_load_graph.place(relx = 0.05, rely=0.6, anchor=W)

btn_cr_graph = Button(window, text = " Start! ", fg = 'blue', font=("Helvetica", 12))
btn_cr_graph.place(relx = 0.8, rely=0.5, anchor=W)

btn_load_graph = Button(window, text = " Start! ", fg = 'blue', font=("Helvetica", 12))
btn_load_graph.place(relx = 0.8, rely=0.6, anchor=W)





# ENTRY
#txtField = Entry(window, text = "This is enrty Widget", bd = 5)
#txtField.place(x=80, y=150)



window.title('Fleury Algorithm')              # title of the window
window.geometry("500x400+10+10")          # width * height + XPOS + YPOS
window.mainloop()  




