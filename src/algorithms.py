from graph import Graph
from random import randint
from random import random

def randomErdosRenyi(n, m, directed=False, auto=False):
    """
    Genera grafo aleatorio con el modelo Erdos-Renyi
    :param n: número de nodos (> 0)
    :param m: número de aristas (>= n-1)
    :param directed: el grafo es dirigido?
    :param auto: permitir auto-ciclos?
    :return: grafo generado
    """
    #Crear nuevo grafo
    name='Erdos_Renyi_nodes_'+str(n) +'_edges_'+str(m)
    graph= Graph(name, directed, auto);

    #Si el numero de nodos es cero, regresar grafo vacio.
    if n==0:
        return graph

    #Agregar los n nodos  al grafo
    for i in range(n):
        graph.addNode(i)

    #generar aristas
    for i in range(m):
        #generara nodos random
        node1= randint(0, n-1)
        node2= randint(0, n-1)
        #agregar arista
        graph.addEdge(node1,node2)
    return graph

def randomGilbert(n, p, directed=False, auto=False):
    """
    Genera grafo aleatorio con el modelo Gilbert
    :param n: número de nodos (> 0)
    :param p: probabilidad de crear una arista (0, 1)
    :param directed: el grafo es dirigido?
    :param auto: permitir auto-ciclos?
    :return: grafo generado
    """
    #Crear nuevo grafo
    name='Gilbert_nodes_'+str(n) +'_probability_'+str(p)
    graph= Graph(name,directed, auto)

    #Si el numero de nodos es cero, regresar grafo vacio.
    if n==0:
        return graph

    #Agregar los n nodos  al grafo
    for i in range(n):
        graph.addNode(i)

    #for para obtener nodo source
    for i in range(n):
        #for para obtener nodo target
        for j in range(n):
            #obtener numero random
            randomN= random()
            #si el numero random es menor a la probabilidad, agregar arista
            if randomN<p:
                graph.addEdge(i,j)    
    return graph

def gridGraph(m, n, directed=False):
    """
    Genera grafo de malla, dicho grafa se puede ver como una matriz que estara unida
    :param m: número de columnas (> 1)
    :param n: número de filas (> 1)
    :param dirigido: el grafo es dirigido?
    :return: grafo generado
    """

    #Crear nuevo grafo
    name='Grid_columns_'+str(m) +'_rows_'+str(n)
    graph= Graph(name,directed);

    #Si m o n es cero, regresar grafo vacio.
    if n==0 or m==0:
        return graph

    #diccionario auxiliar para el mapeo de las ubicacion en matriz con id del nodo
    #con este diccionario se buscara el id del nodo que servira para ir creando las conexiones
    #ejemplo de 3 columnas x 2 filas:
    #{[0,0]:0, [0,1]:1, [1,0]:2, [1,1]:3, [2,0]:4, [2,1]:5}
    dictNodos={}
    key='' #key del diccionario
    node=0 #id del nodo de la grafica
    nodeDict=0 #valor del key diccionario que ayudara a ubicar al nodo
    
    #for que itera columnas
    for i in range(m):
        #for que itera filas
        for j in range(n):
            #key para diccionario
            key=str([i,j])
            #si se ubica en [0,0], agrega el primer nodo a la grafica para empezar
            if i==0 and j==0:
                #se agrega la ubicacion del nodo
                dictNodos[key]=node
                graph.addNode(node)
            #si se esta en la primer columna y fila mayor a cero, se agrega nodo 
            #a la grafica y se agrega la arista entre este nodo y el de una fila antes
            elif i==0 and j>0:
                #se agrega la ubicacion del nodo
                dictNodos[key]=node                
                graph.addNode(node)
                key=str([i,j-1])
                nodeDict=dictNodos[key]
                graph.addEdge(node, nodeDict)
            #si se esta en cualquier otra columna
            else:
                #key para diccionario
                key=str([i,j])
                
                #si se esta en la fila 0, se agrega el nodo a la grafica y la arista que une a este
                # con el nodo de la columna anterior 
                if j==0:
                    dictNodos[key]=node                                     
                    graph.addNode(node)
                    key=str([i-1,j])
                    nodeDict=dictNodos[key]
                    #print(node, 'source')
                    #print(nodeDict,'target')
                    graph.addEdge(node, nodeDict)
                #si se esta en cualquier otra fila, se agrega el nodo a la grafica y la arista que une a este
                # con el nodo de la columna anterior y la arista con la de la fila anterior 
                else:
                    dictNodos[key]=node
                    graph.addNode(node)
                    key=str([i,j-1])
                    nodeDict=dictNodos[key]
                    graph.addEdge(node, nodeDict)
                    key=str([i-1,j])
                    nodeDict=dictNodos[key]
                    graph.addEdge(node, nodeDict)
            #se aumenta el id del nodo
            node+=1
    #print(dictNodos)
    #print("=============")
    #print(nodeDict)
    return graph

def randomGeografico(n, r, directed=False, auto=False):
  '''
  Genera grafo aleatorio con el modelo geográfico simple
  :param n: número de nodos (> 0)
  :param r: distancia máxima para crear un nodo (0, 1)
  :param dirigido: el grafo es dirigido?
  :param auto: permitir auto-ciclos?
  :return: grafo generado
  '''

  #Crear nuevo grafo
  name='Geografico_nodes_'+str(n)+'_distanciaMax_'+str(int(r*10))
  graph = Graph(name,directed,auto)
  
  #Si el numero de nodos es cero, regresar grafo vacio.
  if n==0:
      return graph
  
  #Agregar los n nodos  al grafo y agregar atributo geoX_Y coordenadas del nodo para posteriormente
  #obtener la distancia entre nodos
  for i in range(n):
    graph.addNode(i)
    node=graph.getNode(i)
    node.attr["geoX_Y"]= [random(),random()]
  
  #for para obtener nodo source
  for i in range(n):
    #se obtiene las coodenadas de nodo source
    node=graph.getNode(i)
    nodeSource=node.attr["geoX_Y"]
    #for para obtener nodo target
    for j in range(n):
      #se obtiene las coordenadas del nodo target
      node=graph.getNode(j)
      nodeTarget=node.attr["geoX_Y"]
      #se calcula la distancia entre ellos
      d=dist(nodeSource[0], nodeTarget[0], nodeSource[1], nodeTarget[1]);

      #si la distancia dada r es mayor que la calculada entre nodos, se agrega arista
      if d <=r:
          graph.addEdge(i,j)
  return graph

#funcion para calcular distancia entre nodos
def dist(x1, x2, y1, y2):
    return ((x2-x1)**2+(y2-y1)**2)**0.5


def randomBarabasiAlbert(n, d, directed=False, auto=False):
    """
     Genera grafo aleatorio con el modelo Barabasi-Albert
    :param n: número de nodos (> 0)
    :param d: grado máximo esperado por cada nodo (> 1)
    :param dirigido: el grafo es dirigido?
    :param auto: permitir auto-ciclos?
    :return: grafo generado
    """

    #Crear nuevo grafo
    name='BarabasiAlbert_nodes_'+str(n)+'_GradoMax_'+str(d)
    graph = Graph(name,directed,auto)

    #Si el numero de nodos es cero, regresar grafo vacio.
    if n==0:
        return graph

    #Agregar los n nodos  al grafo
    for i in range(n):
        graph.addNode(i)

    #for para obtener nodo source
    for i in range(n):
        #for para obtener nodo target
        for j in range(n):
            #obtener grados de los nodos
            nodeSource = graph.getDegree(i)
            nodeTarget= graph.getDegree(j)

            #si el grado del nodo source y nodo target son menores que el grado max esperado 
            if nodeSource<d and nodeTarget<d:
                #se calcula probabilidad
                p = 1 - (nodeSource/d)

                #si la probabilidad es mayor a un num random, agraga arista entre nodo source y target
                if random() < p:
                    graph.addEdge(i,j)
    return graph


def randomDorogovtsevMendes (n, directed=False):
    '''
    Genera grafo aleatorio con el modelo Dorogovtsev-Mendes
    :param n: número de nodos (≥ 3)
    :param dirigido: el grafo es dirigido?
    :return: grafo generado
    '''
    #Crear nuevo grafo
    name='Dorogovtsev_Mendes_nodes_'+str(n)
    graph = Graph(name,directed)

    #Si el numero de nodos es menor o igual a 3, regresar grafo vacio.
    if n<=3:
        return graph

    #Agregar los n nodos  al grafo
    for i in range(n):
        graph.addNode(i)

    #Se crea el triangulo
    graph.addEdge(0,1)
    graph.addEdge(1,2)
    graph.addEdge(2,0)

    #for para obtener el nodo target, se empieza a partir del 4to nodo porque ya se usaron los 3
    #primeros para crear el triangulo
    for i in range(3, n):
        #se obtiene el total de aristas del grafo
        totalEdges = graph.getTotalEdges()
        #se obtiene un numero entero random de rango 0 a totalEdges que servira despues para 
        #seleccionar al azar una arista
        randomN = randint(0, totalEdges-1)
        #se obtienen los ids de las aristas y se convierte a una lista
        edgesInGraph = list(graph.edges.keys())
        #se selecciona una arista al azar
        randomEdge = edgesInGraph[randomN]
        
        #se obtienen los nodos extremos de dicha arista random
        n1=graph.edges[randomEdge].source.id
        n2=graph.edges[randomEdge].target.id

        #se agregan aristas entre nodo Target y nodos Extremos
        graph.addEdge(i,n1)
        graph.addEdge(i,n2)

    return graph
