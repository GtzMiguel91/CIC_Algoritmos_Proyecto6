from node import Node
from edge import Edge
from queue import PriorityQueue
import math

class Graph:
    def __init__(self,id="grafo", directed=False, auto=False):
        """
        Constructor
        """
        self.id=id
        self.nodes={}
        self.edges={}
        self.directed= directed
        self.auto=auto


    def addNode(self, id):
        """
        Agrega nodo al grafo, en caso de que no exista lo crea, si existe, regresa el nodo
        encontrado en el diccionario
        :param id= Node Id
        :return: node
        """
        new_node=self.nodes.get(id)
        if new_node is None:
            new_node=Node(id)
            self.nodes[new_node.id]=new_node
        return new_node

    def addEdge(self, source, target):
        """
        Agregar una arista al grafo, los nodos deben ser agregados con anterioridad, si no,
        levanta una excepcion
        :param source: Node source
        :param target: Node target
        """

        #Si los nodos no se encuentran en el grafo, levantar excepcion
        if self.nodes.get(source) is None or self.nodes.get(target) is None:
            raise Exception("Nodos no encontrados en el grafo, por favor agregarlos primero")

        #nodos en grafo
        nodeSource=self.nodes[source]
        nodeTarget=self.nodes[target]

        #crear el id de la arista
        idAux=str(source)+' -> '+str(target)

        #Si el grafo es no dirigido, checar que no se repitan los vertices en el diccionario
        repeated=False
        autoAux=False
        if not self.directed:
            idAuxNotDirected=str(target) + ' -> ' +str(source)
            aux=self.edges.get(idAuxNotDirected)
            if not(aux is None):
                repeated=True
        
        #Si el grafo es no autociclico, checar que source y target no sean iguales
        if not self.auto:
            if source is target:
                #print(source, target)
                autoAux=True
        
        new_edge= self.edges.get(idAux)
        
        """
        chequeo para grafo no dirigido y no autociclico.
        si la arista es nueva (no se encuentra en el grafo) y los nodos no son repetidos
        agrega nueva arista
        """
        if new_edge is None and repeated is False and autoAux is False:
            new_edge= Edge(idAux, nodeSource, nodeTarget)
            self.edges[new_edge.id]=new_edge
            nodeSource.attr.get("neighbors").append(nodeTarget)
            nodeTarget.attr.get("neighbors").append(nodeSource)
            nodeSource.attr.get("edges").append(new_edge)
            nodeTarget.attr.get("edges").append(new_edge)
            
        return new_edge


    def getDegree(self, id):
        """
        Obtener el grado de nodo
        :param: id: Node id
        :return: Node degree
        """
        node=self.nodes.get(id)
        if node is None:
            return 0
        return len(node.attr["neighbors"])
    
    def getNode(self, id):
        """
        Encontrar nodo en el grafo
        :param id: Node id to find
        :return: found node
        """
        return self.nodes.get(id)

    def getEdge(self, idS, idT):
        """
        Encontrar arista en el grafo
        :param idS: id source
        :param idT: id target
        :return: found Edge
        """
        idEdge=str(idS) + ' -> ' +str(idT)
        return self.edges.get(idEdge)

    def getTotalNodes(self):
        """
        Obtener el total de nodos en el grafo
        :return: total nodes
        """
        nodes=self.nodes
        if nodes is None:
            return 0
        return len(self.nodes)
    
    def getTotalEdges(self):
        """
        Obtener el total de aristas del grafo
        :return: total edges
        """
        edges=self.edges
        if edges is None:
            return 0
        return len(self.edges)
    
    ######GV files######
    def saveGV(self):
        """
        Crea el archivo .gv que posteriormente sera usado para la creacion de los grafos
        """

        #creacion del string gv
        graph=''
        graph+='digraph '+self.id+' {\n'
        
        for nodo in self.nodes:
            graph+=str(nodo)+';\n'

        for key, value in self.edges.items():
            graph+= value.id+';\n'

        graph+='}'

        #se escribe y salva el archivo
        name=self.id+'.gv'
        file = open(name, "w")
        file.write(graph)
        file.close()
        #se imprime q el file fue creado para saber cuando termina
        print('File GraphViz: '+name+' was created\n')
    

    def saveGVwithLabels(self):
        """
        Crea el archivo .gv con etiquetas que posteriormente sera usado para la creacion de los grafos
        """

        #creacion del string gv
        graph=''
        graph+='digraph '+self.id+' {\n'
        for key, value in self.nodes.items():
            graph+='\"nodo_'+str(value.id)+' ('+str(value.attr["distance"])+')\";\n'
        for key, value in self.edges.items(): 
            graph+= '\"nodo_'+str(value.source.id)+' ('+str(value.source.attr["distance"])+')\" -> '+'\"nodo_'+str(value.target.id)+' ('+str(value.target.attr["distance"])+')\" [weight='+str(value.attr["weight"])+'];\n'
        graph+='}'

        #se escribe y salva el archivo
        name=self.id+'.gv'
        f = open(name, "w")
        f.write(graph)
        f.close()
        
        #se imprime q el file fue creado para saber cuando termina
        print('File GraphViz: '+name+' was created\n')


    def saveGVwWeigth(self):
        """
        Crea el archivo .gv con etiquetas nodoID y peso arista que posteriormente sera usado para la creacion de los grafos
        """

        #creacion del string gv
        graph=''
        graph+='digraph '+self.id+' {\n'
        for key, value in self.nodes.items():
            graph+='\"'+str(value.id)+'\";\n'
        for key, value in self.edges.items(): 
            graph+= '\"'+str(value.source.id)+'\" -> '+'\"'+str(value.target.id)+'\" [weight='+str(value.attr["weight"])+'];\n'
        graph+='}'

        #se escribe y salva el archivo
        name=self.id+'.gv'
        f = open(name, "w")
        f.write(graph)
        f.close()
        
        #se imprime q el file fue creado para saber cuando termina
        print('File GraphViz: '+name+' was created\n')

    ############Proyecto 2 (BFS, DFS iterativo y DFS recursivo)###################   
    #BFS
    def BFS(self,s):
        """
        BFS
        :param s: nodo raiz
        """
        try:
            name = self.id + '_BFS_'+str(s)
            #Objeto grafo bfs
            bfsGraph = Graph(name)
            #Fila para el algoritmo BFS
            queue = []
            #Obtener objeto nodo a partir de nodo raiz
            s=self.nodes[s]
            # Agreagr nodo a la fila 
            queue.append(s)
            #Poner al nodo como visitado
            s.attr["visitedBFS"] = True
            #Agregar nodo a grafo BFS
            bfsGraph.addNode(s.id) 
            #Mientras encuentre nodos en la fila
            while queue: 
                #Sacar el primer objeto nodo de la fila 
                s = queue.pop(0)               
                #Obtener los vecinos del nodo s
                neighbors = s.attr["neighbors"]
                #Iterar los vecinos del nodo s
                for nodeNeighbor in neighbors:
                    #Si el nodo aún no ha sido visitado
                    if not (nodeNeighbor.attr["visitedBFS"]):
                        #Agregar nodo a la fila
                        queue.append(nodeNeighbor)
                        #Poner al nodo como visitado
                        nodeNeighbor.attr["visitedBFS"] = True
                        #Agregar nodo a grafo BFS
                        bfsGraph.addNode(nodeNeighbor.id) 
                        #Agregar arista a grafo BFS
                        bfsGraph.addEdge(s.id,nodeNeighbor.id)
            
            #reset atributo visitedBFS de los nodos por si se llama de nuevo
            for nodeId, node in self.nodes.items():
                node.attr["visitedBFS"] = False

            #regresa arbol BFS
            return bfsGraph
        except:
            print("Por favor agrega un nodo raiz valido")


    #DFS iterativo
    def DFS_I(self,s):
        """
        DFS iterativo
        :param s: nodo raiz
        """
        try:              
            name =  self.id +'_DFS_I_'+str(s)
            #Generar objeto grafo
            dfs_i_Graph = Graph(name)
            # Pila para el algoritmo DFS
            stack = []
            #Obtener objeto nodo a partir de nodo raiz
            s=self.nodes[s]
            #Agregar nodo a la pila
            stack.append(s)
            #agregar nodo s al grafo DFSI
            dfs_i_Graph.addNode(s.id)
            while stack:
                # Remover un elemento de la pila y asignarlo a s
                s = stack.pop()
                # Si no ha sido visitado marcarlo como visitado
                if not s.attr["visitedDFSI"]:
                    s.attr["visitedDFSI"] = True
                #Obtener los vecinos del nodo s
                neighbors = s.attr["neighbors"]
                #Iterar vecinos
                for neighbor in neighbors:
                    # Si un vecino no ha sido visitado, entrar
                    if not neighbor.attr["visitedDFSI"]:
                        #Agregar nodo al grafo DFSI
                        dfs_i_Graph.addNode(neighbor.id)
                        #Agregar nodo a la pila
                        stack.append(neighbor)
                        #Agregar el nodo raiz del actual nodo al atributo rootNodeDFSI 
                        neighbor.attr["rootNodeDFSI"]=s.id
                        ##dfs_i_Graph.addEdge(s.id,neighbor.id)
            #Iterar nodos para agregar aristas a los nodos
            for key, node in self.nodes.items():
                #reset atributo visitedDFSI de los nodos por si se llama de nuevo la funcion
                node.attr["visitedDFSI"] = False
                if node.attr["rootNodeDFSI"]>-1:
                    #Agregar arista
                    dfs_i_Graph.addEdge(key,node.attr["rootNodeDFSI"])
                    #reset atributo rootNodeDFSI de los nodos por si se llama de nuevo la funcion
                    node.attr["rootNodeDFSI"] =-1
                    
            return dfs_i_Graph
        except:
            print("Por favor agrega un nodo raiz valido")


    #DFS recursivo
    def DFS_R(self,s):
        """
        DFS recursivo usuario
        :param s: nodo raiz
        """
        try: 
            name = self.id +'_DFS_R_'+str(s)
            #Generar objeto grafo
            dfs_r_Graph = Graph(name)
            # Crear un conjunto de nodos visitados vacio
            visited = set()
            #Obtener objeto nodo a partir de nodo raiz
            s=self.nodes[s]
            # Llamar la funcion recursiva dfsRecursive
            self.dfsRecursive(visited,s,dfs_r_Graph)
            return dfs_r_Graph
        except:
            print("Por favor agrega un nodo raiz valido")

    def dfsRecursive(self,visited,node,dfs_r_Graph):
        """
        Auxiliar DFS recursivo 
        :param visited: nodos visitados
        :param node: nodo a trabajar
        :param dfs_r_Graph: grafica final
        """
        # Marcar el nodo como visitado
        visited.add(node.id)
        #Agregar nodo a grafo DFS    
        dfs_r_Graph.addNode(node.id) 
        #Obtener los vecinos del nodo s
        neighbors = node.attr["neighbors"]

        #Recorrer de manera recursiva los vecinos del nodo
        for neighbor in neighbors:
            #Si nodo no esta en el conjunto visitado
            if neighbor.id not in visited:
                #llamer recursivamente a dfsRecursive
                self.dfsRecursive(visited, neighbor, dfs_r_Graph)
                #Agregar arista
                dfs_r_Graph.addEdge(node.id,neighbor.id)
    

    #########Proyecto 3 - Algoritmo de Dijkstra###############
    def Dijkstra(self, s):
        """
        Algoritmo Dijkstra
        :param s: nodo raiz donde empieza el algoritmo
        """
        #Crear cola de prioridades
        q=PriorityQueue()
        #Crear lista S vacia
        S=[]
        dijkstraGraph=None

        for key, node in self.nodes.items():
            node.attr["parent"]=None
            node.attr["distance"]=float('inf')
            node.attr["edgeWeight"]=float('inf'),

        #Obtener objeto nodo a partir de nodo raiz
        nodeSource=self.nodes[s]
        #Poner en cero la distancia de nodo raiz
        nodeSource.attr["distance"]=0
        #igualar d a la distancia raiz
        d=nodeSource.attr["distance"]
        #agregar a la cola de prioridades distancia, nodo. esto se hace para mapear de acuerdo al nodo, obtener su distancia
        q.put((d, nodeSource.id))
        
        #mientras la cola de prioridades no este vacia ejecutar
        while not q.empty():
            #obtener elemento de la cola de prioridades de acuerdo a la distancia
            u = q.get()
            #obtener el objeto nodo, este sera el nodo U
            u=self.nodes[u[1]]
            #agrega a la lista el id del nodo que es visitado 
            S.append(u.id)
            #obtener el id de las aristas que se conectan con u
            edges_u_v = u.attr["edges"]

            #obtener aristas conectadas a u
            for edge in edges_u_v:

                #si el id del nodo target es igual al nodo u, v sera el nodo fuente
                if edge.target.id == u.id:
                    v= edge.source
                #de otra manera v sera el target
                else:
                    v=edge.target 
                #si el nodo V no se encuentra en la lista de visitados
                if v.id not in S:
                    #d= distancia nodo U + peso de la arista que conecta u,v
                    d=u.attr["distance"] + edge.attr["weight"]
                    #si la distancia de v es mayor a d
                    if v.attr["distance"] > d:   
                        #asignar a v el padre, el cual sera u                     
                        v.attr["parent"]=u.id
                        #asignar distancia a v
                        v.attr["distance"]=d
                        #asignar peso de arista para construir el grafo Dikstra posteriormente
                        v.attr["edgeWeight"]=edge.attr["weight"]
                        #agregar a la cola de prioridades el nodo v y su peso
                        q.put((d, v.id))
        #auxiliar para crear arbol dijkstra        
        aux=False
        
        #mientras la lista no este vacia
        while S:
            #sacar nodo Id de la lista
            nodeId=S.pop()
            #obtener nodo objeto a partir del id
            node=self.nodes[nodeId]
            #obtener nodo padre
            nodeParent=node.attr["parent"]
            #si es la primera vez que se entra
            if not aux:
                #crear el arbol dijkstra
                name= self.id+ "_Dijkstra" + "_nodeSource_"+ str(s) 
                dijkstraGraph = Graph(name)
                #poner el auxiliar a verdadero para que no vuelva a entrar
                aux=True
            
            #si el nodoPadre no es None
            if nodeParent is not None:                
                #agregar nodo al grafo dijkstra, si ya esta, regresa nodo objeto
                nodeAux=dijkstraGraph.addNode(node.id)
                #si la distancia es inf, entonces aun no se ha asignado
                if math.isinf(nodeAux.attr["distance"]):
                    #asignar la distancia del nodo dijkstra igual a la distancia del nodo del grafo original
                    nodeAux.attr["distance"]=node.attr["distance"]
                #agregar nodo padre al arbol dijkstra
                dijkstraGraph.addNode(nodeParent)
                #agregar arista, nodoSource= nodo Padre, nodoTarget= nodo
                dijkstraGraph.addEdge(nodeParent, node.id)
                #poner el peso de la arista del grafo dijkstra igual al peso de la arista del grafo original
                dijkstraGraph.setEdgeWeight(node.attr["edgeWeight"],nodeParent, node.id)
            #Si el nodo padre es none, entonces es el nodo raiz que el usuario asigno
            else:
                #poner en cero la distancia del nodo raiz del grafo dijkstra
                nodeAux=dijkstraGraph.getNode(nodeId)
                nodeAux.attr["distance"]=0
            #poner en inf (valor original) a la distancia del nodo del grafo original
            node.attr["distance"]=float('inf')
        #regresar 
        return dijkstraGraph
    

    def setEdgeWeight(self,weight, source, target):
        """
        Funcion que asigna el peso de una arista
        :param weight: peso
        :param source: nodo fuente
        :param target: nodo objetivo
        """
        #crear el id de la arista
        idAux=str(source)+' -> '+str(target)
        #obtener la arista objeto
        aux=self.edges.get(idAux)
        #si arista existe
        if aux is not None:
            #asignar a la arista el peso
            aux.attr["weight"]=weight

    #########Proyecto 4 - Algoritmos Kruskal y Prim###############

    def findSetParent(self,nodo):
        """
        Funcion auxiliar para encontrar el padre de un nodo para el algoritmo Kruskal Directo
        :param nodo: nodo a encontrar su padre
        """
        #obtener nodo objeto
        node=self.getNode(nodo)
        #si su Id del nodo es igual al conjunto que es elemento, regresa, es el padre
        if node.attr["setGroup"] == node.id:
            return node.id
        #recursion
        return self.findSetParent(node.attr["setGroup"])
   
    def removeEdge(self, edge):
        """
        Funcion auxiliar para el algoritmo Kruskal Inverso para remover una arista del grafo
        :param edge: arista a remover
        """
        #obtener nodos objeto
        u= edge.source
        v= edge.target
        #obtener vecinos de nodos
        neighborsU=u.attr["neighbors"]
        neighborsV=v.attr["neighbors"]
        #remover de la lista vecinos los nodos
        neighborsU.remove(v)
        neighborsV.remove(u)
        #remover la arista del grafo
        del self.edges[edge.id]
        #regresar
        return 

    def KruskalD(self):
        """        
        Algoritmo Kruskal
        """
        #Crear arbol Kruskal
        name= self.id+ "_kruskalD"
        kruskalDgraph= Graph(name)

        #Crear cola de prioridades
        q=PriorityQueue()
        #se inicializa el valor del mst en cero
        mst=0

        #agregar a la cola de prioridades (peso, arista). esto se hace para mapear de acuerdo a su peso, obtener arista
        for key, edge in self.edges.items():
            q.put((edge.attr["weight"], edge.id))
            #crear nodos en el arbol kruskal
            kruskalDgraph.addNode(edge.source.id)
            kruskalDgraph.addNode(edge.target.id)
            
        #mientras la cola de prioridades no este vacia ejecutar
        while not q.empty():
            #obtener elemento de la cola de prioridades de acuerdo a la distancia
            e = q.get()
            #obtener el peso y arista de la tupla e
            weightOriginal=e[0]
            edge=self.edges[e[1]]

            #obtener objetos nodos u,v del grafo kruskal
            u=kruskalDgraph.getNode(edge.source.id)
            v=kruskalDgraph.getNode(edge.target.id)

            #obtener el padre (conjunto al que pertenecen)
            setU=kruskalDgraph.findSetParent(u.id)
            setV=kruskalDgraph.findSetParent(v.id)

            #si pertenecen a conjuntos diferentes, ejecuta
            if setU != setV:
                #se suma el peso de la arista a mst
                mst+=weightOriginal

                #se agrega arista y se actualiza peso de arista con el original
                newEdge=kruskalDgraph.addEdge(u.id,v.id)
                newEdge.attr["weight"]=weightOriginal

                #obtener objeto nodo de los conjuntos u,v
                nodeSetU=kruskalDgraph.getNode(setU)
                nodeSetV=kruskalDgraph.getNode(setV)

                #si el ranking de v es mayor que u
                if nodeSetU.attr["rank"] < nodeSetV.attr["rank"]:
                    #se actualiza el conjunto u y se suma uno al conjunto v
                    nodeSetU.attr["setGroup"] = setV
                    nodeSetV.attr["rank"]+=1
                else:
                    #se actualiza el conjunto v y se suma uno al conjunto u
                    nodeSetV.attr["setGroup"] = setU
                    nodeSetU.attr["rank"]+=1                    
        
        #Se muestra el valor de MST
        print("-------Algoritmo Kruskal Directo-----")
        print(self.id)
        print("Valor de MST: "+ str(mst))
        print("-------------------------------------")

        #regresa arbol Kruskal directo
        return kruskalDgraph


    def KruskalI(self):
        """        
        Algoritmo Kruskal Inverso
        """
        #Crear arbol Kruskal inverso
        name= self.id+ "_kruskalI" 
        kruskalIgraph=Graph(name)
        
        #Agregar todos los nodos al grafo kruskal inverso
        for key, value in self.nodes.items():
            kruskalIgraph.addNode(value.id)

        #Crear cola de prioridades y se inicializa mst a cero
        q=PriorityQueue()
        mst=0

        #Agregar aristas al arbol Kruskal Inverso 
        for key, edge in self.edges.items():    
            u=edge.source.id
            v=edge.target.id
            edgeKruskal=kruskalIgraph.addEdge(u,v)
            #si la arista se agrego correctamente
            if edgeKruskal is not None:
                #actualizar peso de arista del arbol Kruskal Inverso y agregar arista a cola de prioridades
                weightOriginal=edge.attr["weight"]
                edgeKruskal.attr["weight"]=weightOriginal
                q.put((-edge.attr["weight"], edge.id))

        #obtener el total de nodos del arbol Kruskal                            
        totalNodes1=kruskalIgraph.getTotalNodes()

        #mientras la cola de prioridades no este vacia ejecutar
        while not q.empty():
            #obtener peso original y id de la arista de la cola de prioridades de acuerdo a la distancia
            weightOriginal, edgeId=q.get()
            #obtener arista objeto
            edge=kruskalIgraph.edges[edgeId]
            #remover arista del arbol
            kruskalIgraph.removeEdge(edge)
            #correr algoritmo dfs y obtener nodos
            dfs= kruskalIgraph.DFS_I(0)
            totalNodesBFS= dfs.getTotalNodes()
            #si el total de nodos del arbon es mayor que el del arbol dfs, hubo desconexion
            if  totalNodesBFS<totalNodes1:
                #sumar mst
                mst-=weightOriginal
                #agregar arista al arbol kruskal inverso y actualizar peso de la arista
                u=kruskalIgraph.getNode(edge.source.id)
                v=kruskalIgraph.getNode(edge.target.id)
                newEdge=kruskalIgraph.addEdge(u.id,v.id)
                newEdge.attr["weight"]= -weightOriginal                                
        
        #Mostrar Valor de MST
        print("-------Algoritmo Kruskal Inverso-----")
        print(self.id)
        print("Valor de MST: "+ str(mst))
        print("-------------------------------------")

        #regresar arbol Kruskal inverso
        return kruskalIgraph

    def Prim(self):
        """
        Algoritmo Prim
        """
        #reset a atributos parentP y distanceP de todos los nodos del grafo original
        for key, node in self.nodes.items():
            node.attr["parentP"]=None
            node.attr["distanceP"]=float('inf')

        #nodo raiz
        root=0
        #Crear cola de prioridades
        q=PriorityQueue()
        #Crear lista S vacia
        S=[]
        #Inicializar arbol prim vacio
        primGraph=None
        #Obtener objeto nodo a partir de nodo raiz
        nodeSource=self.nodes[root]
        #Poner en cero la distancia de nodo raiz
        d=nodeSource.attr["distanceP"]=0
        #agregar a la cola de prioridades distancia, nodo. esto se hace para mapear de acuerdo al nodo, obtener su distancia
        q.put((d, nodeSource.id))
        
        #mientras la cola de prioridades no este vacia ejecutar
        while not q.empty():
            #obtener distancia y nodoId de la cola de prioridades de acuerdo a la distancia
            d, u = q.get()
            #obtener el objeto nodo, este sera el nodo U
            u=self.nodes[u]
            #agrega a la lista el id del nodo que es visitado
            if u.id not in S:
                S.append(u.id)
            #obtener el id de las aristas que se conectan con u
            edges_u_v = u.attr["edges"]

            #obtener aristas conectadas a u
            for edge in edges_u_v:

                #si el id del nodo target es igual al nodo u, v sera el nodo fuente
                if edge.target.id == u.id:
                    v=edge.source
                #de otra manera v sera el target
                else:
                    v=edge.target 
                #si el nodo V no se encuentra en la lista de visitados
                if v.id not in S:
                    #se actualiza d con el peso de la arista
                    d =edge.attr["weight"]
                    #si la distancia de v es mayor a d
                    if v.attr["distanceP"] > d:   
                        #asignar a v el padre, el cual sera u                     
                        v.attr["parentP"]=u.id
                        #asignar distancia a v y agregar a cola de prioridades junto con su distancia
                        v.attr["distanceP"]= d
                        q.put((d, v.id))

        #auxiliar para crear arbol Prim        
        aux=False
        #inicializar mst en cero
        mst=0

        #mientras la lista no este vacia
        while S:
            #sacar nodo Id de la lista
            nodeId=S.pop()
            #obtener nodo objeto a partir del id
            node=self.nodes[nodeId]
            #obtener nodo padre
            nodeParent=node.attr["parentP"]

            #si es la primera vez que se entra
            if not aux:
                #crear el arbol Prim
                name= self.id+ "_Prim" + "_nodeSource_"+ str(root) 
                primGraph = Graph(name)
                #poner el auxiliar a verdadero para que no vuelva a entrar
                aux=True
            
            #si el nodoPadre no es None
            if nodeParent is not None:
                #obtener peso original de la arista
                weight_original=node.attr["distanceP"]
                
                #si la arista aun no se crea, actualizar mst, de otra manera, no sumar nada a mst
                if primGraph.getEdge(nodeParent, node.id) is None:
                    mst+=weight_original

                #agregar nodos al arbol Prim
                primGraph.addNode(nodeParent)
                nodeAux=primGraph.addNode(node.id)
                #agregar arista al arbol Prim
                edge=primGraph.addEdge(nodeParent, node.id)
                #poner el peso de la arista del arbol Prim igual al peso de la arista del grafo original
                edge.attr["weight"]=weight_original                           
                
            #Si el nodo padre es none, entonces es el nodo raiz
            else:
                #poner en cero la distancia del nodo raiz del grafo dijkstra
                nodeAux=primGraph.getNode(nodeId)
                nodeAux.attr["distanceP"]=0

        #Mostrar Valor de MST
        print("-------Algoritmo Prim-----")
        print(self.id)
        print("Valor de MST: "+ str(mst))
        print("-------------------------------------")
        #regresar arbol Prim
        return primGraph
    
    