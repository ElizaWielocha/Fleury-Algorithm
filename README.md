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
![image](https://user-images.githubusercontent.com/61736185/231255323-858b1c47-238b-43f1-b115-172a7dfb9a74.png)
First line: 
arrow (->) means directed graph 
dash (-) indicates undirected graph

Second line:
number of vertices in the graph (the graph starts with vertex number 0)

Other lines:
Edges inscribed with the scheme: v1[space]v2

