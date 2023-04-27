<h1>Graphic program to perform Fleury Algorithm on undirected and directed graphs.</h1>

<h4>Fleury Algorithm</h4> 
<p>-> Finds an Euler path/cycle in a graph.<br>  
It involves removing edges from the graph that are not bridges and adding them to the list until all edges in the graph are removed.  
A bridge is an edge through which you cannot go to the next vertex because, there is no way back from it. </p>

<h4>Programming language: Python</h4>  
<h4>Libraries used:</h4>  
    <p>- matplotlib<br>  
    - networkx  <br> 
    - math  <br> 
    - numpy  <br> 
    - tkinter  <br> 
    - collections  <br> 
    - keyboard </p>

_____________________________________________________________________________________________________________

<h2>RUNNING THE PROGRAM</h2>
<p>
The program is launched using the fleury.py file.  
In the folder with the fleury.py file, type the command in the terminal:  
| python fleury.py |  
Or you can run the file through Visual Studio Code.  
For the program to work you must have installed the libraries used to create it.
</p>

<h2>START MENU</h2> <br>  

![image](https://user-images.githubusercontent.com/61736185/234978717-d8e5b8cc-259a-4377-beca-346b4cfa15ac.png)

<h3>1. Create your own graph:  </h3>  

![image](https://user-images.githubusercontent.com/61736185/234984172-209e8f30-5514-4eea-9401-27171b678122.png)

<p>
When you get to this option, you must:  
    - enter how many vertices your graph has  
    - select whether the graph is directed or undirected  
    - add edges for this graph, e.g. 1 3   
    After each edge you enter, click the "Add" button to add it.  
Important! The vertices in the graph start from 0.  
When you finish typing in the edges you can click "DONE!".  
</p>


<h3>2. Load your graph from the text file:</h3>  
<p>
When you get to this option, you must select a .txt file representing the graph. 
Below is an example of what such a file must look like:  
</p>  

    ->
    8
    0 1
    0 4
    1 2
    1 0
    2 3
    2 5
    3 4
    3 6
    4 5
    4 7
    5 6
    5 1
    6 7
    6 2
    7 0
    7 3


<p>
First line:   
arrow (->) means directed graph   
dash (-) indicates undirected graph  

Second line:  
number of vertices in the graph (the graph starts with vertex number 0)  

Other lines:  
Edges inscribed with the scheme: v1[space]v2  
</p>

_____________________________________________________________________________________________________________

<h2>ALGORITHM OPERATION </h2>
<p>
You need to load into the program a graph that:  
        - is consistent  
        - undirected: either all its vertices have even degree or only 2 vertices have odd degree  
        - directed: the vertices must have the same number of incoming and outgoing edges  
If the graph does not meet the above criteria, the program displays a message and should be closed:  
</p>  

![image](https://user-images.githubusercontent.com/61736185/234979094-9f049af9-52f5-4dbe-93a2-b86aeb8c7119.png)

<p>
If you create/load a good graph, the program displays the graph and runs the fleury algorithm. 
</p>  

![image](https://user-images.githubusercontent.com/61736185/234978968-c42827a3-9c8c-4c1a-b8c1-9cf47d2e7a30.png)

<p>
The next steps of the action are shown by pressing the [space] key.  
</p><p>
A green highlighted edge means that the edge under consideration is not a bridge and therefore can be walked over.   
It is removed from the graph and added to the list, which will be displayed after the algorithm finishes as the result.  
</p><p>
An edge highlighted in red means that this edge is a bridge and it is not yet possible to walk over it. In later steps it is considered again to check again if it is no longer a bridge:  
</p>  

![image](https://user-images.githubusercontent.com/61736185/234979249-72daca4b-8352-4885-b834-3503eacd7e90.png)

_____________________________________________________________________________________________________________

<h2>RESULTS  </h2>
<p>
When the algorithm (with our help of pressing the spacebar) passes all the edges in the graph, the result is displayed: the path or Euler cycle read from the left.
</p>  

![image](https://user-images.githubusercontent.com/61736185/234979344-e47b7638-8c95-403b-ade6-68a4f62d8ed2.png)


