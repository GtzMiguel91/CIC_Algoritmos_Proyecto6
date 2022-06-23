import algorithms as a

def graphs_examples():
    
        #Grafo ErdosRenyi de 30 nodos
        grafoErdos=a.randomErdosRenyi(30, 30, directed=False, auto=False)
        grafoErdos.saveGV()
        #Grafo ErdosRenyi de 100 nodos
        grafoErdos=a.randomErdosRenyi(100, 200, directed=False, auto=False)
        grafoErdos.saveGV()
        #Grafo ErdosRenyi de 500 nodos
        grafoErdos=a.randomErdosRenyi(500, 700, directed=False, auto=False)
        grafoErdos.saveGV()

        #Grafo Gilbert de 30 nodos
        grafoGilbert=a.randomGilbert(30, 0.4, directed=False, auto=False)
        grafoGilbert.saveGV()
        #Grafo Gilbert de 100 nodos
        grafoGilbert=a.randomGilbert(100, 0.2, directed=False, auto=False)
        grafoGilbert.saveGV()
        #Grafo Gilbert de 500 nodos
        grafoGilbert=a.randomGilbert(500, 0.2, directed=False, auto=False)
        grafoGilbert.saveGV()

        #Grafo Malla de 30 nodos
        grafoMalla=a.gridGraph(10,3,directed=False)
        grafoMalla.saveGV()
        #Grafo Malla de 100 nodos
        grafoMalla=a.gridGraph(10,10,directed=False)
        grafoMalla.saveGV()
        #Grafo Malla de 500 nodos
        grafoMalla=a.gridGraph(20,25,directed=False)
        grafoMalla.saveGV()

        #Grafo Geografico de 30 nodos
        grafoGeografico=a.randomGeografico(30, 0.5, directed=False, auto=False)
        grafoGeografico.saveGV()
        #Grafo Geografico de 100 nodos
        grafoGeografico=a.randomGeografico(100, 0.3, directed=False, auto=False)
        grafoGeografico.saveGV()
        #Grafo Geografico de 500 nodos
        grafoGeografico=a.randomGeografico(500, 0.1, directed=False, auto=False)
        grafoGeografico.saveGV()

        #Grafo BarabasiAlbert de 30 nodos
        grafoBarabasiAlbert= a.randomBarabasiAlbert(30, 5, directed=False, auto=False)
        grafoBarabasiAlbert.saveGV()
        #Grafo BarabasiAlbert de 100 nodos
        grafoBarabasiAlbert= a.randomBarabasiAlbert(100, 3, directed=False, auto=False)
        grafoBarabasiAlbert.saveGV()
        #Grafo BarabasiAlbert de 500 nodos
        grafoBarabasiAlbert= a.randomBarabasiAlbert(500, 2, directed=False, auto=False)
        grafoBarabasiAlbert.saveGV()


        #Grafo DorogovtsevMendes de 30 nodos
        grafoDorogovt= a.randomDorogovtsevMendes(n=30, directed=False)
        grafoDorogovt.saveGV()
        #Grafo DorogovtsevMendes de 100 nodos
        grafoDorogovt= a.randomDorogovtsevMendes(n=100, directed=False)
        grafoDorogovt.saveGV()
        #Grafo DorogovtsevMendes de 500 nodos
        grafoDorogovt= a.randomDorogovtsevMendes(n=500, directed=False)
        grafoDorogovt.saveGV()