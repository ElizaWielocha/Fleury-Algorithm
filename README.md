Graphic program to perform Fleury Algorithm on undirected and directed graphs.

Programming language: Python
Libraries used:
    - matplotlib
    - networkx
    - math
    - numpy
    - tkinter
    - collections
    - keyboard

RUNNING THE PROGRAM
The program is launched using the fleury.py file.
In the folder with the fleury.py file, type the command in the terminal:
| python fleury.py |
Or you can run the file through Visual Studio Code.
For the program to work you must have installed the libraries used to create it.

START MENU
![image](https://user-images.githubusercontent.com/61736185/231253665-668c63b4-a570-4e9a-a68c-b0c90981a912.png)
The initial menu has 2 options:
1. Create your own graph:
![image](https://user-images.githubusercontent.com/61736185/231253734-290198f2-1a2b-4120-9ecd-424754ecc183.png)
When you get to this option, you must:
    - enter how many vertices your graph has
    - select whether the graph is directed or undirected
    - add edges for this graph, e.g. 1 3 
    After each edge you enter, click the "Add" button to add it.
Important! The vertices in the graph start from 0.
When you finish typing in the edges you can click "DONE!".


2. Load your graph from the text file:
When you get to this option, you must:
    - select a .txt file representing the graph. Below is an example of what such a file must look like:
![image](https://user-images.githubusercontent.com/61736185/231255462-b4bf2999-1fda-41ef-8236-f5ccff33a8ea.png)

First line: 
arrow (->) means directed graph 
dash (-) indicates undirected graph

Second line:
number of vertices in the graph (the graph starts with vertex number 0)

Other lines:
Edges inscribed with the scheme: v1[space]v2


ALGORITHM OPERATION

You need to load into the program a graph that:
- is consistent
- undirected: either all its vertices have even degree or only 2 vertices have odd degree
- directed: the vertices must have the same number of incoming and outgoing edges
If the graph does not meet the above criteria, the program displays a message and should be closed:
![image](https://user-images.githubusercontent.com/61736185/231257278-73c8656c-173d-4914-b16b-d773d1973782.png)


If you create/load a good graph, the program displays the graph and runs the fleury algorithm.
![image](https://user-images.githubusercontent.com/61736185/231258452-3f8e5777-b68d-4207-934d-0117727e5970.png)

The next steps of the action are shown by pressing the [space] key.

A green highlighted edge means that the edge under consideration is not a bridge and therefore can be walked over. 
It is removed from the graph and added to the list, which will be displayed after the algorithm finishes as the result.

An edge highlighted in red means that this edge is a bridge and it is not yet possible to walk over it. In later steps it is considered again to check again if it is no longer a bridge. 
