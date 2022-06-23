import algorithms as a

def dijkstra_examples():
     #Nodo raiz para algoritmo Dijkstra
        rootNode=5

        ###########Grafo ErdosRenyi############################
        #Grafo ErdosRenyi de 10 nodos
        grafoErdos=a.randomErdosRenyi(10, 20, directed=False, auto=False)
        dijkstra=grafoErdos.Dijkstra(rootNode)
        grafoErdos.saveGVwithLabels()
        dijkstra.saveGVwithLabels()

        #Grafo ErdosRenyi de 250 nodos
        grafoErdos=a.randomErdosRenyi(100, 200, directed=False, auto=False)
        dijkstra=grafoErdos.Dijkstra(rootNode)
        grafoErdos.saveGVwithLabels()
        dijkstra.saveGVwithLabels()
    
        #####################Grafo Gilbert ####################################

        #Grafo Gilbert de 10 nodos
        grafoGilbert=a.randomGilbert(10, 0.6, directed=False, auto=False)
        dijkstra=grafoGilbert.Dijkstra(rootNode)
        grafoGilbert.saveGVwithLabels()
        dijkstra.saveGVwithLabels()  

        #Grafo Gilbert de 100 nodos
        grafoGilbert=a.randomGilbert(100, 0.2, directed=False, auto=False)
        dijkstra=grafoGilbert.Dijkstra(rootNode)
        grafoGilbert.saveGVwithLabels()
        dijkstra.saveGVwithLabels()


        #####################Grafo Malla################################

        #Grafo Malla de 20 nodos
        grafoMalla=a.gridGraph(10,2,directed=False)
        dijkstra=grafoMalla.Dijkstra(rootNode)
        grafoMalla.saveGVwithLabels()
        dijkstra.saveGVwithLabels()

        #Grafo Malla de 100 nodos
        grafoMalla=a.gridGraph(10,10,directed=False)
        dijkstra=grafoMalla.Dijkstra(rootNode)
        grafoMalla.saveGVwithLabels()
        dijkstra.saveGVwithLabels()

        ###########################Grafo Geografico#######################################

        #Grafo Geografico de 10 nodos
        grafoGeografico=a.randomGeografico(10, 0.5, directed=False, auto=False)
        dijkstra=grafoGeografico.Dijkstra(rootNode)
        grafoGeografico.saveGVwithLabels()
        dijkstra.saveGVwithLabels()

        #Grafo Geografico de 100 nodos
        grafoGeografico=a.randomGeografico(100, 0.3, directed=False, auto=False)
        dijkstra=grafoGeografico.Dijkstra(rootNode)
        grafoGeografico.saveGVwithLabels()
        dijkstra.saveGVwithLabels()
        #####################Grafo BarabasiAlbert################################
        
        #Grafo BarabasiAlbert de 10 nodos
        grafoBarabasiAlbert= a.randomBarabasiAlbert(10, 5, directed=False, auto=False)
        dijkstra=grafoBarabasiAlbert.Dijkstra(rootNode)
        grafoBarabasiAlbert.saveGVwithLabels()
        dijkstra.saveGVwithLabels()

        #Grafo BarabasiAlbert de 100 nodos
        grafoBarabasiAlbert= a.randomBarabasiAlbert(100, 3, directed=False, auto=False)
        dijkstra=grafoBarabasiAlbert.Dijkstra(rootNode)
        grafoBarabasiAlbert.saveGVwithLabels()
        dijkstra.saveGVwithLabels()

        #####################Grafo DorogovtsevMendes################################

        #Grafo DorogovtsevMendes de 10 nodos
        grafoDorogovt= a.randomDorogovtsevMendes(n=10, directed=False)
        dijkstra=grafoDorogovt.Dijkstra(rootNode)
        grafoDorogovt.saveGVwithLabels()
        dijkstra.saveGVwithLabels()

        #Grafo DorogovtsevMendes de 100 nodos
        grafoDorogovt= a.randomDorogovtsevMendes(n=100, directed=False)
        dijkstra=grafoDorogovt.Dijkstra(rootNode)
        grafoDorogovt.saveGVwithLabels()
        dijkstra.saveGVwithLabels()
