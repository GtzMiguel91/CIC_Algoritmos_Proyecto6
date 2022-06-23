import algorithms as a

def kruskal_prim_examples():              
        # ###########Grafo ErdosRenyi############################
        #Grafo ErdosRenyi de 10 nodos
        grafoErdos=a.randomErdosRenyi(10, 40, directed=False, auto=False)
        createSaveKrPrG(grafoErdos)
      
        #Grafo ErdosRenyi de 100 nodos
        grafoErdos=a.randomErdosRenyi(100, 350, directed=False, auto=False)
        createSaveKrPrG(grafoErdos)
    
        #####################Grafo Gilbert ####################################
        # #Grafo Gilbert de 10 nodos
        grafoGilbert=a.randomGilbert(10, 0.6, directed=False, auto=False)
        createSaveKrPrG(grafoGilbert)

        # #Grafo Gilbert de 100 nodos
        grafoGilbert=a.randomGilbert(100, 0.1, directed=False, auto=False)
        createSaveKrPrG(grafoGilbert)

        # #####################Grafo Malla################################
        # #Grafo Malla de 20 nodos
        grafoMalla=a.gridGraph(5,4,directed=False)
        createSaveKrPrG(grafoMalla)

        # #Grafo Malla de 100 nodos
        grafoMalla=a.gridGraph(10,10,directed=False)
        createSaveKrPrG(grafoMalla)

        # ###########################Grafo Geografico#######################################
        # #Grafo Geografico de 10 nodos
        grafoGeografico=a.randomGeografico(10, 0.6, directed=False, auto=False)
        createSaveKrPrG(grafoGeografico)

        # #Grafo Geografico de 100 nodos
        grafoGeografico=a.randomGeografico(100, 0.3, directed=False, auto=False)
        createSaveKrPrG(grafoGeografico)

     

        # #####################Grafo DorogovtsevMendes################################
        # #Grafo DorogovtsevMendes de 10 nodos
        grafoDorogovt= a.randomDorogovtsevMendes(n=10, directed=False)
        createSaveKrPrG(grafoDorogovt)

        # #Grafo DorogovtsevMendes de 100 nodos
        grafoDorogovt= a.randomDorogovtsevMendes(n=100, directed=False)
        createSaveKrPrG(grafoDorogovt)

        # #####################Grafo BarabasiAlbert###############################
        #Grafo BarabasiAlbert de 10 nodos
        grafoBarabasiAlbert= a.randomBarabasiAlbert(10, 5, directed=False, auto=False)
        createSaveKrPrG(grafoBarabasiAlbert)

        #Grafo BarabasiAlbert de 100 nodos
        grafoBarabasiAlbert= a.randomBarabasiAlbert(100, 5, directed=False, auto=False)
        createSaveKrPrG(grafoBarabasiAlbert)

def createSaveKrPrG(graph):
        kruskalD=graph.KruskalD()
        prim=graph.Prim()
        kruskalI=graph.KruskalI()

        graph.saveGVwWeigth()
        kruskalD.saveGVwWeigth()
        prim.saveGVwWeigth()
        kruskalI.saveGVwWeigth()